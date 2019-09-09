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