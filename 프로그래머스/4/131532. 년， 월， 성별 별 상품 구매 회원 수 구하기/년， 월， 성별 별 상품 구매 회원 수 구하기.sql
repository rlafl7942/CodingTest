with new as (
    select a.user_id, a.sales_date, b.gender
    from online_sale a join user_info b
    on a.user_id = b.user_id
)

select year(sales_date) year,
       month(sales_date) month, gender, count(distinct(user_id)) users
from new
where gender is not null
group by year, month, gender
order by year, month, gender