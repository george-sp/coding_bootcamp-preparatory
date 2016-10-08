# Display those students that participated at "SQL" course.
SELECT bootcamp.students.* 
FROM bootcamp.students
INNER JOIN bootcamp.students_has_courses 
ON bootcamp.students.StID = bootcamp.students_has_courses.students_StID 
INNER JOIN bootcamp.courses 
ON bootcamp.students_has_courses.courses_CID = bootcamp.courses.CID 
WHERE bootcamp.courses.Name = "SQL";
