select b.user_id, b.nickname, 
       concat(b.city," ",b.street_address1," ",street_address2) 전체주소, 
       concat(substr(b.tlno,1,3), "-", substr(b.tlno,4,4), "-", substr(b.tlno,8,4)) 전화번호
from used_goods_board a join used_goods_user b
on a.writer_id = b.user_id
group by a.writer_id
having count(a.writer_id) >= 3
order by b.user_id desc