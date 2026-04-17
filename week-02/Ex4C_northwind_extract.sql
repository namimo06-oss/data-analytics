-- 4a. The table that holds the items Northwind sells is called: products.
-- 4b. The table that holds the types/categories of the items Northwind sells is: categories.

SELECT * FROM employees;
-- The employee whose name makes it sound like she is a bird is: Margaret Peacock.
-- becasue "Peacock" is a type of bird.

SELECT * FROM products;
-- 6a. The query returns 77 records. 
-- To show only 10 rows using the toolbar: 
-- Click the "limit rows" dropdown in My SQL workbench and set it to "Limit to 10 rows"

SELECT * FROM products
LIMIT 10;
-- The source that I use was W3schools.com. It was a little confusing because the "TOP" opotion didn't work but the "LIMIT" one did work.

SELECT * FROM categories;
-- The category id of seafood is 8. 

SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders
LIMIT 50;
-- I used LIMIT intead of TOP becuase it didn't work.