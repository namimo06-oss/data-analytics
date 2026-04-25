-- NOTES 04/24/26
USE sakila;

SELECT first_name,last_name, email FROM staff
UNION -- is like an OR
SELECT first_name,last_name, email FROM customer;

SELECT first_name FROM staff
UNION ALL -- turns off dupplication
SELECT first_name FROM customer;

-- We wont get any results back because there is 
-- no one from staff and customer with the same email
SELECT first_name, email FROM staff
INTERSECT -- combination of top and bottom. Its like an AND
SELECT first_name, email FROM customer;

-- example using EXCEPT, using first result minus second result
SELECT first_name FROM staff
EXCEPT 
SELECT first_name FROM customer; -- nothing will come out 

-- ORDER REALLY MATTERS IN EXCEPT 
SELECT first_name FROM customer
EXCEPT
SELECT first_name FROM staff;


-- another UNION example
USE world;

-- this will give me the result of languages of countries 
-- that have a GNP higher than 1000000 and population higher 50Million
SELECT Language FROM countrylanguage
JOIN country ON country.code= countrylanguage.countrycode
WHERE country.GNP > 1000000
UNION
SELECT Language FROM countrylanguage
JOIN country ON country.code= countrylanguage.countrycode
WHERE country.population > 50000000; 

-- EXCEPT EXAMPLE
SELECT Language FROM countrylanguage
JOIN country ON country.code= countrylanguage.countrycode
WHERE country.GNP > 1000000
EXCEPT -- USING IT TO FILTER RESULTS OUT FROM THE FIRST ONE 
SELECT Language FROM countrylanguage
JOIN country ON country.code= countrylanguage.countrycode
WHERE country.population < 50000000; 

-- ---------
-- comparing 

    
-- rewriting as CTE

WITH AvgGNPCont AS (
	SELECT 
		Continent, 
		ROUND(Avg(GNP),0) AS "Avg GNP by continent"
    FROM country 
    GROUP BY continent
)
SELECT 
	ROUND(AVG(country.GNP),0) AS "Avg GNP by continent",
    AvgGNPCont. `Avg GNP by continent`,
    country.region,
    country.continent
FROM country
JOIN AvgGNPCont ON country.Continent = AvgGNPCont.Continent
GROUP BY country.continent, country.region, `Avg GNP by Continent`
ORDER BY  country.continent, country.region;

-- -------
USE sakila;

-- setting up CASE example
SELECT 
	first_name,
	CASE first_name
		WHEN 'Mike' THEN 'Skip'
		WHEN 'Jon' THEN 'JJ'
		ELSE first_name
		END AS Nickname
FROM staff;

SELECT
	customer.customer_id,
    customer.first_name,
    customer.last_name,
    COUNT(rental.rental_id) AS num_of_rentals,
	CASE
		WHEN COUNT(rental.rental_id) > 35 THEN 'Platinum VIP'
        WHEN COUNT(rental.rental_id) > 25 THEN "Gold VIP"
        WHEN COUNT(rental.rental_id) > 15 THEN 'VIP'
		ELSE 'none'
	END AS 'VIP STATUS'
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
GROUP BY customer.customer_id, customer.first_name, customer.last_name
ORDER BY num_of_rentals;

    
    










