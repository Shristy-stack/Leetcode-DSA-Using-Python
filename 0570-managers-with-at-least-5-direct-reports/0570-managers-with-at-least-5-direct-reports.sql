# Write your MySQL query statement below
SELECT e.name FROM Employee as e
JOIN Employee as m
on e.id=m.managerId
GROUP BY e.id
HAVING COUNT(m.managerId)>=5