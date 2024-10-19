with A as (
    select a.book_id, a.category, a.author_id, a.price, b.author_name
    from book a join author b
    on a.author_id = b.author_id
)

select a.author_id, a.author_name, a.category, (sum(sales * price)) total_sales
from A a join book_sales b
on a.book_id = b.book_id
where date_format(sales_date, "%Y-%m") = "2022-01"
group by a.author_id, category
order by a.author_id, category desc