# Vanilla js API 요청

1. fetch 사용
   - header의 content type 지정에 있어 문제가 발생



2. axios 사용

   - 설치

     `npm i axios -S`

   - cdn

     `<script src="./node_modules/axios/dist/axios.min.js"></script>`

   - 사용

     ```js
         const addRecipe = (recipeData) => {
           axios
             .post("url", recipeData, {
               headers: {
                 "Content-Type": "application/json",
                 "Access-Control-Allow-Origin": "*",
               },
             })
             .then((res) => (btn1.value = "성공!"))
             .catch((res) => (btn1.value = "실패!"));
         };
     ```

     