SELECT
    CASE 
        WHEN SUM(CASE WHEN category = 'Front End' THEN 1 ELSE 0 END) > 0 
            AND SUM(CASE WHEN name = 'Python' THEN 1 ELSE 0 END) > 0 THEN 'A'
        WHEN SUM(CASE WHEN name = 'C#' THEN 1 ELSE 0 END) > 0 THEN 'B'
        WHEN SUM(CASE WHEN category = 'Front End' THEN 1 ELSE 0 END) > 0 THEN 'C'
        ELSE 'NONE'
    END AS grade,
    id,
    email
FROM
    DEVELOPERS AS D 
    JOIN (
        SELECT name, code, category
        FROM SKILLCODES
        WHERE category = "Front End" OR name IN ('C#', 'Python')
    ) AS S 
    ON D.skill_code & S.code > 0
GROUP BY
    id, email
HAVING
    grade != 'NONE'
ORDER BY
    grade, id;