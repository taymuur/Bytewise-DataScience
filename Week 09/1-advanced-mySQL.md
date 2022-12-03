## Advanced MySQL

### Wild Cards

Grabs data that matches a specific pattern where % = *any number of characters* and _ = *one character*.

```sql
SELECT * FROM client WHERE client_name LIKE '%LLC'  # any character before LLC 

SELECT * FROM client WHERE client_name LIKE '____-10%'  # shows ppl born in october
```

### Union

Combines SELECT statement. We can do multiple unions and should have: same no. of columns and same data type.

```sql
SELECT first_name
FROM employee;
UNION
SELECT branch_name
FROM branch;
#return first name and branch name in a single columm
```

### Joins

Combines rows from two or more tables.
- When using LEFT JOIN all employee from FROM employee gets displyed
- When using RIGHT JOINT it displays all branch table data

```sql
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch   
ON employee.emp_id = branch.mgr_id; 
```

### Natural Join
A join operation that creates an implicit join clause for us based on the common columns in the two tables being joined. Common columns are columns that have the same name in both tables. 

A natural join can be an inner join, a left outer join, or a right outer join. The default is inner join.

```sql
SELECT * 
FROM company.branch,company.client
where branch.branch_id = client.branch_id;
```
