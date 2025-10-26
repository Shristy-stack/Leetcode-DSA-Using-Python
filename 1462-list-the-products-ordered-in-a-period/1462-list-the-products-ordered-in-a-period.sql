# Write your MySQL query statement below
SELECT product_name, SUM(unit) as unit
FROM Products as p JOIN Orders as o
ON p.product_id=o.product_id
WHERE order_date LIKE ('2020-02%')
GROUP BY p.product_id,product_name
HAVING SUM(unit) >=100 