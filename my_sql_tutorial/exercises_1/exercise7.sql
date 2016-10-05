# Exercise 7
SELECT * FROM bootcamp.students WHERE YEAR(NOW()) - YEAR(`date of birth`) > 17;