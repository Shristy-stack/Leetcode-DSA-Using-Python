With js as (SELECT m.movie_id ,m.title , u.user_id, u.name , mr.rating, mr.created_at 
FROM MovieRating mr  JOIN Movies m
ON m.movie_id=mr.movie_id 
JOIN Users u
ON u.user_id=mr.user_id )    

  (SELECT name AS results FROM js 
GROUP BY user_id
ORDER BY count(*) desc, name asc LIMIT 1 )
UNION ALL 
(
    SELECT title AS results FROM js 
    WHERE created_at >='2020-02-01' AND created_at <='2020-02-29'
    GROUP BY movie_id
    ORDER BY AVG(rating) DESC, title asc LIMIT 1

)

