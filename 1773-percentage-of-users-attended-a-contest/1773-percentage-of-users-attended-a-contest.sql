# Write your MySQL query statement below
With half as(SELECT r.contest_id ,COUNT(u.user_id) as u_id
FROM Users as u  JOIN Register as r
ON u.user_id=r.user_id
GROUP BY  r.contest_id)

SELECT h.contest_id,ROUND(((h.u_id/COUNT(u.user_id))*100),2) as percentage  
FROM Users as u,half as h
GROUP BY h.contest_id
ORDER BY percentage DESC,contest_id ASC