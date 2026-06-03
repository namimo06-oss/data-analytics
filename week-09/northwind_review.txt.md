Exercise 2A Exploring the Northwind Database



Northwind Database



**QUESTIONS 6:**

* What is the primary key of the table?
* What are the parent tables of this table?(i.e. What tables do any foreign keys reference?)



1. Table : categories

&#x09;PK: CategoryID

&#x09;Parent Tables: none

2\. Table : customers

&#x09;PK: CustomerID

&#x09;Parent Tables: none

3\. Table : employees

&#x09;PK: EmployeeID

&#x09;Parent Tables: employees (through ReportsTo -- EmployeeID)

4\. Table : employeeterritories

&#x09;PK: EmployeeID 

&#x09;    TerritoryID

&#x09;Parent Tables: employees (EmployeeID → EmployeeID)

&#x09;	       territories (TerritoryID → TerritoryID)

5\. Table : order details

&#x09;PK: OrderID

&#x09;    ProductID

&#x09;Parent Tables: orders (OrderID → OrderID)

&#x09;	       products (ProductID → ProductID)

6\. Table : orders

&#x09;PK: OrderID

&#x09;    CustomerID

&#x09;    EmployeeID

&#x09;    OrderDate

&#x09;Parent Tables: customers (CustomerID → CustomerID)

&#x09;	       employees (EmployeeID → EmployeeID)

&#x09;	       shippers (ShipVia → ShipperID)

7\. Table : products

&#x09;PK: ProductID  

&#x09;    ProductName 

&#x20;   	    SupplierID  

&#x09;    CategoryID

&#x09;Parent Tables: categories (CategoryID → CategoryID)

&#x09;	       suppliers (SupplierID → SupplierID)

8\. Table : region

&#x09;PK: RegionID

&#x09;Parent Tables: none 

9\. Table : shippers

&#x09;PK: ShipperID

&#x09;Parent Tables: none

10\. Table : suppliers

&#x09;PK: SupplierID

&#x09;    CompanyName

&#x09;Parent Tables: none

11\. Table : territories

&#x09;PK: TerritoryID	

&#x09;Parent Tables: region (RegionID → RegionID)



**QUESTION 7:**

&#x09;

1. What does a value in this column represent? What values might you see here?
2. Is this column a part of the primary key to this table?
3. Is this column a part of a foreign key that points to a record in another table?
4. Would this column be valuable to bring into our Power BI Model? Yes, or no? Why?
5. Do you believe this column is appropriately named for Data Analysis purposes?
6. If not, what might be a more appropriate name?
7. What might be the data type and format for this column in a Power BI Model?
8. Can you think of any calculations where this column data might be used?



==================================================

TABLE:CATEGORIES

==================================================



Column: CategoryID

\- Represents: Unique ID for each category.

\- Primary Key? Yes.

\- Foreign Key? No.

\- Valuable in Power BI? Yes, to connect categories with products.

\- Good name? Yes.

\- Power BI type: Whole Number.

\- Calculations: Count of categories.



Column: CategoryName

\- Represents: Name of the category, like Beverages or Seafood.

\- Primary Key? No.

\- Foreign Key? No.

\- Valuable in Power BI? Yes, to group/filter sales by category.

\- Good name? Yes.

\- Power BI type: Text.

\- Calculations: Sales by category, count products by category.



Column: Description

\- Represents: Description of the category.

\- Primary Key? No.

\- Foreign Key? No.

\- Valuable in Power BI? Maybe, but not very useful for calculations.

\- Good name? Yes.

\- Power BI type: Text.

\- Calculations: None, mostly used as extra detail.



Column: Picture

\- Represents: Image of the category.

\- Primary Key? No.

\- Foreign Key? No.

\- Valuable in Power BI? No, probably not needed for analysis.

\- Good name? Yes.

\- Power BI type: Binary/Image.

\- Calculations: None.



==================================================

TABLE: CUSTOMERS

==================================================





Column: CustomerID

1\. Represents: The unique ID for each customer. Values might be ALFKI, ANATR, or BERGS.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, because it connects customers to orders.

5\. Appropriate name? Yes.

6\. Better name: Customer ID.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count of customers, orders per customer.



Column: CompanyName

1\. Represents: The customer's company name. Values might be Alfreds Futterkiste or Around the Horn.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for identifying and grouping customers.

5\. Appropriate name? Yes.

6\. Better name: Company Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count of customers by company.



Column: ContactName

1\. Represents: The name of the contact person for the customer.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful as extra customer detail.

5\. Appropriate name? Yes.

6\. Better name: Contact Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none; could count contacts.



