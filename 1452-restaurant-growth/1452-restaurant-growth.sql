# Write your MySQL query statement below
WITH sum_as as
(
    SELECT visited_on , SUM(amount) as amount 
    FROM Customer GROUP BY visited_on
),
sump as
(SELECT
  visited_on,
  SUM(amount) OVER (
    ORDER BY visited_on
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS amount,
  ROUND(AVG(amount) OVER (
    ORDER BY visited_on
    ROWS BETWEEN 6  PRECEDING AND CURRENT ROW
  ),2) AS average_amount 
  , ROW_NUMBER() OVER (ORDER BY visited_on ASC) AS rn
FROM sum_as)

SELECT visited_on,amount,average_amount FROM sump
WHERE rn>=7