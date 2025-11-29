# Write your MySQL query statement below
WITH cs as (SELECT mr.user_id,mr.movie_id,u.name,m.title,mr.rating , mr.created_at  
FROM MovieRating as mr JOIN Movies as m
ON mr.movie_id = m.movie_id
JOIN Users as u        
ON mr.user_id = u.user_id) 
,avg_ratings AS (
    SELECT 
        movie_id,
        title,
        AVG(rating) AS avg_rating
    FROM cs
    WHERE created_at LIKE '2020-02%'
    GROUP BY movie_id, title
),
max_rating AS (
    SELECT MAX(avg_rating) AS max_avg
    FROM avg_ratings
)
(SELECT * FROM (SELECT name as results FROM cs
GROUP BY user_id 
ORDER BY COUNT(user_id) DESC ,name ASC LIMIT 1) AS t1)
UNION ALL
(SELECT * FROM (SELECT title AS results
FROM avg_ratings
WHERE avg_rating = (SELECT max_avg FROM max_rating)
ORDER BY title limit 1 ) AS t2)