Column: ContactTitle

1\. Represents: The job title of the contact person. Values might be Owner or Sales Representative.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for grouping contacts by role.

5\. Appropriate name? Yes.

6\. Better name: Contact Title.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count of contacts by title.



Column: Address

1\. Represents: The customer's street address.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for detailed location information but not always needed for analysis.

5\. Appropriate name? Yes.

6\. Better name: Customer Address.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: City

1\. Represents: The city where the customer is located. Values might be Berlin, London, or Madrid.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic analysis.

5\. Appropriate name? Yes.

6\. Better name: Customer City.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count customers by city, sales by city.



Column: Region

1\. Represents: The customer's state, province, or region when available.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic grouping, but may have missing values.

5\. Appropriate name? Mostly yes.

6\. Better name: Customer Region.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count customers by region, sales by region.



Column: PostalCode

1\. Represents: The customer's postal or ZIP code.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for detailed location analysis.

5\. Appropriate name? Yes.

6\. Better name: Customer Postal Code.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count customers by postal code.



Column: Country

1\. Represents: The country where the customer is located. Values might be Germany, USA, or UK.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic analysis and filtering.

5\. Appropriate name? Yes.

6\. Better name: Customer Country.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Sales by country, customers by country.



Column: Phone

1\. Represents: The customer's phone number.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, because it is contact information, not analysis data.

5\. Appropriate name? Yes.

6\. Better name: Customer Phone.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: Fax

1\. Represents: The customer's fax number.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, because it is operational contact information.

5\. Appropriate name? Yes.

6\. Better name: Customer Fax.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



==================================================

TABLE: EMPLOYEES

==================================================



Column: EmployeeID

1\. Represents: The unique ID for each employee. Values might be 1, 2, or 3.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, because it connects employees to orders.

5\. Appropriate name? Yes.

6\. Better name: Employee ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Count of employees, orders by employee.



Column: LastName

1\. Represents: The employee's last name.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful to identify employees.

5\. Appropriate name? Yes.

6\. Better name: Last Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none; could count employees by name.



Column: FirstName

1\. Represents: The employee's first name.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful to identify employees.

5\. Appropriate name? Yes.

6\. Better name: First Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: Title

1\. Represents: The employee's job title. Values might be Sales Representative or Sales Manager.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for grouping employees by role.

5\. Appropriate name? Mostly yes.

6\. Better name: Job Title.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count employees by title, sales by title.



Column: TitleOfCourtesy

1\. Represents: The employee's courtesy title. Values might be Mr., Ms., or Dr.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, because it is not very useful for business analysis.

5\. Appropriate name? Yes.

6\. Better name: Courtesy Title.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: BirthDate

1\. Represents: The employee's birth date.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for employee age analysis.

5\. Appropriate name? Yes.

6\. Better name: Birth Date.

7\. Power BI Data Type/Format: Date.

8\. Possible calculations: Employee age.



Column: HireDate

1\. Represents: The date the employee was hired.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for tenure analysis.

5\. Appropriate name? Yes.

6\. Better name: Hire Date.

7\. Power BI Data Type/Format: Date.

8\. Possible calculations: Employee tenure, hires by year.



Column: Address

1\. Represents: The employee's street address.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, because it is personal contact information.

5\. Appropriate name? Yes.

6\. Better name: Employee Address.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: City

1\. Represents: The city where the employee is located.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for employee location analysis.

5\. Appropriate name? Yes.

6\. Better name: Employee City.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count employees by city.



Column: Region

1\. Represents: The employee's state or region.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for geographic grouping.

5\. Appropriate name? Mostly yes.

6\. Better name: Employee Region.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count employees by region.



Column: PostalCode

1\. Represents: The employee's postal or ZIP code.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, too detailed for most analysis.

5\. Appropriate name? Yes.

6\. Better name: Employee Postal Code.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: Country

1\. Represents: The country where the employee is located.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for employee location analysis.

5\. Appropriate name? Yes.

6\. Better name: Employee Country.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count employees by country.



Column: HomePhone

1\. Represents: The employee's home phone number.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? No, it is contact information, not analysis data.

5\. Appropriate name? Yes.

6\. Better name: Home Phone.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: Extension

1\. Represents: The employee's phone extension.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, it is operational contact information.

5\. Appropriate name? Yes.

6\. Better name: Phone Extension.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: Photo

1\. Represents: The employee's photo.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, not useful for data analysis.

5\. Appropriate name? Yes.

6\. Better name: Employee Photo.

7\. Power BI Data Type/Format: Binary/Image.

8\. Possible calculations: None.



Column: Notes

