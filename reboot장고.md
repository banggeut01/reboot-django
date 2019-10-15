# 장고 - 자주 보는 오류

> 주의할 점 3가지!

* 불러오지 않은 것은 절대 쓸 수 없다!!
  * import해서 가져와야 한다!
* 클래스는 `CamelCase`, 함수나 변수는 `snake_case`
  * 일반적으로 app은 `복수형`, class는 `단수형`
* 재사용성 높이자!
  * 변수, 함수, 클래스 등

> 자주 발견되는 오류

* 무조건 `model`부터 정의하고 `makemigrations`을 하는 습관

  ```bash
  # error message
  No changes detected
  ```

  db > django > models > class Model

> 데이터베이스 변경되었을 때

- db.splite3 삭제
- migrations > 0001*.py와 같은 파일 삭제
  - 0001*.py와 같은 파일을 직접 수정하는 것은 불가능
- 새롭게 `makemigrations`, `migrate`

> HTML FORM 작성시

* `form action=` 지정시 끝에 `/` 붙이기

  * 예) `form action="/article/create/"` (o)

    `form action="/article/create"`(x) => GET방식 일 땐, 동작하는 것 처럼 보일 수 있으나 꼭 `/`를 붙여주자!

  ```
  # error message
  You called this URL via POST, ... (note the trailing slash)
  ```

> Reverse error message

* URL을 보자

> POST로 바꿀 때

* `html`에서 method 값 바꿔주기

* 토큰 넣어주기

  ```html
  {% csrf_token %}
  ```

  ```bash
  # GET log message
  [10/Sep/2019 11:31:43] "GET /articles/20/update/?title=%EB%B0%B0%EC%A7%B1%EA%B3%A0%ED%8C%8C&content=%E3%85%A0%E3%85%A0 HTTP/1.1" 302 0
  
  # POST log message
  [10/Sep/2019 11:45:23] "POST /articles/22/update/ HTTP/1.1" 302 0
  ```


> such no table ... articles_Article

* Model 명 수정한 경우 다시 migrate해줘야 한다.
* migrate하게 되면
  
* 앱이름_모델명 table 생겨남
  
* 설치 오류

  ```shell
  ModuleNotFoundError: No module named 'bootstrap4'
  ```

  ```shell
  $ pip install django-bootstrap4
  ```


> path('signup/', views.signup, name='signup'), # accounts C
> NameError: name 'views' is not defined

* view가 없을 때 발생하는 오류

* urlts.py 에서 view를 import한다.

  ```python
  from . import views
  ```

  

# Review

* 가상환경 만들기

  ```bash
  $ python -m venv venv
  ```

  

* 가상환경 실행

  ```bash
  $ source venv/Scripts/activate
  ```

  

* django 설치

  설치 확인

  ```bash
  $ pip list
  ```

  설치

  ```bash
  $ pip install django 
  ```

  `settings.py`의 INSTALLED_APPS에 `django_extiensions` 있다면,

  ```bash
  # error message
  ModuleNotFoundError: No module named 'django_extensions'
  
  # solution
  $ pip install django-extensions
  ```

  이러한 error가 뜨면, 가상환경에서 설치한 것이 아닌, 글로벌 영역에서 설치했던 것이다.

* git 설정

  ```bash
  $ git init
  $ touch .gitignore
  $ pip freeze > requirments.txt
  ```

* 장고 프로젝트 시작

  ```bash
  $ django-admin startproject reboot .
  ```

* 서버 실행

  ```bash
  $ python manage.py runserver
  ```

* `settings.py`설정 - 한국어로

  ```python
  # reboot/settings.py
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  ```

* app 생성

  ```bash
  $ python manage.py startapp articles
  ```

* app 등록

  ```python
  # reboot/settings.py
  INSTALLED_APPS = [
      'articles',
      # ...
  ]
  ```

  

* `reboot/urls.py` 설정

  * include

  ```python
  from django.contrib import admin
  from django.urls import path, include # include import
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls')), # articles.urls에 있는 것을 포함하겠다.
  ]
  ```

