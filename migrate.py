import requests
from bs4 import BeautifulSoup

from wordpress_xmlrpc import Client
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods import posts

class Task():
    tURL = "티스토리 URL 입력"
    tNUM = "티스토리 마지막 게시물 글 번호(게시물 개수) 입력"

    def __init__(self):
        if self.tURL[-1] != '/':
            self.tURL += '/'
        self.migrate()
        print("migration 성공")

    def migrate(self):
        for i in range(1, self.tNUM + 1):
            self.getPost(i)

    def getPost(self, num):
        res = requests.get(self.tURL + str(num))
        if res.status_code != 200:
            print(str(num) + "번 게시물 연결 실패")
            return None
            
        bs = BeautifulSoup(res.text, "html.parser")
            
        title = bs.select_one('#content > div > div.post-cover > div > h1').text
        category = bs.select_one('#content > div > div.post-cover > div > span.category').text
        if category.find('/') != -1:
            category = category[category.index('/') + 1:]
        con = bs.select_one('#content > div > div.entry-content > div.tt_article_useless_p_margin.contents_style')
        
        self.move(title, category, str(con))

    def move(self, title, category, con):
        wd_tag="태그"
        url = '워드프레스 URL 입력'
        id ='ID 입력'
        password ='패스워드 입력'
        #wd_slug="슬러그"


        wp = Client(url, id, password)
        post = WordPressPost()
        post.post_status = 'publish'
        post.title = title
        post.content = con
        #post.slug= wd_slug
        post.terms_names = {
            "category": [category]
        }
        wp.call(posts.NewPost(post))


if __name__ == "__main__":
    Task()
