WITH CUMM_SUM AS (
    SELECT person_name,
SUM(Weight) OVER (ORDER BY TURN) AS  Total_Weight_So_Far
FROM Queue
ORDER BY Total_Weight_So_Far DESC
)
SELECT person_name FROM CUMM_SUM
WHERE Total_Weight_So_Far <= 1000
LIMIT 1