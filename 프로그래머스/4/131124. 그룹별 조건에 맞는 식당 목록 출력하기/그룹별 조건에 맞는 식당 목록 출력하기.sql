SELECT
    MEMBER_NAME,
    R.REVIEW_TEXT AS REVIEW_TEXT,
    DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM
    MEMBER_PROFILE AS M JOIN REST_REVIEW AS R ON M.MEMBER_ID = R.MEMBER_ID
WHERE
    M.MEMBER_ID IN (
        SELECT MEMBER_ID
        FROM (
            SELECT MEMBER_ID, DENSE_RANK() OVER(ORDER BY COUNT(*) DESC) AS RNK
            FROM REST_REVIEW
            GROUP BY MEMBER_ID
        ) AS SUB
        WHERE RNK = 1
    )
ORDER BY
    REVIEW_DATE ASC, REVIEW_TEXT ASC;