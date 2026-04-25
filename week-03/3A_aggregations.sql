USE northwind;

-- 1).Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price.
SELECT MIN(unitprice) AS CheapestPrice
FROM products; -- cheapest item price 
-- To find product name with that price
SELECT Productname, unitprice
FROM products
WHERE unitprice = ( SELECT MIN(unitprice) FROM products);

-- *2. Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.) 
SELECT AVG(unitprice) FROM products; -- To find average of all prices.
-- BONUS 
SELECT ROUND(AVG(unitprice), 2) AS Averageprice
FROM products; 

-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.
SELECT MAX(unitprice) AS Highestprice
FROM products; -- highest price 
-- To find product name with that price
SELECT 
	products.Productname,
	products.unitprice,
    suppliers.companyname AS Suppliername
FROM products
JOIN suppliers -- join suppliers to find suppliername because products only has supplierid no name
	on products.supplierID = Suppliers.supplierID
WHERE unitprice = ( 
	SELECT MAX(unitprice) 
    FROM products
);

-- 4). Write a query to find total monthly payroll (the sum of all the employees’ monthly salaries).
SELECT SUM(salary) AS TotalmontlyPayroll 
FROM employees;

-- 5). Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)
SELECT 
	MAX(salary) AS HighestSalary,
	MIN(salary) AS LowestSalary
FROM employees;

-- 6). Write a query to find the name and supplier ID of each supplier and the number of items they supply.
-- Hint: Join is your friend here.
SELECT 
	suppliers.supplierid, 
	suppliers.companyname,
    COUNT(products.productID) AS NumberofItems
FROM suppliers
JOIN products
	ON suppliers.supplierID = products.supplierID
GROUP BY suppliers.supplierid, suppliers.companyname;
    
-- 7). Write a query to find the list of all category names and the average price for items in
-- each category.
SELECT 
	categories.CategoryName,
    AVG(products.unitprice) AS AveragePrice
FROM categories
JOIN products 
	ON categories.CategoryID = Products.CategoryID
GROUP BY categories.categoryname;

-- 8). Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply.
SELECT 
	suppliers.companyname,
    COUNT(products.productid) AS ItemsSupplied
FROM suppliers
JOIN products
	ON suppliers.supplierid = products.supplierid
GROUP BY suppliers.companyname
HAVING COUNT(products.productid) >= 5 ;

-- 9).Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the samevalue,
-- order by product name. If a product is not in stock, leave it off the list.
SELECT 
	productid,
    productname,
    unitprice * UnitsInStock AS InventoryValue
FROM products
WHERE Unitsinstock > 0
ORDER BY 
	InventoryValue DESC, ProductName;