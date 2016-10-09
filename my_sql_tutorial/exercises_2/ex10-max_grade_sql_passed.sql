# Display the max grade (of all courses), the First and the Last name,
# for each student that have a grade more than 5 at "SQL" course.
SELECT max_grade.maximumGrade, max_grade.FName, max_grade.LName, max_grade.StID
FROM (
	  SELECT MAX(students_has_courses.grade) As maximumGrade, StID, students.FName, students.LName, students_has_courses.courses_CID 
      FROM students 
      INNER JOIN students_has_courses 
      ON students.StID = students_has_courses.students_StID
      GROUP BY StID
      ) max_grade
INNER JOIN (
			SELECT students.StID, students.FName, students.LName, courses.CID
			FROM bootcamp.students
			INNER JOIN bootcamp.students_has_courses 
			ON bootcamp.students.StID = bootcamp.students_has_courses.students_StID 
			INNER JOIN bootcamp.courses 
			ON bootcamp.students_has_courses.courses_CID = bootcamp.courses.CID 
			WHERE bootcamp.courses.Name = "SQL" AND bootcamp.students_has_courses.grade > 5) sql_passed
ON max_grade.StID = sql_passed.StID;