# Write your MySQL query statement below
SELECT score ,
DENSE_RANK() OVER(ORDER BY score desc) as 'rank'
FROM Scores
ORDER BY score
desc