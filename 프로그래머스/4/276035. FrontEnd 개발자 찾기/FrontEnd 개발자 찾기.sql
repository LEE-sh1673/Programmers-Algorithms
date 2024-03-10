# 16 ->              1 0000
# 2048 ->    1000 0000 0000
# 8192 -> 10 0000 0000 0000 
# ----------------------------
#         10 1000 0001 0000

SELECT
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM
    DEVELOPERS
WHERE
    SKILL_CODE & (
        SELECT SUM(CODE)
        FROM SKILLCODES
        WHERE CATEGORY = 'Front End'
    )
ORDER BY
    ID ASC;
