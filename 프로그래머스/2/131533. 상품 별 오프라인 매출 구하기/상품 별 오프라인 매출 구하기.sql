select a.product_code, sum(a.price*(b.sales_amount)) sales
from product a join offline_sale b
on a.product_id = b.product_id
group by a.product_code
order by 2 desc, a.product_code