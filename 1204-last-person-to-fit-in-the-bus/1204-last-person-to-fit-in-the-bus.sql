WITH cas as 
(
    SELECT person_name , weight,
    SUM(weight) OVER (ORDER BY turn) as cum_sum
    FROM Queue

)
SELECT person_name FROM cas 
WHERE cum_sum <= 1000 
ORDER BY  cum_sum DESC LIMIT 1