WITH CUMM_SUMS AS 
(
    SELECT turn,person_name, 
    SUM(Weight) OVER (ORDER BY turn) as cumm_sum
    from Queue
)
SELECT person_name FROM CUMM_SUMS
WHERE cumm_sum <= 1000
ORDER BY cumm_sum DESC LIMIT 1