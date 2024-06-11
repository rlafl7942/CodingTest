-- 코드를 입력하세요
select b.user_id, b.nickname, sum(a.price) total_sales
from used_goods_board as a join used_goods_user as b
on a.writer_id = b.user_id
where a.status = "DONE"
group by a.writer_id
having sum(a.price)>=700000
order by total_sales