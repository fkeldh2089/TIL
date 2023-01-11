# Spring JPA

1. `build.gradle`에 dependency 추가

   ```java
   dependencies {
       // JPA
       implementation("org.springframework.boot:spring-boot-starter-data-jpa")
   }
   
   ```

   - 추가한 후 gradle refresh 해줄것

2. application.properties 에 정보 입력

   ```
   # MySQL 설정
   spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
   
   # DB Source URL
   spring.datasource.url=jdbc:mysql://127.0.0.1:3306/Schema?useSSL=false&useUnicode=true&serverTimezone=Asia/Seoul
   
   #DB Username
   spring.datasource.username=<username>
   
   #DB Password
   spring.datasource.password=<password>
   
   #true 설정시 JPA 쿼리문 확인 가능
   spring.jpa.show-sql=true
   
   #DDL(Create, Alter, Drop) 정의시 DB의 고유 기능을 사용할 수 있다.
   spring.jpa.hibernate.ddl-auto=update
   
   # JPA의 구현체인 Hibernate가 동작하면서 발생한 SQL의 가독성을 높여준다.
   spring.jpa.properties.hibernate.format_sql=true
   ```

   spring.jpa.hibernate.ddl-auto=[]

   - create : 기존 테이블을 삭제하고 새로 생성 [ Drop + Create ]
   - create-drop : Create 속성에 추가로 어플리케이션을 종료할 때 생성한 DDL을 제거 [ Drop + Create + Drop]
   - update : DB 테이블과 엔티티 매핑 정보를 비교해서 변경 사항만 수정 [ 테이블이 없을 경우 Create ]
   - validate : DB 테이블과 엔티티 매핑정보를 비교해서 차이가 있으면 경고를 남기고 어플리케이션을 실행하지 않음
   - none : 자동 생성 기능을 사용하지 않음

    

3. 유저와 스키마 생성

   ```sql
   create database IF NOT EXISTS `recipestore` collate utf8mb4_general_ci;
   create user 'recipestore'@'%' identified by 'recipestore9801';
   grant all privileges on *.* to recipestore@'%';
   flush privileges;
   ```

   