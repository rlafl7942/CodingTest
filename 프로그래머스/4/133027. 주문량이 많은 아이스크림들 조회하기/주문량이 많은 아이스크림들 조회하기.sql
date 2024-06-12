-- 코드를 입력하세요
select a.flavor
from first_half a left join july b
on a.flavor = b.flavor
group by a.flavor
having sum(a.total_order + b.total_order)
order by sum(a.total_order + b.total_order) desc limit 3