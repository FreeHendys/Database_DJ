### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
    PostgreSQL is an open source object relational database management system

- What is the difference between SQL and PostgreSQL?
    PostgreSQL is an advanced object-relational database management system which extends the subset of SQL standards
- In `psql`, how do you connect to a database?
    \c database_name
- What is the difference between `HAVING` and `WHERE`?
    Having applies to the group as a whole while Where applies to individual rows
- What is the difference between an `INNER` and `OUTER` join?
    Inner joins return matching data between the two tables while outer join returns all data
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
    Left outer returns all data from left table even if it has no matching data
    Right outer returns all data from Right table even if it has no matching data
- What is an ORM? What do they do?
    ORM stands for Object Relational Mapper. Bridges the gap between OOP and Databases
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  Server side request may require page reloads while Ajax will require DOM operations
- What is CSRF? What is the purpose of the CSRF token?
  CSRF tokens are a large value used in preventing CSRF attacks. The server will compare the token upon request to see if it is valid
- What is the purpose of `form.hidden_tag()`?
  You are able to hide CSRF tokens used in form requests
