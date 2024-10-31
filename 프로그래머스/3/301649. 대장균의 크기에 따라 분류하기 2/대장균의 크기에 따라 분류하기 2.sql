with new as (
    select id, rank() over(order by size_of_colony desc) ranking, count(id) over() total
    from ecoli_data
)

select id,
    case when (ranking/total*100) <= 25 then "CRITICAL"
         when (ranking/total*100) <= 50 then "HIGH"
         when (ranking/total*100) <= 75 then "MEDIUM"
         else "LOW"
    end colony_name
from new
order by id