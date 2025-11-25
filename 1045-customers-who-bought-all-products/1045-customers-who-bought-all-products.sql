SELECT customer_id   FROM Customer
group by customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)