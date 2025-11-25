# Write your MySQL query statement below
WITH step1 as (SELECT requester_id , COUNT(*) as cnt FROM RequestAccepted 
GROUP BY requester_id )
,step2 as (SELECT accepter_id  , COUNT(*) as cnt FROM RequestAccepted 
GROUP BY accepter_id  ), step3 as (
SELECT requester_id as id,cnt FROM step1
UNION ALL
SELECT accepter_id as id,cnt FROM step2   )

SELECT id, SUM(cnt) as num FROM step3 
GROUP BY id
ORDER BY num desc Limit 1