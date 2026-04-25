USE northwind;

-- 1). Create a single query to list the product id, product name, unit price and category
-- name of all products. Order by category name and within that, by product name.
SELECT 
	productid,
    productname,
    unitprice,
    categoryname 
FROM products
JOIN categories
	ON products.categoryid= categories.CategoryID
ORDER BY categories.categoryname, products.productname;

-- 2).Create a single query to list the product id, product name, unit price and supplier
-- name of all products that cost more than $75. Order by product name.
SELECT productid, productname, unitprice, companyname AS suppliername
FROM products
JOIN suppliers
	ON products.supplierid = suppliers.supplierid
WHERE unitprice > 75
ORDER BY products.productname;

-- 3). Create a single query to list the product id, product name, unit price, category name,
-- and supplier name of every product. Order by product name.
SELECT 
	productid,
    productname,
    unitprice,
    categoryname,
    companyname AS suppliername 
FROM products
JOIN categories
	ON products.CategoryID= categories.CategoryID
JOIN suppliers
	ON products.supplierid= suppliers.SupplierID
ORDER BY products.ProductName;

-- 4). Create a single query to list the order id, ship name, ship address, and shipping
-- company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.
SELECT 
	orders.orderid,
    orders.shipname,
    orders.shipaddress,
    shhippers.companyname AS Shipper,
    orders.shipcountry
FROM Orders
JOIN shippers
	ON orders.shipvia = shippers.ShipperID
WHERE orders.shipcountry = 'Germany'
ORDER BY shipper, shipname;

-- 5). Start from the same query as above (#4), but omit OrderID and add logic to group by
-- ship name, with a count of how many orders were shipped for that ship name.
SELECT 
    orders.shipname, COUNT(shipname) AS "Number of Orders",
    orders.shipaddress,
    shippers.companyname AS Shipper,
	orders.shipcountry
FROM Orders
JOIN shippers
	ON orders.shipvia = shippers.ShipperID
WHERE orders.shipcountry = 'Germany'
GROUP BY shipname, shipaddress, shipper, shipcountry
ORDER BY shipper, shipname;

/* 6). Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.*/
SELECT 
	orders.orderid,
    orders.orderdate,
    orders.shipname,
    orders.shipaddress,
    products.productname
FROM orders
JOIN northwind.`order details` ON northwind.`order details`.OrderID = orders.OrderID
JOIN products ON products.ProductID = northwind.`order details`.ProductID 
WHERE products.ProductName = 'Sasquatch Ale';
