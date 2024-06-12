-- 코드를 입력하세요
select a.product_id, a.product_name, (sum(b.amount)*a.price) total_sales
# select *
from food_product a join food_order b
on a.product_id = b.product_id
where b.produce_date like "2022-05%"
group by a.product_id
order by 3 desc, a.product_id