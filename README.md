# Tistory-To-Wordpress
티스토리 게시물을 워드프레스로 이전하는 Python 코드입니다.  
개인적으로 필요하여 작성한 코드이나, 필요 시 자유롭게 사용 가능합니다.

### 주의사항
티스토리 게시물의 HTML을 파싱하여 워드프레스에 게시합니다.  
따라서 다음과 같은 제약이 있습니다.
1. 텍스트, 이미지 등 요소의 정렬이 풀릴 수 있습니다.
2. 텍스트 서식이 풀릴 수 있습니다.
3. 워드프레스에서 게시물을 편집할 시 블록 모드를 사용할 수 없습니다. (편집 자체는 가능합니다.)
4. 게시물에 사용된 이미지는 워드프레스에 저장되지 않고 카카오 CDN으로 가져옵니다. 따라서 카카오 서버 접속 장애 시 이미지 로딩이 되지 않을 수 있습니다.

### 사용법
1. 다음과 같은 Python 모듈이 필요합니다.
```
pip install requests
pip install beautifulsoup4
pip install python-wordpress-xmlrpc
```

2. 티스토리 게시물을 모두 공개로 변경합니다.
(Python으로 티스토리 로그인을 하여 세션 유지를 하면 비공개 글도 옮길 수 있을 것 같긴 한데, 이 당시 귀찮아서 구현하지 않았습니다. 나중에 업데이트 할 의사가 있으나, 일단 필요시 직접 구현하여 사용해 주시기 바랍니다.)

3. migrate.py의 9라인, 10라인, 39 ~ 43라인에 정확한 정보를 입력합니다.

4. 코드를 실행하면 자동으로 마이그레이션이 진행됩니다.
