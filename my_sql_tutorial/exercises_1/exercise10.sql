SELECT 	`name of the lecturer`, SUM(`duration of the course`)
AS `total days per lecturer`
FROM bootcamp.courses
GROUP BY `name of the lecturer`