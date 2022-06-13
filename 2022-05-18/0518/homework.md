1. 

from : 현재 url 정보가 다긴 라우터 객체

to : 이동할 url정보가 담긴 라우터 객체, 대상 라우터 객체로 이동

next : to 에서 지정한 url로 이동하기 위해 호출돼야하는 함수, next에 제공된 전달인자에 따라 행동이 달라진다.

- `next(false)` : 현재 네비게이션을 중단, 브라우저 url이 변경되면 from 경로의 url로 재설정 됩니다.
- `next('/')` or `next({path:})`  다른 위치로 리다이렉션, 현재 네비게이션이 중단되고 새 네비게이션이 시작
- `next(error)`: next에 전달된 인자가 error 인스턴스이면 탐색이 중단되고, `router.onError()`를 이용해 등록된 콜백에 에러가 전달
- 항상 next함수를 호출해야 한다.



2. 

{Authorization : `Token 1234`}