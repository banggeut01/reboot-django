# 전생 app

"무연님은 전생에 선생님이었습니다."

1. Model 정의

   1. app 생성 후 등록

      ```bash
      $ python manage.py startapp jobs
      ```

      

1. Form : 이름을 받아서

2. 직업 랜덤 추출

   ```python
   fake.job()
   ```

   

3. 결과를 출력

   1. DB에 등록된 이름이 있으면, 해당하는 결과 출력

   2. 이름이 없으면 새롭게 DB에 추가하고,

      결과 출력

## faker python package

랜덤으로 데이터 만들어주는 함수

* 설치

  ```bash
  $ pip install faker
  ```

* 사용

  ```python
  >>> from faker import Faker
  >>> fake = Faker() # 클래스 인스턴스 생성
  >>> fake.name() # 이름 생성 함수
  'William Foster'
  >>> fake.address()
  '346 Dyer Ridge Suite 107\nAlexview, WA 93863'
  >>> fake.text() 
  'We speech still some magazine your. Defense
  lose structure after billion.\nProfessor strategy drug candidate choice bit room glass. Court forward discover cause stop high speak.'
  >>> fake.text()
  'Senior raise either read single. Provide letter would concern finally success believe positive.\nMention wrong down daughter. Few require share friend. Full anyone represent.'
  >>> fake.email()
  'michelle91@yahoo.com'
  >>> fake.email()
  'inelson@hotmail.com'
  
  ```

* 한국어

  ```python
  >>> fake = Faker('ko_KR')
  >>> fake.name()
  '박은서'
  >>> fake.name()
  '임성수'
  >>> fake.address()
  '경상북도 성남시 석촌호수가'
  >>> fake.job()
  '애완동물 미용사'
  >>> fake.job()
  '강구조물 가공원 및 건립원'
  ```



## key 값 숨기기

* `python-decouple`설치

  ```bash
  $ pip install python-decouple
  ```

* `.env` 파일 만들고 아래 내용 작성

  ```.env
  GIPHY_API_KEY="asdf12314asdf" => api key값
  ```

* key값 가져오기

  ```python
  from decouple import config
  # ...
  api_key = config('GIPHY_API_KEY')
  ```

  

## api 관련 참고링크

[카카오 형태소부 github](https://github.com/kakao/khaiii)

[공공데이터 포털 API](https://www.data.go.kr/search/index.do?index=OPENAPI&query=&currentPage=1&countPerPage=10)

