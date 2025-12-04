-- 1. Find all grades for a specific student (Alice Johnson)
SELECT s.full_name, g.subject, g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';


-- 2. Calculate the average grade per student
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id;


-- 3. List all students born after 2004
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;


-- 4. List all subjects and their average grades
SELECT subject, AVG(grade) AS avg_grade
FROM grades
GROUP BY subject;


-- 5. Find the top 3 students with the highest average grades
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 3;


-- 6. Show all students who have scored below 80 in any subject
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON g.student_id = s.id
WHERE g.grade < 80;
