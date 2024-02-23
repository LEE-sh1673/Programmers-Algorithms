SELECT 
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS AS D
WHERE 
    D.SKILL_CODE IN (
        SELECT D.SKILL_CODE
        FROM
            SKILLCODES
        WHERE
            (NAME = 'Python' OR NAME = 'C#') AND D.SKILL_CODE & CODE = CODE
    )
ORDER BY ID ASC;
