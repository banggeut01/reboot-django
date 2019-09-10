# 장고를 시작하면서...

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