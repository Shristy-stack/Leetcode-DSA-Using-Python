# Write your MySQL query statement below
With parta as (SELECT name AS results FROM MovieRating as p JOIN
Movies as m
 ON m.movie_id = p.movie_id
 JOIN Users as u
 on u.user_id = p.user_id
 GROUP BY u.user_id 
 ORDER BY COUNT(*) DESC , name LIMIT 1
 ), partb as 
 (SELECT title AS results FROM Movies as m JOIN MovieRating as p
 ON m.movie_id = p.movie_id
 WHERE created_at LIKE '2020-02%'
 GROUP BY m.movie_id 
 ORDER BY AVG(rating) desc,title LIMIT 1)
 SELECT results from parta
 UNION ALL
 SELECT results FROM partb