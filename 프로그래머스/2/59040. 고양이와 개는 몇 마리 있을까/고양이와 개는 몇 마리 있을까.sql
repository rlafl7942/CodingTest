-- 코드를 입력하세요
select animal_type, count(animal_id) count
from animal_ins
where animal_type in ("Dog", "Cat")
group by animal_type
order by animal_type 