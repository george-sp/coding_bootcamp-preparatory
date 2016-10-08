# Display the first and last name of those students that have average grade more than 5.
SELECT bootcamp.students.Fname, bootcamp.students.Lname 
FROM bootcamp.students 
INNER JOIN (
 SELECT bootcamp.students_has_courses.students_StID, AVG(bootcamp.students_has_courses.grade) 
 AS AverageGrade 
 FROM bootcamp.students_has_courses 
 GROUP BY bootcamp.students_has_courses.students_StID 
 HAVING AverageGrade > 5) grades_average
ON bootcamp.students.StID = grades_average.students_StID;

