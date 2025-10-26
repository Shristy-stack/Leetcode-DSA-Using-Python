# Write your MySQL query statement below
With counts as (SELECT class,count(student) as count_no
FROM Courses GROUP BY class
)

SELECT class
FROM counts where count_no>=5;