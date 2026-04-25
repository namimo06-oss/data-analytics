USE northwind;

-- 1. What is the product name(s) of the most expensive products?
-- HINT: Find the max price in a subquery and then use that value to find products
-- whose price equals that value. (Some of your answers from Exercise 3.A may offer a
-- useful starting point.)
-- ANSWER: the most expensive product is Cte de Blaye
SELECT 
	MAX(unitprice) AS Highestprice
FROM products;  -- To find the max price which is 263.5000
SELECT productname,unitprice
FROM products
WHERE unitprice = (SELECT MAX(unitprice) FROM products); -- too find what product corresponds to the max price 

-- 2). What is the product name(s) and categories of the least expensive products?
-- HINT: Find the min price in a subquery and then use that in your more complex
-- query that joins products with categories.
-- ANSWER: The least expensive product is Geitost and is under DairyProducts category
SELECT 
	MIN(unitprice) AS LeastExpensive
FROM products;  -- To find the lowest price which is 2.5000
SELECT 
	products.productname,
    categories.categoryname
FROM products
JOIN categories
	ON products.CategoryID = categories.Categoryid
WHERE unitprice = (SELECT MIN(unitprice) 
FROM products); 

-- 3). What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?
-- HINT: Find the shipper id of "Federal Shipping" in a subquery and then use that
-- value to find the orders that used that shipper.
-- You do not need "Federal Shipping" to display in the results.
SELECT shipperid 
FROM shippers WHERE companyname = 'Federal Shipping'; -- To Find shipper id of "federal shipping" which is 3
SELECT 
	orderid,
    shipname,
	shipaddress
FROM orders
WHERE shipvia = (SELECT shipperid FROM shippers WHERE shipperid = '3'
);

-- 4). What are the order ids of the orders that included "Sasquatch Ale"?
-- HINT: Find the product id of "Sasquatch Ale" in a subquery and then use that value
-- to find the matching orders from the `order details` table.
/*Your final results only need to display OrderID, but you may find it helpful to include
additional columns as you work on creating the query to better understand how the
query is working.*/
SELECT productid FROM products WHERE productname = 'Sasquatch Ale'; -- Productid of Sasquatch Ale is 34
SELECT 
	orderid,
    productid,
    quantity,
    unitprice
FROM `order details`
WHERE productid = (SELECT productid FROM products WHERE productid = '34'
);

-- 5). What is the name of the employee that sold order 10266?
-- ANSWER: the name of the employee that sold order 10266 was Janet Leverling
SELECT
	firstname,
    lastname
FROM employees
WHERE employeeid= (SELECT employeeid FROM orders WHERE orderid = 10266);

-- 6). What is the name of the customer that brought order 10266?
-- ANSWER: the name of the customer that brought order 10266 is Wartian Herkku.
SELECT customerid FROM orders WHERE orderid = 10266;
SELECT
	customerid, 
    CompanyName as CustomerName
FROM
    customers
WHERE
    CustomerID =(SELECT CustomerID FROM orders WHERE OrderID = 10266);
