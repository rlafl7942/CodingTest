select category, sum(sales) total_sales
from book_sales a join book b
on a.book_id = b.book_id
where date_format(a.sales_date, "%Y-%m") = "2022-01"
group by category
order by category