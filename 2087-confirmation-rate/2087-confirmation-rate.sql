SELECT COALESCE(s.user_id, c.user_id) AS user_id,
       ROUND((SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(*)),2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
GROUP BY COALESCE(s.user_id, c.user_id)

UNION

SELECT COALESCE(s.user_id, c.user_id) AS user_id,
       ROUND((SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END)  / COUNT(*)),2) AS confirmation_rate
FROM Signups AS s
RIGHT JOIN Confirmations AS c ON s.user_id = c.user_id
WHERE s.user_id IS NULL
GROUP BY COALESCE(s.user_id, c.user_id);
