-- =====================================
-- Initialize database: students & grades
-- =====================================

-- Create the "students" table
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique student ID
    full_name TEXT NOT NULL,               -- Full name of the student
    birth_year INTEGER                     -- Year of birth
);

-- Create the "grades" table
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique grade ID
    student_id INTEGER,                    -- Reference to student
    subject TEXT,                          -- Name of the subject
    grade INTEGER,                         -- Grade (1 to 100)
    FOREIGN KEY (student_id) REFERENCES students(id)  -- Link to students table
);

-- Insert sample students
INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Insert sample grades
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),

(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),

(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),

(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),

(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),

(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),

(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),

(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),

(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);
