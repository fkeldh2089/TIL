# SQL

#### 데이터 베이스 생성

1. shell 켜기

```
sqlite3 tutorial.sqlite3  # 
```

2. 생성

```
sqlite> .database
```

3. 

```
sqlite> .mode csv
sqlite> .import hellodb.csv examples
```

4. 테이블

```
DROP TABLE classmates;

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);
```



#### CRUD

1. 조회

```
sqlite> SELECT * FROM examples;  # *은 전체를 의미

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT rowid, name FROM classmates WHERE address = '서울';

SELECT DISTINCT age FROM classmates;
```

2. 생성

```
INSERT INTO classmates (name, age, address) 
VALUES ('홍길동', 30, '서울');

CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates 
VALUES 
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '광주'),
('박삼성', 29, '구미'),
```

3.  업데이트

```
UPDATE classmates 
SET name='홍길동', address='제주도'
WHERE rowid=5;

SELECT rowid, * FROM classmates;

```



4. 삭제

```
DELETE FROM classmates WHERE rowid=5;

INSERT INTO classmates VALUES ('최전자', 28, '부산');

SELECT rowid, * FROM classmates;

```

