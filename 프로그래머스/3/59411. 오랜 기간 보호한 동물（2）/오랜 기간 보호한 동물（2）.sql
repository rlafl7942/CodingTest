select a.animal_id, a.name
from animal_outs a join animal_ins b
on a.animal_id = b.animal_id
order by datediff(a.datetime, b.datetime) desc
limit 2