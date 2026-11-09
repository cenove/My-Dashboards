-- Check if there's any duplicated value inside a key
SELECT
	purchase_id,
	COUNT(*) AS qtd
FROM fact_sales
GROUP BY purchase_id
HAVING COUNT(*) > 1;