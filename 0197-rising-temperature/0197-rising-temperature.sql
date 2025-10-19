SELECT m.id  FROM
Weather as w JOIN Weather as m
ON DATEDIFF(m.recordDate, w.recordDate) = 1
where m.temperature >w.temperature
