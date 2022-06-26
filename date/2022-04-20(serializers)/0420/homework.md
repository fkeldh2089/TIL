1.  아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오

- T
- F 이 외에도 'DELETE, PUT' 등 이 있다.
- T





2. 다음의 HTTP status code의 의미를 간략하게 작성하시오

- 200 : OK
- 400 : BAD REQEUST
- 401 : UNAUTHORIZED
- 403 : FORBIDDEN4
- 404 :  NOT FOUND
- 500 : INTERNAL_SERVER_ERROR





3. 아래의 모델을 바탕으로 ,,,

```python
class StudentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = __all__
```





4. Serializer의 의미

쿼리셋이나 모델과 같이 복잡한 데이터를 JSON 등의 유형으로 쉽게 변환가능한 python 데이터 타입으로 변환해 준다.