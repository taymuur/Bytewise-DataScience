## ER Diagrams

An Entity Relationship (ER) Diagram is a type of flowchart that illustrates how 'entities' such as people, objects or concepts relate to each other within a system. 

An ER diagram shows the relationship among entity sets. An entity set is a group of similar entities and these entities can have attributes. In terms of DBMS, an entity is a table or attribute of a table in database, so by showing relationship among tables and their attributes, ER diagram shows the complete logical structure of a database. 


* **Entity:** an object we want to model & store information about (student)

* **Attributes:** specific pieces of information about an entity (gpa, student id)

* **Primary Key:** an attribute(s) that uniquely identify an entry in the database table (student id)

* **Composite Attribute:** an attribute thatcan be broken up into sub-attributes (fname, lname)

* **Multi-valued Attribute:** an attribute that can have more than one value (clubs)

* **Derived Attribute:** an attribute that can be derived from the other attributes (honors)

* **Relationships:** defines a relationship between two entities

* **Total Participation:** all members must participate in the relationship

* **Weak Entity:** an entity that cannot be uniquely identified by its attributes alone (exam cannot exist without class)

* **Identifying Relationship:** a relationship that serves to uniquly identify the weak entity (HAS)

* **Relationship Cardianility:** number of related rows for each of the two objects in the relationship. The rows are related by the expression of the relationship; this expression usually refers to the primary and foreign keys of the underlying tables.

### Designing ER Diagram: Company Data 

* The company is organized into branches. Each branch has a unique number, a name, and a particular employee who manages it.

* The company makes it's money by selling to clients. Each client has a name and a unique umber to identify it.

* The foundation of the company is it's employees. Each employee has a name,birthday, sex,salary and a unique number.

* An employee can work for one branch at a time,and each branch will be managed by one of the employees that work there. We will also want to keep track of when the current manager started as manager.

* An employee can act as a supervisor for other employees at the branch, an employee may also act as the supervisor for employees at other branches. An employee can have at most one supervisor.

* A branch may handle a number of clients, with each client having a name and a unique number to identify it. A single client may only be handled by one branch at a time.

* Employees can work with clients controlled by their branch to sell them stuff. If nescessary multiple employees can work with the same client. We will want to keep track of how many dollars worth of stuff each employee sells to each client they work with.

* Many branches will need to work with suppliers to buy inventory. For each supplier we'll keep track of their name and the type of product they're selling the branch. A single supplier may supply products to multiple branches.
