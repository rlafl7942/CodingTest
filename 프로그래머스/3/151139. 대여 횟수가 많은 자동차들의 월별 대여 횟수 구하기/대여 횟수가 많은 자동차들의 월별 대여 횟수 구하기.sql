-- 코드를 입력하세요
select month(start_date) month, car_id, count(car_id) records
from car_rental_company_rental_history
where car_id in (
    select car_id from car_rental_company_rental_history
    where start_date between "2022-08-01" and "2022-11-01"
    group by car_id
    having count(car_id)>=5
) and start_date between "2022-08-01" and "2022-11-01"
group by month, car_id
order by month, car_id desc