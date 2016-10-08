# Display the average grade of each student (in all courses)
SELECT bootcamp.students.StID, bootcamp.students.Fname, bootcamp.students.Lname, 
AVG(bootcamp.students_has_courses.grade) AS AverageGrade 
FROM bootcamp.students
INNER JOIN bootcamp.students_has_courses
ON bootcamp.students.StID = bootcamp.students_has_courses.students_StID
GROUP BY bootcamp.students.StID;