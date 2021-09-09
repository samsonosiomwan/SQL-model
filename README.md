# A SQL Model

Writing a simple model classes for interaction with database tables using raw SQL for this task.

# Technologies
-PostgreSQL
-Psycopg2
-pandas
-numpy


### for context: Part I → PostgreSQL

We will be dealing with two database tables namely, users and books. Where users can have books in the database. Hence there is a one to many relationships between users and books, that is, a user can have many books and a book can only belong to one user.

Users table fields will include: `id`, `username`, `first_name`, `last_name`, `created_at` and `updated_at`

Books table fields will include: `id`, `user_id`, `name`, `pages`, `created_at` and `updated_at`


### Expectations

At the end of this task,  the following will be the outcome

1. A **schema file**, an SQL script that when run should create our database tables users and books that we will be working with.
2. A **seeder file**, which is a script that adds default data into these tables so we have default data we can play with first.
3. A **models** folder that holds all models files, that is user.py and book.py. These files will hold the definition of our model classes for communication with their respective database tables.
4. A **test folder** that will contain our written tests for the model classes



### Features implemented

Below is a list of actions we want to be able to perform using these models, and each one below should follow the workflow. This means that you should have 8 raised pull requests at the end of this exercise, which each pull request containing implementation for a model method and the test for it in the TDD order.

1. Fetch all users available: User.all()
2. Fetch one user by id : User.get(<int: id>)
3. Create a user record : User.create(params)
4. Update a user record: User.update(id, params)
5. Delete a user record: User.destroy(id) - CASCADE
6. Fetch all books available for a user: Book.all(user_id)
7. Fetch one book by id : Book.get(<int: id>) 
8. Create a book record : Book.create(user_id, params)
9. Update a book record: Book.update(id, params)
10. Delete a book record: Book.destroy(id)

### Part II → SQLite

In this part, we want to manage data presented in CSV format in the `grades.csv`, which contains data about student grades in different tests they have written. Check it out to understand the type of data you will be working with.

### Features implemented

1. Transfer data in CSV file into an SQLite database.
2. Performs CRUD operation on the transferred data
3. Fetch student that passed (has a final grade of 50 and above)
4. Fetch students that failed (has a final grade less than 50)
5. Fetch students that scored 45 and above in `test1`

# How to use;
-clone this repository
-set up postgres/sqlite database environment and keep it running
-follow the instructions on main.py
- set up database by removing comment # from the setup in main.py
- set up seed initial data by removing the # from 'check_set = set_up.setup_default_data()' on main.py
- comment set and check_set after setting up database and then uncomment any step on main.py to use the program as you please

