WITH cummulative_sum as 
(
    SELECT person_id ,person_name ,turn ,
    SUM(weight) over (ORDER BY  turn asc) as cumm_weight
    FROM Queue 
)

SELECT person_name  FROM cummulative_sum
WHERE cumm_weight <=1000
ORDER BY turn desc limit 1