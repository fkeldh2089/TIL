```sqlite
CREATE TABLE countries (
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL,
  price INT NOT NULL
);

INSERT INTO countries VALUES 
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'delux', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);

ALTER TABLE countries RENAME TO hotels;

SELECT room_num, price FROM hotels ORDER BY price DESC
LIMIT 2;

SELECT grade, COUNT(*) FROM hotels GROUP BY grade;

SELECT * FROM hotels WHERE room_num LIKE 'B%';

SELECT * FROM hotels WHERE check_in='2020-01-04'
AND room_num NOT LIKE 'B%' ORDER BY price DESC;
```

