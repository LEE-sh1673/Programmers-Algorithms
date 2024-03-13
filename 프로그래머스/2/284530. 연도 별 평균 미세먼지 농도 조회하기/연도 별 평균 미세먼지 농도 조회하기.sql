-- 수원 지역
-- 연도 별 평균 미세먼지 오염도 (PM10)
-- 평균 초미세먼지 오염도 (PM2.5)
-- 셋째 자리에서 반올림
-- 연도를 기준으로 오름차순 정렬

SELECT
    YEAR,
    ROUND(AVG(PM_VAL1), 2) AS 'PM10',
    ROUND(AVG(PM_VAL2), 2) AS 'PM2.5'
FROM (
        SELECT
            YEAR(YM) AS YEAR,
            PM_VAL1,
            PM_VAL2
        FROM AIR_POLLUTION
        WHERE LOCATION1 = '경기도' AND LOCATION2 = '수원' 
    ) AS SUB
GROUP BY YEAR
ORDER BY YEAR ASC;
