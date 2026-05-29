select * FROM orders;

select * FROM customers;

CREATE TABLE employees(
id INTEGER PRIMARY KEY,
name TEXT,
salary INTEGER
);

SELECT * FROM employees;

SELECT * FROM users;
INSERT INTO employees (id, name, salary)
VALUES (
    10,
    'rose',
    60000
  );

  INSERT INTO orders (order_id, user_id, product)
  VALUES (
      202,
      1234,
      'Water heater'
    );