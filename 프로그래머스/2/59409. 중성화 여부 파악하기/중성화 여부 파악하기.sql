-- CASE + 정규표현식
SELECT
    ANIMAL_ID,
    NAME,
    CASE WHEN SEX_UPON_INTAKE REGEXP '^(Neutered|Spayed)' THEN 'O'
        ELSE 'X'
    END
        AS '중성화'
FROM
    ANIMAL_INS;


-- CASE + SUBSTRING_INDEX
SELECT
    ANIMAL_ID,
    NAME,
    CASE SUBSTRING_INDEX(SEX_UPON_INTAKE, " ", 1) 
        WHEN 'intact' THEN 'X'
        ELSE 'X'
    END
        AS '중성화'
FROM
    ANIMAL_INS;



-- IF + 정규표현식
SELECT
    ANIMAL_ID,
    NAME,
    IF (SEX_UPON_INTAKE REGEXP '^(Neutered|Spayed)', 'O', 'X')
        AS '중성화'
FROM
    ANIMAL_INS;


-- IF + INSTR(ORACLE)
SELECT
    ANIMAL_ID,
    NAME,
    IF (INSTR(SEX_UPON_INTAKE, 'intact'), 'X', 'O')
        AS '중성화'
FROM
    ANIMAL_INS;