* `articles/urls.py` 설정

  * **urlpatterns 반드시 필요하다.**

  ```python
  from django.urls import path
  from . import views # 현 디렉토리에 있는 view.py를 import
  
  # 반드시 있어야하는 변수
  urlpatterns = [
      path('', views.index),
  ]
  ```

* html 생성(템플릿 생성)

  템플릿을 생성하기 위해 app 이름으로 된 폴더를 생성한다.

  articles > templates > articles > index.html

  ```python
  from django.shortcuts import render
  
  # Create your views here.
  def index(request):
      return render(request, 'articles/index.html')
  ```

# Django

## Model 정의

* title : charfield
* content : textfield
* created_at : auto_now_add, datetimefield
* updated_at : auto_now, datetimefield

```python
from django.db import models

# Create your models here.
class Aricle(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



### 마이그레이션 

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



### admin 설정 ## error

```bash
$ python manage.py createsuperuser
```

```python
# articles/admin.py
from django.contrib import admin
from .models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at', 'updated_at']
admin.site.register(Article, ArticleAdmin)
```

http://127.0.0.1:8000/admin/



## CRUD

* C
  * `/new/` : 글 작성 form
  * `/create/` : 저장 후 index로 보내기(redirect)
* R
  * `/1/` : detail 함수에서 처리
* D
  * `/1/delete/` : 삭제 후 index로 보내기
* U
  * `/1/edit/` : 글 수정 form
  * `/1/update/` : 저장 후 Read로 보내기

# 데이터베이스

## N:1관계

### ipython - shell_plus

아래는 error!

```shell
In [1]: comment = Comment()

In [2]: comment.content = '댓글입
   ...: 니다.'

In [3]: comment.sava()
```

외래키를 가지고 있는 comment에게 관계를 지정해주지 않았기 때문

```shell
In [5]: article = Article.objects..get(pk=18)

In [6]: article
Out[6]: <Article: Article object (13)>

# 첫번째 댓글 생성
In [7]: comment
Out[7]: <Comment: Comment object (None)> # 아직 db에 저장되지 않음

In [8]: comment.article = article

In [9]: comment.save()

In [10]: comment
Out[10]: <Comment: Comment object (1)> # db에 저장되어 pk 1값을 가짐

# 댓글과 연결된 게시글
In [22]: comment.article
Out[22]: <Article: Article object (13)>

# 게시글에 있는 댓글 모두 검색
In [24]: article.comment_set.all()
Out[24]: <QuerySet [<Comment: Comment object (1)>]>

# 두번째 댓글 생성
In [25]: Comment.objects.create(content="댓글2", article=article)
Out[25]: <Comment: Comment object (2)>

# 게시글에 있는 댓글 모두 가져오기
In [26]: article.comment_set.all()
Out[26]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>
```

* N:1 관계

  * Article(글) - 1, Comment(댓글) - N일 때(하나의 글에 여러개의 댓글 존재),

    comment에서 article 찾을 시 `comment.article`로 조회

    article에서는 comment 찾을 시 `article.comment_selt.all()`

### 외래키 (N:1관계에서)

* 다음과 같이 설정함

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=30)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
  class Comment(models.Model):
      content = models.CharField(max_length=140)
      created_at = models.DateTimeField(auto_now_add=True)
      # 외래키 => article_id 외래키 생성
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
  ```

* 외래키 지정 옵션

  * CASCADE : 글이 삭제되었을 때 모든 댓글을 삭제
  * PROTECT : 댓글이 존재하면 글 삭제 안됨
  * SET_NULL : 글이 삭제되면 NULL로 치환(NOT NULL일 경우 옵션 사용 X)
  * SET_DEFAULT : 디폴트 값으로 치환

# Ipython

* shell : `>` 여기서 실행 될 땐, 이전 명령어(방향키 위) 안먹힘

  ```bash
  # 설치
  $ pip install ipython
  
  # 실행
  $ python manage.py shell
  ```

* shell_plus : 웬만한 것 다 import 해줌

  ```bash
  # 설치
  $ pip install django_extensions
  
  # settings.py INSTALLED_APPS에 'django_extensions' 추가
  
  # 실행
  $ python manage.py shell_plus
  ```

# Query 실습