1\. Represents: Extra notes about the employee.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, unless used for descriptive details.

5\. Appropriate name? Yes.

6\. Better name: Employee Notes.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: ReportsTo

1\. Represents: The manager or supervisor that the employee reports to. Values might be another EmployeeID.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? Yes, references Employees.EmployeeID.

4\. Valuable for Power BI? Yes, useful for employee hierarchy analysis.

5\. Appropriate name? Mostly yes.

6\. Better name: Manager Employee ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Employees per manager, sales by manager.



Column: PhotoPath

1\. Represents: The file path or link to the employee photo.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, unless images are needed in the report.

5\. Appropriate name? Yes.

6\. Better name: Photo Path.

7\. Power BI Data Type/Format: Text or Image URL.

8\. Possible calculations: None.



Column: Salary

1\. Represents: The employee's salary.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for payroll or compensation analysis.

5\. Appropriate name? Yes.

6\. Better name: Employee Salary.

7\. Power BI Data Type/Format: Decimal Number or Currency.

8\. Possible calculations: Average salary, total salary, salary by job title.



==================================================

TABLE: EMPLOYEETERRITORIES

==================================================



Column: EmployeeID

1\. Represents: The employee assigned to a territory. Values might be 1, 2, or 3.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? Yes, references Employees.EmployeeID.

4\. Valuable for Power BI? Yes, connects employees with territories.

5\. Appropriate name? Yes.

6\. Better name: Employee ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Count territories per employee.



Column: TerritoryID

1\. Represents: The territory assigned to an employee. Values might be territory codes such as 01581.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? Yes, references Territories.TerritoryID.

4\. Valuable for Power BI? Yes, connects employees with territories.

5\. Appropriate name? Yes.

6\. Better name: Territory ID.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count employees per territory.



==================================================

TABLE: ORDER DETAILS

==================================================



Column: OrderID

1\. Represents: The order that contains the product. Values might be 10248 or 10249.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? Yes, references Orders.OrderID.

4\. Valuable for Power BI? Yes, connects order details to orders.

5\. Appropriate name? Yes.

6\. Better name: Order ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Count of orders, sales by order.



Column: ProductID

1\. Represents: The product included in the order. Values might be 1, 2, or 11.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? Yes, references Products.ProductID.

4\. Valuable for Power BI? Yes, connects sales to products.

5\. Appropriate name? Yes.

6\. Better name: Product ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Sales by product, quantity sold by product.



Column: UnitPrice

1\. Represents: The unit price of the product at the time of the order.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, needed for revenue calculations.

5\. Appropriate name? Yes.

6\. Better name: Unit Price.

7\. Power BI Data Type/Format: Decimal Number or Currency.

8\. Possible calculations: Revenue = UnitPrice \* Quantity.



Column: Quantity

1\. Represents: The number of units sold in the order.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, needed to analyze units sold.

5\. Appropriate name? Yes.

6\. Better name: Quantity Sold.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Total quantity sold, average quantity per order.



Column: Discount

1\. Represents: The discount applied to the order line. Values might be 0, 0.05, or 0.10.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for discount and revenue analysis.

5\. Appropriate name? Yes.

6\. Better name: Discount Rate.

7\. Power BI Data Type/Format: Decimal Number or Percentage.

8\. Possible calculations: Discounted revenue, average discount.



==================================================

TABLE: ORDERS

==================================================



Column: OrderID

1\. Represents: The unique ID for each order. Values might be 10248 or 10249.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, connects orders with order details.

5\. Appropriate name? Yes.

6\. Better name: Order ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Count of orders.



Column: CustomerID

1\. Represents: The customer who placed the order. Values might be ALFKI or ANATR.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? Yes, references Customers.CustomerID.

4\. Valuable for Power BI? Yes, connects orders to customers.

5\. Appropriate name? Yes.

6\. Better name: Customer ID.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Orders by customer, sales by customer.



Column: EmployeeID

1\. Represents: The employee responsible for the order.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? Yes, references Employees.EmployeeID.

4\. Valuable for Power BI? Yes, connects orders to employees.

5\. Appropriate name? Yes.

6\. Better name: Employee ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Orders by employee, sales by employee.



Column: OrderDate

1\. Represents: The date the order was placed.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, important for time trend analysis.

5\. Appropriate name? Yes.

6\. Better name: Order Date.

7\. Power BI Data Type/Format: Date.

8\. Possible calculations: Orders by month, sales by year.



Column: RequiredDate

1\. Represents: The date the order was required or expected by the customer.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for fulfillment timing analysis.

5\. Appropriate name? Yes.

6\. Better name: Required Date.

