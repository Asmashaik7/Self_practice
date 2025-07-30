-- Drop tables if they already exist (optional, prevents errors)
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- Create Departments table
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
);

-- Insert sample data into Departments
INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance'),
(4, 'Sales');

-- Create Employees table
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    dept_id INTEGER,
    salary INTEGER,
    location TEXT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert sample data into Employees
INSERT INTO employees (emp_id, emp_name, dept_id, salary, location) VALUES
(101, 'Asha', 1, 60000, 'Chennai'),
(102, 'Ravi', 2, 80000, 'Delhi'),
(103, 'Zoya', 2, 50000, 'Mumbai'),
(104, 'John', NULL, 70000, 'Hyderabad'),
(105, 'Priya', 3, 90000, 'Chennai'),
(106, 'Karan', 4, 75000, 'Bangalore');
