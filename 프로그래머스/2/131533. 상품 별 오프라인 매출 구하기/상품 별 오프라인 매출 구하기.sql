-- 코드를 입력하세요
SELECT PRODUCT_CODE , SUM(PRICE*SALES_AMOUNT) AS SALES
FROM PRODUCT AS P 
INNER JOIN OFFLINE_SALE AS OS
ON P.PRODUCT_ID = OS.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE
;