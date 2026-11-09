-- Check odd values inside a specific column (amount)

SELECT 
	pu.purchase_id,
	c.country_name,
	pu.amount_usd,
	pu.boxes_shipped
FROM fact_sales pu
LEFT JOIN dim_countries c
ON c.country_id = pu.country_id
WHERE pu.amount_usd IS NULL
   OR pu.amount_usd <= 0
   OR pu.amount_usd >= 20000000