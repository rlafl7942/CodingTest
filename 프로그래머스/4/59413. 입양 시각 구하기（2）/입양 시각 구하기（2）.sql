with recursive rc as (
    select 0 as hour
    union all
    select hour + 1
    from rc
    where hour < 23
)

select b.hour, count(hour(a.datetime)) count
from rc b left join animal_outs a
on b.hour = hour(a.datetime)
group by 1