```shell
# 1. '홍길동' 이름 가진 reporter1(object) 생성
In [1]: reporter1 = Reporter()

In [2]: reporter1.name = '홍길동'

In [3]: reporter1.save()

# 2. '철수' 이름 가진 reporter2 생성
In [6]: reporter2 = Reporter.objects.create(name='철수')

# 값 확인
In [7]: reporter1.pk
Out[7]: 1

In [8]: reporter2.pk
Out[8]: 2

# 3. reporter1의 article1추가 (오브젝트 통해서)
# NOTNULL 오류 - N:1 관계 reporter정보를 넣어야함.
In [9]: article = Article()

In [10]: article.title = '1번 글'

In [11]: article.content = '1번 내용'

In [12]: article.save()

# article이 가지고 있는 멤버 변수, 함수 등 조회
In [14]: dir(article)

# 3. reporter1의 article1추가 (오브젝트 통해서)
In [15]: article.reporter = reporter1

In [16]: article.save()

# 4. reporter1의 article3추가 (article_set을 통해서)
In [32]: reporter3 = Reporter()
In [33]: article4.reporter = reporter2
In [35]: article3.save()
In [41]: reporter1.article_set.add(article3)
In [42]: article3.reporter
Out[42]: <Reporter: Reporter object (1)>

# 5. reporter1의 article2추가 (id값을 통해서)
# ValueError: Cannot assign "1": "Article.reporter" must be a "Reporter" instance.
In [18]: article2 = Article.objects.create(title='제목', content='내용', reporter=1)

# 5. reporter1의 article2추가 (id값을 통해서)
# (1) 첫번째방법 article.reporter_id = reporter pk(FK)
In [20]: article2 = Article.objects.create(title='제목', content='내용', reporter_id=1)
# (2) 두번째방법
In [21]: article2 = Article.objects.create(title='제목', content='내용', reporter=reporter1)

# 6. 각 reporter의 article들 조회 (filter?_set?)
In [26]: Article.objects.filter(reporter_id=1)
In [27]: reporter1.article_set.all()
In [28]: article3.reporter
In [29]: article3.reporter_id

# 7. article1에 댓글 두개 추가
In [43]: comment1 = Comment()
In [45]: comment1.save()
In [46]: article1.comment_set.add(comment1)
In [47]: comment1.content = '댓글'
In [48]: comment1.article_id = 1
In [49]: comment1.save()

In [55]: comment2.article = article1
In [50]: comment2 = Comment()
In [51]: comment2.content = '댓글2'
In [56]: comment2.save()

# 8. 마지막 댓글의 기사를 작성한 기자?
In [68]: Comment.objects.all().last().article.reporter
Out[68]: <Reporter: Reporter object (1)>

# 9. 기사별 댓글 내용 출력
In [60]: articles = Article.objects.all()

In [61]: articles
Out[61]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>

In [62]: for article in articles:
    ...:     for comment in article.comment_set.all():
    ...:         print(comment.content)
    ...: 
댓글
댓글2

# 10. 기자별 기사 내용 출력
In [69]: reporters = Reporter.objects.all()
In [75]: for reporter in reporters:
    ...:     print(reporter.name)
    ...:     for article in reporter.article_set.all():
    ...:         print(article.title)
    ...: 
홍길동
1번 글
제목
제목
제목
철수

# 11. reporter1의 기사 갯수
In [76]: reporter1.article_set.count()
Out[76]: 4

In [77]: article1.comment_set.count()
Out[77]: 2
```

* 관계를 통해 값 가져오기

  * 1쪽에서 가지고 오기

  ```shell
  # 1.
  In [26]: Article.objects.filter(reporter_id=1)
  Out[26]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
  
  # 2. 
  In [27]: reporter1.article_set.all()
  Out[27]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
  ```

  * N쪽에서 가지고 오기

  ```shell
  In [28]: article3.reporter
  Out[28]: <Reporter: Reporter object (1)>
  
  In [29]: article3.reporter_id
  Out[29]: 1
  ```

  * comment2의 기사를 쓴 리포터 가져오기

    ```bash
    In [57]: comment2.article
    Out[57]: <Article: Article object (1)>
    
    In [58]: comment2.article.reporter
    Out[58]: <Reporter: Reporter object (1)>
    ```

    