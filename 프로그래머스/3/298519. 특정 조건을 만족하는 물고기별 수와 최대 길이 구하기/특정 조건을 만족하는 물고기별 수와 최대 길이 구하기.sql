with new as (
    select id, fish_type,
    case when length is null then 10
         when length <= 10 then 10
         else length
    end length
    from fish_info
)

select count(id) fish_count, max(length) max_length, fish_type
from new
group by fish_type
having avg(length) >= 33
order by 3