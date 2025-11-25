-- 1. View all data
SELECT * FROM sales


-- 2. Total revenue
SELECT SUM(Total) AS total_revenue FROM sales;

-- 3. Sales by product
SELECT Product, SUM(Total) AS product_sales
FROM sales
GROUP BY Product;

-- 4. Customer order count
SELECT Customer, COUNT(*) AS number_of_orders
FROM sales
GROUP BY Customer;