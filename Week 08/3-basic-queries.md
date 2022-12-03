## Basic Queries

### Count Number of Employees

```sql
SELECT COUNT(emp_id)
FROM employee;     
```

### Count Number of Female Employess Born After 1970

```sql
SELECT COUNT(emp_id)
FROM employee  
WHERE sex='F' AND birth_date > '1971-01-01' ;
```

### Calculate Average of Salary

```sql
SELECT AVG(salary)
FROM employee   
```

### Find Average Salarry of Male Employees 

```sql
SELECT COUNT(emp_id)
FROM employee  
WHERE sex='M';  
```

# Find Total Salary Paid to Employees

```sql
SELECT SUM(salary)
FROM employee    
```

# Find Number of Females and Males by Aggregation

```sql
SELECT COUNT(sex), sex
FROM employee  
GROUP BY sex;  
```

### Finds Total Amount Each Client has Spent
```sql
SUM(total_sales), client_id
FROM works_with
GROUP BY client_id; 
```
