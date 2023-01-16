의문점

1. class interface 등의 차이점
   - 예상 : 큰 차이는 없더라도 구분용?
   - https://velog.io/@hsw0194/Spring-Boot%EC%97%90%EC%84%9C-interface%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C
2. public private의 차이점
   - 예상 : 전역이냐, 아니냐의 차이가 아닐까?
   - 접근 제한자로 public, protected, private 3가지로 구분
   - public은 외부 클래스가 자유롭게 사용됨
   - protected는 같은 패키지 또는 자식 클래스에서 사용 가능
   - private는 외부에서 사용할 수 없음
3. @Getter, @Setter의 의미?
   - @Getter 메소드는 인스턴스나 클래스의 변수 값을 갖오는 메소드
     - ex> getbyuserId()이런 것들
   - @Setter는 적용시키는 메소드
4. Service내부에서 @Service, @AllArgsConstructor의 의미 + private final
   - @Service는 anootation
   -  `@NoArgsConstructor` 어노테이션은 파라미터가 없는 기본 생성자를 생성해주고, `@AllArgsConstructor` 어노테이션은 모든 필드 값을 파라미터로 받는 생성자를. `@RequiredArgsConstructor` 어노테이션은 `final`이나 `@NonNull`인 필드 값만 파라미터로 받는 생성자
   
   - static은 상수로 선언
   - private final로 선언한다면, 직접 값을 참조할 수 없지만 생성자를 통해 값 참조가 가능