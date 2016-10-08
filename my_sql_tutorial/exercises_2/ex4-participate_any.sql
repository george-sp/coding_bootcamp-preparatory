# Display those students that have participated in an (any) course.
SELECT DISTINCT `bootcamp`.`students`.* FROM `bootcamp`.`students` 
INNER JOIN `bootcamp`.`students_has_courses` 
ON `bootcamp`.`students`.StID = `bootcamp`.`students_has_courses`.`students_StID`