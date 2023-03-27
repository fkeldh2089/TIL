# RESTful API

### REST 란

- REST: Representational State Transfer의 약자

  - 자원을 이름으로 구분하여 해당 자원의 상태를 주고 받는 모든 것

    ex) 학생의 정보가 자원일 때, `student`로 자원을 표현

  - 월드 와이드 웹과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 형식

    - HTTP를 사용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처
    - Client Server 간 통식 방식

### 세부 내용

- HTTP URI(Uniform Resource Identifier)를 통해 자원 (Resource)를 명시하고, Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD 를 적용한다.
  - 자원 기반의 구조(Resource Oriented Architecture)
  - HTTP Method에 의한 자원 처리 설계



### 장점

1. HTTP의 인프라를 사요하므로 REST API 사용을 위한 별도의 인프라 구축이 필요 없다
2. 1에 의거하여 HTTP를 따르는 모든 플랫폼에서 장점을 갖는다.
3. Hypermedia API의 기본을 지키며 범용성이 있다.
4. 메시지가 의도하는 바를 쉽게 파악할 수 있다.
5. 서버와 클라이언트의 역할을 명확히 분리한다.



### 단점

1. 표준이 존재 하지 않는다.
2. Method가 4가지 밖에 없다.



### 필요 이유

1. 앱의 분리 및 통합
2. 다양한 클라이언트의 등장
   - 최근 서버는 다양한 브라우저 및 디바이스에도 차이가 있다.



### 구성 요소

1. 자원(Resource) : URI
   - 모든 자원에 고유한 ID가 존재
   - Client는 URI를 통해 자원을 지정 => Server에 요청
2. 행위(Verb) : HTTP Method
   - HTTP Method를 사용
   - GET(R), POST(C), PUT(U, Patch), DELETE(D)
3. 표현(Representation of Resource)
   - Client가 자원의 상태에 대한 조작을 요청 => 서버는 응답(Representation)
   - JSON, XML, TEXT, RSS등의 여러 형태가 존재



### 특징

1. Server-Client 구조
   - 서버는 API를 제공, 자원의 관리 저장
   - 클라이언트는 사용자의 인증등을 관리
2. Stateless(무상태)
   - HTTP 는 Stateless Protocol이므로 REST는 무상태성
   - 클라이언트의 context를 서버에 저장하지 않음 => 구현의 단순화
   - 서버는 각각의 요청을 완전히 별개의 것으로 인식하고 처리 => 서비스의 자유도 상승
3. Cacheable(캐시)
   - HTTP를 사용하므로 웹의 인프라를 그대로 활용 가능
     - 캐싱 가능
   - 대량의 요청을 효율적으로 처리하기 위해 캐싱
   - 서버 트랜잭션 방지 및 서버 자원 이용률 향상
4. Layered System(계층화)
   - 클라이언트는 서버만 호출
   - 서버는 다중 계층으로 구성 가능
     - 순수 로직, 보안, 로드 밸런싱, 암호화, 사용자 인증 등등
   - 프록시, 게이트웨이 같은 네트워크 기반 매체 사용 가능
5. Code On Demand(Op)
   - 서버로부터 스크립트를 받아 서버에서 실행 -> SSL
6. Uniform Interface(인터페이스 일관성)
   - URI로 지정한 자원에 조작을 통일되고 일관된 인터페이스로 수행
   - HTTP 에 따르는 모든 플랫폼에 사용 가능