7\. Power BI Data Type/Format: Date.

8\. Possible calculations: Days between order date and required date.



Column: ShippedDate

1\. Represents: The date the order was shipped.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for shipping performance analysis.

5\. Appropriate name? Yes.

6\. Better name: Shipped Date.

7\. Power BI Data Type/Format: Date.

8\. Possible calculations: Shipping delay, average days to ship.



Column: ShipVia

1\. Represents: The shipper used for the order. Values point to a ShipperID.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? Yes, references Shippers.ShipperID.

4\. Valuable for Power BI? Yes, useful for shipping company analysis.

5\. Appropriate name? Not fully clear.

6\. Better name: Shipper ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Orders by shipper, freight by shipper.



Column: Freight

1\. Represents: The shipping cost for the order.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for cost analysis.

5\. Appropriate name? Mostly yes.

6\. Better name: Freight Cost.

7\. Power BI Data Type/Format: Decimal Number or Currency.

8\. Possible calculations: Total freight, average freight cost.



Column: ShipName

1\. Represents: The shipping recipient name or company name.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for shipping details.

5\. Appropriate name? Mostly yes.

6\. Better name: Ship To Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: ShipAddress

1\. Represents: The shipping street address.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, but it may be too detailed for analysis.

5\. Appropriate name? Yes.

6\. Better name: Shipping Address.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: ShipCity

1\. Represents: The city where the order was shipped.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic shipping analysis.

5\. Appropriate name? Yes.

6\. Better name: Shipping City.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Orders by city, freight by city.



Column: ShipRegion

1\. Represents: The region/state where the order was shipped.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic analysis.

5\. Appropriate name? Yes.

6\. Better name: Shipping Region.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Orders by region, sales by region.



Column: ShipPostalCode

1\. Represents: The postal or ZIP code where the order was shipped.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for detailed location analysis.

5\. Appropriate name? Yes.

6\. Better name: Shipping Postal Code.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Orders by postal code.



Column: ShipCountry

1\. Represents: The country where the order was shipped.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic analysis.

5\. Appropriate name? Yes.

6\. Better name: Shipping Country.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Orders by country, sales by country.



==================================================

TABLE: PRODUCTS

==================================================



Column: ProductID

1\. Represents: The unique ID for each product.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, connects products to order details.

5\. Appropriate name? Yes.

6\. Better name: Product ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Count of products, sales by product.



Column: ProductName

1\. Represents: The product name. Values might be Chai or Chang.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for reporting and filtering.

5\. Appropriate name? Yes.

6\. Better name: Product Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Sales by product, quantity sold by product.



Column: SupplierID

1\. Represents: The supplier that provides the product.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? Yes, references Suppliers.SupplierID.

4\. Valuable for Power BI? Yes, connects products to suppliers.

5\. Appropriate name? Yes.

6\. Better name: Supplier ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Products by supplier, sales by supplier.



Column: CategoryID

1\. Represents: The category the product belongs to.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? Yes, references Categories.CategoryID.

4\. Valuable for Power BI? Yes, connects products to categories.

5\. Appropriate name? Yes.

6\. Better name: Category ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Products by category, sales by category.



Column: QuantityPerUnit

1\. Represents: How the product is packaged or sold. Values might be 10 boxes x 20 bags.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for product detail but not many calculations.

5\. Appropriate name? Mostly yes.

6\. Better name: Quantity Per Unit.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: UnitPrice

1\. Represents: The current unit price of the product.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for price and revenue analysis.

5\. Appropriate name? Yes.

6\. Better name: Unit Price.

7\. Power BI Data Type/Format: Decimal Number or Currency.

8\. Possible calculations: Average product price, estimated revenue.



Column: UnitsInStock

1\. Represents: The number of units currently in stock.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for inventory analysis.

5\. Appropriate name? Yes.

6\. Better name: Units In Stock.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Total units in stock, low stock products.



Column: UnitsOnOrder

1\. Represents: The number of units already ordered from suppliers.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for inventory planning.

5\. Appropriate name? Yes.

6\. Better name: Units On Order.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Total units on order.



Column: ReorderLevel

1\. Represents: The inventory level where the product should be reordered.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful to identify products that need restocking.

5\. Appropriate name? Yes.

6\. Better name: Reorder Level.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Products below reorder level.



Column: Discontinued

1\. Represents: Whether the product is discontinued. Values might be 0 for active or 1 for discontinued.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful to filter active vs discontinued products.

5\. Appropriate name? Yes.

6\. Better name: Is Discontinued.

7\. Power BI Data Type/Format: True/False or Whole Number.

