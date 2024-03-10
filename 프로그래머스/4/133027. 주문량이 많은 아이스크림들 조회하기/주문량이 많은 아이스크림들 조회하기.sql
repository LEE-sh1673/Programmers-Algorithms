-- FIRST_HALF 테이블의 기본 키는 FLAVOR
-- FIRST_HALF 테이블의 SHIPMENT_ID는 JULY 테이블의 SHIPMENT_ID의 외래 키입니다.
-- JULY 테이블의 기본 키는 SHIPMENT_ID
-- JULY 테이블의 FLAVOR는 FIRST_HALF 테이블의 FLAVOR의 외래 키입니다. 
 
-- 서로 다른 두 공장에서 아이스크림 가게로 출하를 진행하는 경우
-- 같은 맛의 아이스크림이라도 다른 출하 번호 (SHIPMENT_ID)를 갖게 됩니다.

-- 7월 아이스크림 총 주문량 + 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서
-- 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

SELECT F.FLAVOR
FROM
   FIRST_HALF AS F JOIN (
       SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
       FROM JULY
       GROUP BY FLAVOR
    ) AS J ON F.FLAVOR = J.FLAVOR
GROUP BY
    F.FLAVOR
ORDER BY
    SUM(F.TOTAL_ORDER) + J.TOTAL_ORDER DESC
LIMIT 3;