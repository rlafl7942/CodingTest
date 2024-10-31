select count(id) fish_count, max(length) max_length, fish_type
from fish_info
group by fish_type
having avg(
    case when length is null then 10
         when length <= 10 then 10
         else length
    end
) >= 33
order by fish_type