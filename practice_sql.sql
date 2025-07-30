-- Check tables
SELECT * FROM employees;
SELECT * FROM departments;

-- 1. INNER JOIN example
SELECT emp_name, dept_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;

-- Add more queries below as you learn