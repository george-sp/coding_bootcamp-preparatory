# Display the students and all their grades (in all courses)
SELECT bootcamp.students.StID, bootcamp.students.Fname, bootcamp.students.Lname, bootcamp.students_has_courses.grade 
FROM bootcamp.students 
INNER JOIN bootcamp.students_has_courses
ON bootcamp.students.StID = bootcamp.students_has_courses.students_StID;
