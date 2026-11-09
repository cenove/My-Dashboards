-- that script show us what was the total amount after discounts for each sale
DECLARE @discount_divisor DECIMAL(5,2) = 3.5;
SELECT
    purchase_id,
    sales_person_id,
    purchase_date,
    amount_usd,
    CAST((amount_usd / @discount_divisor) AS DECIMAL(18,2)) AS discount,
    CAST((amount_usd - (amount_usd / @discount_divisor)) AS DECIMAL(18,2)) AS revenue,
    CAST(
        SUM(amount_usd - (amount_usd / @discount_divisor)) OVER(
            PARTITION BY sales_person_id
            ORDER BY purchase_date, purchase_id
        ) AS DECIMAL(18,2)
    ) AS running_revenue
FROM fact_sales;