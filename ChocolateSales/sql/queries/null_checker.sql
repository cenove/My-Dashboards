-- Check if there's any Null values inside important columns

SELECT
	SUM(
		CASE 
			WHEN amount_usd IS NULL THEN 1 
			ELSE 0 
		END
	) AS null_amount,
	SUM(
		CASE
			WHEN product_id IS NULL THEN 1
			ELSE 0
		END
	) AS null_product
FROM fact_sales;