-- Check if any product is missing
SELECT pu.*
FROM fact_sales pu
LEFT JOIN dim_products pr
    ON pu.product_id = pr.product_id
WHERE pr.product_id IS NULL
  AND pu.product_id IS NOT NULL;