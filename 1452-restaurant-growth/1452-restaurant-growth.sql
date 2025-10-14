# Write your MySQL query statement below
WITH sum_as as
(
    SELECT visited_on , SUM(amount) as amount 
    FROM Customer GROUP BY visited_on
)

SELECT
  visited_on,
  SUM(amount) OVER (
    ORDER BY visited_on
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS amount,
  ROUND(AVG(amount) OVER (
    ORDER BY visited_on
    ROWS BETWEEN 6  PRECEDING AND CURRENT ROW
  ),2) AS average_amount 
FROM sum_as
order by visited_on
LIMIT 18446744073709551615 OFFSET 6
