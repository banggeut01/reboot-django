from django.db import models

# Create your models here.
# Reporter(1) - Article(N)
# reporter - name

class Reporter(models.Model):
    name = models.CharField(max_length=30)

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # on_delete
    # 1. CASCADE : 글이 삭제되었을 때 모든 댓글을 삭제
    # 2. PROTECT : 댓글이 존재하면 글 삭제 안됨
    # 3. SET_NULL : 글이 삭제되면 NULL로 치환(NOT NULL일 경우 옵션 사용 X)
    # 4. SET_DEFAULT : 디폴트 값으로 치환

# models.py : python 클래스 정의
#           : 모델 설계도
# makemigrations : migration 파일 생성 => migrations/0001_*.py
#                : DB 설계도 작성
# migrate : migration 파일 DB 반영

# Article(1) - Comment(N)
# comment - content