SELECT DISTINCT l1.num as ConsecutiveNums 
FROM logs as l1 JOIN logs as l2 
ON l1.id=l2.id-1
JOIN logs as l3
ON l2.id=l3.id-1
where l1.num=l2.num and l2.num=l3.num