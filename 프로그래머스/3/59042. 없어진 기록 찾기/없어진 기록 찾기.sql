select b.animal_id, b.name
# select *
from animal_ins a right join animal_outs b
on a.animal_id = b.animal_id
where a.datetime is null and b.datetime is not null
order by a.animal_id
