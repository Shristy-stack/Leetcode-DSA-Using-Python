SELECT activity_date as day ,Count(DISTINCT user_id) AS active_users FROM Activity
WHERE activity_date<='2019-07-27' AND  activity_date>='2019-06-28'
GROUP BY activity_date