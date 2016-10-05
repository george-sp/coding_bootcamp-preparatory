# Exercise 3
INSERT INTO bootcamp.students (`students id`, `first name`, `last name`, `date of birth`) 
VALUES (1, "George", "Spyridakis", '1991-10-24'),
       (2, "Dimitris", "Theodoropoulos", '1989-9-18');

INSERT INTO bootcamp.students (`students id`, `first name`, `last name`, `date of birth`)
VALUES (4,"sdfas", "asfdq", '1234-12-12');

# Select the unique names of the assistant
SELECT DISTINCT bootcamp.courses.`name of the assisstant` FROM bootcamp.courses;

# Delete
DELETE FROM bootcamp.students WHERE `students id`=4;

SELECT * FROM bootcamp.students;