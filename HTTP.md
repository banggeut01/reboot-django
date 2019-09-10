FTP, SMTP

## HTTP

* HTTP 기본 속성
  1. Stateless
     * 상태 정보가 저장되지 않음
     * C/S간 상호작용 위해 HTTP 쿠키 만듬
  2. Connectless
* URL(파일 식별자, Uniform Resource Locator)
  * 네트워크상 파일이 어디에 있는지
* URI(통합 자원 식별자, Uniform Resource Identifier)
  * URI = URN + URL

* HTTP URI 구문
  * ex) http://localhost:3000/posts/3
    * `http` : Scheme / Protocol
    * `localhost` : Host
    * `3000` : Port, 기본적으로 http - 80, https - 443
    * `Posts/3` : Path
  * ex) http://google.com/search?q=http
    * `q=http` : Query
  * ex) https://github.com/djpy02-01/django-crud#1-create
    * `#` : fragment, 파일 내에 위치



## HTTP URL

### HTTP 요청 URL on Django

* def index(request):

### HTTP 요청 메시지

* GET / HTTP/1.1

  * Method, 경로, version of the protocol, Header

* 개발자도구 > Network > Headers 

  * 어떤 브라우저로 접속했는지 등을 알 수 있음

* Django의 request.META

* GET / 1.1 200 OK

  * `200` : 상태코드

  * HTTP는 연결되어 있지 않고, 요청을 하면 던져주고 끝인데

    제대로 응답한 건지 알 수 없음

    상태코드로 응답이 제대로 된지 확인할 수 있다.

  * 200 OK : 200대는 모두 다 OK

  * 300 Redirection : Redirect된 것. 

    * 서버가 클라이언트를 다른 주소로 보냄

  * 400 대 error는 사용자 잘못

    * 400 Bad Request : 서버가 요청을 받지 못함 
    * 401 Unauthorized : 로그인되지 않음(비인증)
    * 403 : 접근 권리가 없음
    * 404 Page not found : url 요청 잘못 보냈을 때

  * 500 Internal Server Error : 서버측 잘못

### HTTP Method

* GET : DB에 등록 수정이 아니라 값을 꺼내와 결과를 던질 때
* POST :  클라이언트 데이터 서버로 보낼 때
* PUT/PATCH : HTML에서 공식적으로 지원되지 않음. API에서 많이 쓰임
* DELETE 

###  RESTful(Transfer한 State를 )

* REST API ? 

  * 카카오의 REST API
  * 구성
    * URL
    * HTTP Method
    * 표현
  * 규칙
    * **URL 필요한 정보만**
    * **URL은 자원을 표현하는데 중점을 둬야함**
    * GET 가져오다 POST 보내다

* Restful in Django

  ```bash
  $ python manage.py show_urls
  ```

* HTML에서 공식적인 지원은 GET/POST 두가지로 수행해야 한다.



* ipython 설치 후 진행해보기
  * `embed()`

```bash
In [1]: request
Out[1]: <WSGIRequest: GET '/articles/'>

In [2]: request.method
Out[2]: 'GET'

In [3]: request.path
Out[3]: '/articles/'

In [4]: request.body
Out[4]: b''

In [5]: request.content_type
Out[5]: 'text/plain'
```

```bash
In [1]: request
Out[1]: <WSGIRequest: POST '/articles/create/'>

In [2]: request.method
Out[2]: 'POST'

In [3]: request.body
Out[3]: b'csrfmiddlewaretoken=wU6g41ZinnVGWvGvlekEau35htbS2D3F6jisOe2jVmVJnldQu2BH0A4ZCYENCJ3F&title=%EB%82%98%EB%8A%94+%EC%A0%9C%EB%AA%A9&content=aa'

In [4]: request.POST
Out[4]: <QueryDict: {'csrfmiddlewaretoken': ['wU6g41ZinnVGWvGvlekEau35htbS2D3F6jisOe2jVmVJnldQu2BH0A4ZCYENCJ3F'], 'title': ['나는 제목'], 'content': ['aa']}>

In [5]: request.content_type
Out[5]: 'application/x-www-form-urlencoded'
```

