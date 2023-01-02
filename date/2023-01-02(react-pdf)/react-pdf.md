# react-pdf

1. 설치

   `npm install react-pdf`

2. 예제는 다음과 같다.

   ```js
   import React, { useState } from 'react';
   import { Document, Page } from 'react-pdf';
   
   function MyApp() {
     const [numPages, setNumPages] = useState(null);
     const [pageNumber, setPageNumber] = useState(1);
   
     function onDocumentLoadSuccess({ numPages }) {
       setNumPages(numPages);
     }
   
     return (
       <div>
         <Document file="somefile.pdf" onLoadSuccess={onDocumentLoadSuccess}>
           <Page pageNumber={pageNumber} />
         </Document>
         <p>
           Page {pageNumber} of {numPages}
         </p>
       </div>
     );
   }
   ```

3. 오류 발생

   ```js
   import React, { useState } from "react"
   import { Document, Page, pdfjs } from "react-pdf"
   
   // Link
   import { Link } from "react-router-dom"
   
   function Repdf() {
     const [numPages, setNumPages] = useState(null)
     const [pageNumber, setPageNumber] = useState(1)
   
     function onDocumentLoadSuccess({ numPages }) {
       setNumPages(numPages)
     }
     pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`
     return (
       <div>
         <Link to="/">뒤로</Link>
         <Document file="../assets/cat.pdf" onLoadSuccess={onDocumentLoadSuccess}>
           <Page pageNumber={pageNumber} />
         </Document>
         <p>
           Page {pageNumber} of {numPages}
         </p>
       </div>
     )
   }
   export default Repdf
   ```

   위와 같이 pdfjs 추가, 참조하는 위치를 변경하는 듯

4. 이후 다음과 같은 오류 발생

   ```
   Warning: getHexString - ignoring invalid character: 33
   util.js:425 Warning: getHexString - ignoring invalid character: 79
   util.js:425 Warning: getHexString - ignoring invalid character: 84
   util.js:425 Warning: getHexString - ignoring invalid character: 89
   util.js:425 Warning: getHexString - ignoring invalid character: 80
   util.js:425 Warning: getHexString - ignoring additional invalid characters.
   util.js:425 Warning: getHexString - ignoring invalid character: 104
   ```

   pdf를 불러올 때, 문제가 발생하는 듯

5. 