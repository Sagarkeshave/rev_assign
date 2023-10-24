
# # tables created in database and then imported csv data into it in supabase UI.

-- Create books table
CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title TEXT,
  author TEXT,
  publication_year INTEGER,
  available_copies INTEGER
);

-- Create users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  email TEXT
);

-- Create checkouts table
CREATE TABLE checkouts (
  id SERIAL PRIMARY KEY,
  book_id INTEGER REFERENCES books(id),
  user_id INTEGER REFERENCES users(id),
  checkout_date DATE,
  return_date DATE
);






1. Write a SQL query to retrieve the titles and authors of all books published before the
year 2000.

SELECT title, author 
FROM books 4. Create a query that calculates the average number of days a book is checked out.

WHERE publication_year < 2000;

2. Create a query that lists all users who have never checked out a book from the library.

SELECT name 
FROM users 
WHERE id NOT IN (SELECT DISTINCT user_id FROM checkouts);

3. Write a query to find the book with the most available copies.

SELECT title 
FROM books 
ORDER BY available_copies DESC 
LIMIT 1;

4. Create a query that calculates the average number of days a book is checked out.

select avg(return_date - checkout_date ) as avg_days
from checkouts

5. Write a SQL query to update the available_copies field of a book with the given id. You
can choose any book and update it with a new value.

UPDATE books
SET available_copies = (value)
WHERE id = (id);

