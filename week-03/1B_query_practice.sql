USE northwind;
/*1).Write a query to list the product id, product name, and unit price of every product that
Northwind sells. (Hint: To help set up your query, look at the schema preview to see
what column names belong to each table. Or use SELECT * to query all columns
first, then refine your query to just the columns you want.)*/
SELECT productID, productname, unitprice FROM products;

-- 2).Write a query to identify the products where the unit price is $7.50 or less.
SELECT
	ProductID,
	ProductName,
	Unitprice
FROM Products
WHERE unitprice <= 7.50;

-- 3). What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question
SELECT productID,ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInstock = 0 
AND UnitsOnorder >= 1;

/*4). Examine the products table. How does it identify the type (category) of each item
sold? Where can you find a list of all categories? Write a set of queries to answer these
questions, ending with a query that creates a list of all the seafood items we carry.*/
/*SELECT * FROM Products;  THIS IS ANOTHER WAIT TO DO IT BUT USING JOINS
SELECT * FROM Categories;
SELECT 
	Products.ProductID,
    Products.ProductName,
    Categories.CategoryName
FROM Products 
JOIN Categories
	ON Products.CategoryID = Categories.CategoryID
WHERE Categories.CategoryName= 'Seafood'; */

SELECT CategoryID, CategoryName FROM categories; -- category ID for Seafood is 8
SELECT ProductID, ProductName, CategoryID FROM products
WHERE CategoryID = 8;


/* 5). Examine the products table again. How do you know what supplier each product
comes from? Where can you find info on suppliers? Write a set of queries to find the
specific identifier for "Tokyo Traders" and then find all products from that supplier */
SELECT supplierID, companyname
FROM suppliers
WHERE companyname= 'Tokyo Traders'; -- To find the specific identifier for Tokyo Traders=supplierid 4

SELECT ProductId, ProductName, SupplierID FROM products
WHERE SupplierID = 4; -- To find all products from that supplier

-- 6). How many employees work at northwind? What employees have "manager"
-- somewhere in their job title? Write queries to answer each question
SELECT COUNT(*) AS TotalEmployees
FROM Employees; -- To find how many employees work at northwind 

SELECT EmployeeID, LastName, FirstName, Title FROM employees
WHERE Title LIKE "%manager"; -- To find what employees have "manager" somewhere in their job title
