import requests
from decouple import config
from django.shortcuts import render, redirect
from .models import User
from faker import Faker

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

'''def search(request):
    name = request.GET.get('name')
    users = User.objects.all()
    for user in users:
        if user.name == name:
            context = {
                'user': user
            }
            return render(request, 'jobs/search.html', context)
    fake = Faker('ko_KR')
    job = fake.job()
    user = User.objects.create(name=name, job=job)
    context = {
        'user': user
    }
    return render(request, 'jobs/search.html', context)
'''

'''
def search(request):
    name = request.GET.get('name')
    # get 쓰면, 빈 리스트일 때 오류!
    user = User.objects.filter(name=name)
    if not user:
        fake = Faker('ko_KR')
        job = fake.job()
        user = User.objects.create(name=name, job=job)
    else:
        user = user[0]
    context = {
        'user': user
    }
    return render(request, 'jobs/search.html', context)
'''

def search(request):
    name = request.GET.get('name')
    # DB에 이름이 있으면,
    user = User.objects.filter(name=name).first()
    # 이름이 없으면,
    if not user:
        # fake = Faker('ko_KR')
        fake = Faker('en')
        job = fake.job()
        user = User.objects.create(name=name, job=job)
    # 직업 결과에 따라, giphy 요청
    job = user.job
    api_key = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}'
    # url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=en'
    # 2. 요청보내기
    response = requests.get(url).json()
    # 3. 응답 결과에서 이미지 url 뽑기
    try:
        image_url = response['data'][0].get('images').get('original').get('url')
    except:
        image_url = None
    context = {
        'user': user,
        'image_url': image_url
    }
    return render(request, 'jobs/search.html', context)