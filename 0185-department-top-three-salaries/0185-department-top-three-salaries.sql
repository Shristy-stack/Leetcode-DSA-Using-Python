# Write your MySQL query statement below
WITH cs as(SELECT e.id, e.name , salary,departmentId , d.name as Department FROM Employee e JOIN Department d
ON e.departmentId=d.id)
,ps as (SELECT Department,name AS Employee,salary AS Salary,
DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) as ranks
FROM cs)
SELECT Department,Employee, Salary
 FROM ps WHERE ranks<=3