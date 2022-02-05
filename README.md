# Notion-to-Github

Notion에서 작성하여 export한 파일을 자동으로 GitHub 블로그(jekyll)에 업로드 가능한 형태로 변환해주는 프로그램입니다.  Notion 글에 삽입된 이미지를 자동으로 처리하여 GitHub 블로그에 편리하게 포스팅할 수 있습니다. 

이 프로그램은 파이썬3 버전으로 작성 되었습니다. 

# What's New
- [2022.02.06] Notion의 export 포맷 변경에 따른 업데이트. Notion에서 md 파일 추출시 이미지 관련 포맷이 `![이미지주소](이미지주소)`에서 `![캡션](이미지주소)`로 변경되었습니다. 

# 기능

- *_posts* 폴더에 있는 Notion에서 Export된 압축 파일을 jekyll에 업로드할 수 있는 형태로 바꿔줍니다.
    - md파일: 날짜-{notion note의 제목}.md로 변환 후 *_posts* 폴더로 이동됩니다.
    - image파일: 폴더명을 *날짜-{notion note의 제목}*의 새로운 이미지 폴더가 생성된 후 *assets/images* 폴더로 이동됩니다.
- *title, meta_date* 메타정보를 자동으로 인식하여 삽입합니다.
- *subtitle, categories, tag* 메타정보를 수동으로 입력받아 삽입합니다.

# 사용법

1. `notion-to-github-python.py`를 *본인 로컬 PC github 블로그 디렉터리 (username.github.io)* 에 저장합니다.  아래의 명령어로도 해당 작업이 가능합니다. 
- Window OS

```bash
git clone https://github.com/jeongHwarr/notion-to-github-python.git
cd notion-to-github-python
xcopy notion-to-github-python.py <본인의 github 블로그 디렉터리> 
```

- Linux OS

```bash
git clone https://github.com/jeongHwarr/notion-to-github-python.git
cd notion-to-github-python
sudo cp notion-to-github-python.py <본인의 github 블로그 디렉터리> 
```

2. 아래의 방법으로 Notion 페이지를 Export하여 본인 github 블로그 디렉터리 안 _*posts* 폴더*(username.github.io/_posts)*에 옮겨줍니다. 

![/assets/images/2021-02-03-notion_to_github_python/untitled.png](/assets/images/2021-02-03-notion_to_github_python/untitled.png)

![/assets/images/2021-02-03-notion_to_github_python/untitled_1.png](/assets/images/2021-02-03-notion_to_github_python/untitled_1.png)

3. `notion_to_github-python.py`를 실행시킵니다. 

```bash
python notion-to-github-python.py
```

4. 파일의 메타 정보를 입력합니다. 

![/assets/images/2021-02-03-notion_to_github_python/untitled_2.png](/assets/images/2021-02-03-notion_to_github_python/untitled_2.png)

5. 압축 파일 삭제 여부를 선택합니다. (`y`: 삭제, `n`: 미삭제) 

![/assets/images/2021-02-03-notion_to_github_python/untitled_3.png](/assets/images/2021-02-03-notion_to_github_python/untitled_3.png)

6. 작업물을 git에 add하고 commit 및 push를 하여 업로드 합니다. 

# 예정

- [ ]  파이썬 환경이 아니더라도 프로그램 이용이 가능하도록 exe 파일로 배포 예정입니다.

# 참고

[https://github.com/uoneway/notion-to-github-pages](https://github.com/uoneway/notion-to-github-pages)의 글과 코드를 많이 참고하였습니다. 감사합니다.
