# 해설: https://school.programmers.co.kr/questions/37996
#
# 이 문제에서 GROUP BY를 FOOD_TYPE을 기준으로 수행하였기 때문에
# 출력해야 하는 다른 REST_ID나 NAME이 MAX(FAVORITES)을 가진 튜플의 속성값일 것이라 확신할 수 없다.
# (특정 한 속성을 기준으로 그룹화를 진행하면 해당 속성만을 기준으로 하기 때문에 그 외의 묶이는 헹들의 순서는 # # 보장되지 않는다.)
#
# 따라서 서브 쿼리를 통해 각 음식 종류 별 즐겨찾기 수가 큰 값에 대한 집합을 얻어와
# WHERE 절에서 해당 집합의 최대값과 일치하는 값을 가진 튜플을 찾아내야 한다.

SELECT
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM
    REST_INFO
WHERE
    FAVORITES IN (
        SELECT MAX(FAVORITES)
        FROM REST_INFO
        GROUP BY FOOD_TYPE
    )
GROUP BY
    FOOD_TYPE
ORDER BY
    FOOD_TYPE DESC;

# SELECT
#     FOOD_TYPE,
#     FAVORITES
# FROM
#     REST_INFO
# GROUP BY
#     FOOD_TYPE
# ORDER BY
#     FOOD_TYPE ASC;