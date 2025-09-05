WITH car_type AS (
    SELECT *
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_TYPE IN ('세단', 'SUV')
),
available_car AS (
    SELECT c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE
    FROM car_type c
    WHERE NOT EXISTS (
        SELECT 1
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        WHERE h.CAR_ID = c.CAR_ID
          AND h.START_DATE <= '2022-11-30'
          AND h.END_DATE >= '2022-11-01'
    )
),
integration AS (
    SELECT a.CAR_ID,
           a.CAR_TYPE,
           a.DAILY_FEE,
           p.DISCOUNT_RATE
    FROM available_car a
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
      ON a.CAR_TYPE = p.CAR_TYPE
     AND p.DURATION_TYPE = '30일 이상'
)
SELECT 
    i.CAR_ID,
    i.CAR_TYPE,
    FLOOR(i.DAILY_FEE * 30 * (1 - i.DISCOUNT_RATE / 100)) AS FEE
FROM integration i
WHERE FLOOR(i.DAILY_FEE * 30 * (1 - i.DISCOUNT_RATE / 100)) BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;
