-- CAR_RENTAL_COMPANY: 대여 중인 자동차들 정보
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY: 자동차 대여 기록
-- CAR_RENTAL_COMPANY_DISCOUNT_PLAN: (자동차 종류, 대여 기간) 별 할인 정책 정보
--  대여 기간 종류는 '7일 이상', '30일 이상', '90일 이상'
--  대여 기간이 7일 미만인 경우 할인정책 X

-- 조건:
-- 1. 자동차 종류 '세단' 또는 'SUV'
-- 2. 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
-- 3. 30일간의 대여 금액이 50만원 이상 200만원 미만

-- 출력
-- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 출력
-- 대여 금액-내림차순 정렬, 자동차 종류-오름차순 정렬, 자동차 ID-내림차순 정렬


SELECT CP.CAR_ID, CP.CAR_TYPE, TRUNCATE(FEE, 0) AS FEE
FROM (
    SELECT
        C.CAR_ID,
        C.CAR_TYPE,
        C.DAILY_FEE * 30 * (1 - P.DISCOUNT_RATE/100) AS FEE
    FROM 
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P JOIN (
            SELECT CAR_ID, CAR_TYPE, DAILY_FEE
            FROM CAR_RENTAL_COMPANY_CAR
            WHERE CAR_TYPE = '세단' OR CAR_TYPE = 'SUV' 
    ) AS C ON P.CAR_TYPE = C.CAR_TYPE
    WHERE DURATION_TYPE = '30일 이상'
) AS CP
WHERE
    FEE >= 500000 AND FEE < 2000000 AND CP.CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            (START_DATE LIKE '2022-11-%' OR END_DATE LIKE '2022-11-%')
            OR
            (START_DATE <= '2022-11-01' AND END_DATE >= '2022-11-30')
        )
ORDER BY
    FEE DESC, CAR_TYPE ASC, CAR_ID DESC;
    
    

# SELECT
#     A.CAR_ID, A.CAR_TYPE, 
#     TRUNCATE(DAILY_FEE * 30 * (1 - DISCOUNT_RATE/100), 0) AS FEE
# FROM
#     CAR_RENTAL_COMPANY_CAR A 
#     LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C
#     ON A.CAR_TYPE = C.CAR_TYPE AND DURATION_TYPE = '30일 이상'
# WHERE
#     A.CAR_TYPE IN ('세단', 'SUV') AND
#     DAILY_FEE * 30 * (1 - DISCOUNT_RATE/100) >= 500000 AND
#     DAILY_FEE * 30 * (1 - DISCOUNT_RATE/100) < 2000000 AND
#     A.CAR_ID NOT IN
#     (SELECT 
#         CAR_ID 
#     FROM
#         CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE
#         (START_DATE LIKE '2022-11-%' OR END_DATE LIKE '2022-11-%')
#         OR
#         (START_DATE <= '2022-11-01' AND END_DATE >= '2022-11-30'))
# ORDER BY 
#     FEE DESC, CAR_TYPE ASC, CAR_ID DESC
