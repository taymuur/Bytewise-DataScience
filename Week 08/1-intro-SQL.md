## Structured Query Language
SQL is used to communicate with a database. According to ANSI (American National Standards Institute), it is the standard language for relational database management systems. SQL statements are used to perform tasks such as update data on a database, or retrieve data from a database.
* **Database:** A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.
* **Database Management System:** A database typically requires a comprehensive database software program known as a database management system (DBMS). A DBMS serves as an interface between the database and its end users or programs, allowing users to retrieve, update, and manage how the information is organized and optimized. A DBMS also facilitates oversight and control of databases, enabling a variety of administrative operations such as performance monitoring, tuning, and backup and recovery.
* **CRUD:** CREATE-READ-UPDATE-DELETE

### Relational SQL
Items in a relational database are organized as a set of tables with columns and rows. Relational database technology provides the most efficient and flexible way to access structured information. For example: PostgreSQL and Oracle.

A relational database has the following important features:
* `Primary key:` Uniquely identifies each row/record
* `Surrogate key:` Same as primary key but mapping is unavailable
* `Natural key:` Primary key but has mapping in real-world scenarios for example consider security number a primary key is also a natural key
* `Foreign key:` Primary key that links us to another table
* `Composite key:` Is a primary key but needs 2 attributes.

### Non-Relational SQL 
A NoSQL, or nonrelational database, allows unstructured and semistructured data to be stored and manipulated (in contrast to a relational database, which defines how all data inserted into the database must be composed). NoSQL databases grew popular as web applications became more common and more complex.

### Applications of SQL
- Standardized language for interacting with RDBMS
- Used to perform CRUD operations and administration tasks
- Used to define tables and structures
- SQL code is not always portable 
- Non-Relational DBMS have their own language for implementing CRUD operations 
- Query is set of instructions to tell DBMS what information you want it to retrieve for you.

### Componenets of SQL
* DQL: Data Query Language used to query database for information already stored.
* DDL: Data Definition Language used for defining database schemas.
* DCL: Data Control Language controls access to data (users/permissions)
* DML: Data Management Language (insert, update, delete)

*Implementation is performed in PostgreSQL.*
