SELECT 
    #t.client_id,t.driver_id,u.role,m.role,t.status, t.request_at, u.banned as clientbanned,m.banned as driverbanned
    t.request_at as 'Day',
    ROUND(SUM(CASE WHEN status ='cancelled_by_driver' OR status ='cancelled_by_client' THEN 1 ELSE 0 END)/COUNT(*),2) AS 'Cancellation Rate'
FROM 
    Trips AS t
JOIN 
    Users AS u ON t.client_id = u.users_id
JOIN 
    Users AS m ON t.driver_id = m.users_id
WHERE u.banned='No' and m.banned='No'
GROUP BY t.request_at
HAVING t.request_at >='2013-10-01' AND t.request_at <='2013-10-03' 
