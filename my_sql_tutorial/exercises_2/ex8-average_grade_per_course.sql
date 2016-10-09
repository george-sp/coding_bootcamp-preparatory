# Display the average grade per	course (for all students).
SELECT AVG(bootcamp.students_has_courses.grade) AS AverageGradePerCourse 
FROM bootcamp.students_has_courses
GROUP BY bootcamp.students_has_courses.courses_CID;