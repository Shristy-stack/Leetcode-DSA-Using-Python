# Write your MySQL query statement below
SELECT m.id FROM 
Weather as w JOIN Weather as m
ON DATE_ADD(w.recordDate, INTERVAL 1 DAY)=m.recordDate
where w.temperature<m.temperature