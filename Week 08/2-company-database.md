### Table Creation: Employee

```sql

CREATE TABLE Employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT
);

```

### Table Creation: Branch

```sql
CREATE TABLE Branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

```

### Table Alteration
```sql
ALTER TABLE Employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE Employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

```

### Table Creation: Client

```sql
CREATE TABLE Client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  branch_id INT,
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);
```


### Table Creation: WoksWith

```sql
CREATE TABLE WorksWith (
  emp_id INT,
  client_id INT,
  total_sales INT,
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);
```

### Table Creation: BranchSupplier

```sql
CREATE TABLE BranchSupplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);
```

### Insert Values

```sql
INSERT INTO Employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

INSERT INTO Branch VALUES(1, 'Corporate', 100, '2006-02-09');

UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO Employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);

-- Scranton
INSERT INTO Employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);

INSERT INTO Branch VALUES(2, 'Scranton', 102, '1992-04-06');

UPDATE Employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO Employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO Employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO Employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
INSERT INTO Employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

INSERT INTO Branch VALUES(3, 'Stamford', 106, '1998-02-13');

UPDATE Employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO Employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO Employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);


-- BRANCH SUPPLIER
INSERT INTO BranchSupplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO BranchSupplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO BranchSupplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO BranchSupplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO BranchSupplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO BranchSupplier VALUES(3, 'Stamford Lables', 'Custom Forms');
INSERT INTO BranchSupplier VALUES(3, 'Hammer Mill', 'Paper');

-- CLIENT
INSERT INTO Client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO Client VALUES(401, 'Lackawana Country', 2);
INSERT INTO Client VALUES(402, 'FedEx', 3);
INSERT INTO Client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO Client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO Client VALUES(405, 'Times Newspaper', 3);
INSERT INTO Client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO WorksWith VALUES(105, 400, 55000);
INSERT INTO WorksWith VALUES(102, 401, 267000);
INSERT INTO WorksWith VALUES(108, 402, 22500);
INSERT INTO WorksWith VALUES(107, 403, 5000);
INSERT INTO WorksWith VALUES(108, 403, 12000);
INSERT INTO WorksWith VALUES(105, 404, 33000);
INSERT INTO WorksWith VALUES(107, 405, 26000);
INSERT INTO WorksWith VALUES(102, 406, 15000);
INSERT INTO WorksWith VALUES(105, 406, 130000);
```

### Querying Tables

```sql
SELECT * FROM Employee; # selects all employess
SELECT * FROM Client; # selects all clients

SELECT * FROM Employee
ORDER BY salary; # sort by salary in ascending order

SELECT * FROM Employee
ORDER BY sex, first_name , last_name ; # sort by sex and then name

SELECT * FROM Employee
LIMIT 5 ; # selects first five employees

SELECT first_name, last_name 
FROM Employee # only first and last name

SELECT first_name AS F, last_name AS L
FROM Employee # only first and last name but with column heading F and L

SELECT DISTINCT sex
FROM Employee # selects only F, M as output
```
