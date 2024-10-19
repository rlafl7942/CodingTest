-- 코드를 입력하세요
SELECT date_format(sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount
from (
    select user_id, sales_date, product_id, sales_amount from online_sale
    union all
    select null as user_id, sales_date, product_id, sales_amount 
    from offline_sale
) A
where date_format(sales_date, "%Y-%m") = "2022-03"
order by sales_date ASC, product_id ASC, user_id ASC