8\. Possible calculations: Count discontinued products, sales of active products.



==================================================

TABLE: REGION

==================================================



Column: RegionID

1\. Represents: The unique ID for each region.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, connects regions to territories.

5\. Appropriate name? Yes.

6\. Better name: Region ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Count of regions, territories per region.



Column: RegionDescription

1\. Represents: The name or description of the region. Values might be Eastern or Western.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for grouping and filtering by region.

5\. Appropriate name? Mostly yes.

6\. Better name: Region Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Sales by region, employees by region.



==================================================

TABLE: SHIPPERS

==================================================



Column: ShipperID

1\. Represents: The unique ID for each shipping company.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, connects shippers to orders.

5\. Appropriate name? Yes.

6\. Better name: Shipper ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Orders by shipper.



Column: CompanyName

1\. Represents: The shipping company's name. Values might be Speedy Express or United Package.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for shipping analysis.

5\. Appropriate name? Yes.

6\. Better name: Shipper Company Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Freight by shipper, orders by shipper.



Column: Phone

1\. Represents: The shipper's phone number.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, because it is contact information.

5\. Appropriate name? Yes.

6\. Better name: Shipper Phone.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



==================================================

TABLE: SUPPLIERS

==================================================



Column: SupplierID

1\. Represents: The unique ID for each supplier.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, connects suppliers to products.

5\. Appropriate name? Yes.

6\. Better name: Supplier ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Count of suppliers, products per supplier.



Column: CompanyName

1\. Represents: The supplier company name.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for supplier reporting.

5\. Appropriate name? Yes.

6\. Better name: Supplier Company Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Products by supplier, sales by supplier.



Column: ContactName

1\. Represents: The supplier contact person's name.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful as extra detail.

5\. Appropriate name? Yes.

6\. Better name: Contact Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: ContactTitle

1\. Represents: The supplier contact person's job title.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for contact role analysis.

5\. Appropriate name? Yes.

6\. Better name: Contact Title.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count contacts by title.



Column: Address

1\. Represents: The supplier's street address.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for location details.

5\. Appropriate name? Yes.

6\. Better name: Supplier Address.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: City

1\. Represents: The city where the supplier is located.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic analysis.

5\. Appropriate name? Yes.

6\. Better name: Supplier City.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Suppliers by city.



Column: Region

1\. Represents: The supplier's region, state, or province when available.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic grouping.

5\. Appropriate name? Mostly yes.

6\. Better name: Supplier Region.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Suppliers by region.



Column: PostalCode

1\. Represents: The supplier's postal or ZIP code.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Sometimes, useful for detailed location analysis.

5\. Appropriate name? Yes.

6\. Better name: Supplier Postal Code.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Suppliers by postal code.



Column: Country

1\. Represents: The country where the supplier is located.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for geographic analysis.

5\. Appropriate name? Yes.

6\. Better name: Supplier Country.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Suppliers by country, sales by supplier country.



Column: Phone

1\. Represents: The supplier's phone number.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, because it is contact information.

5\. Appropriate name? Yes.

6\. Better name: Supplier Phone.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: Fax

1\. Represents: The supplier's fax number.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, because it is contact information.

5\. Appropriate name? Yes.

6\. Better name: Supplier Fax.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Usually none.



Column: HomePage

1\. Represents: The supplier's website or homepage information.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Usually no, unless links are needed in the report.

5\. Appropriate name? Mostly yes.

6\. Better name: Supplier Website.

7\. Power BI Data Type/Format: Text or Web URL.

8\. Possible calculations: Usually none.



==================================================

TABLE: TERRITORIES

==================================================



Column: TerritoryID

1\. Represents: The unique ID for each sales territory.

2\. Part of Primary Key? Yes.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, connects territories to employees and regions.

5\. Appropriate name? Yes.

6\. Better name: Territory ID.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Count of territories, employees per territory.



Column: TerritoryDescription

1\. Represents: The name or description of the territory.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? No.

4\. Valuable for Power BI? Yes, useful for grouping and filtering.

5\. Appropriate name? Mostly yes.

6\. Better name: Territory Name.

7\. Power BI Data Type/Format: Text.

8\. Possible calculations: Sales by territory, employees by territory.



Column: RegionID

1\. Represents: The region that the territory belongs to.

2\. Part of Primary Key? No.

3\. Part of Foreign Key? Yes, references Region.RegionID.

4\. Valuable for Power BI? Yes, connects territories to regions.

5\. Appropriate name? Yes.

6\. Better name: Region ID.

7\. Power BI Data Type/Format: Whole Number.

8\. Possible calculations: Territories per region, sales by region.







