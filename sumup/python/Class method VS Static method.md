# Class method VS Static method

### Class Method

- 목적 : 클래스 조작
- 함수 내부에 클래스를 받도록 설계

```python
    @classmethod
    def class_method(cls):
        print(cls.var)
        return cls
```



### Static Method

- 클래스나 인스턴스를 조작할 생각은 없고, 함수만 이용

```python
    @staticmethod
    def static_method():
        return ''
```

