select b.score, a.emp_no, a.emp_name, a.position, a.email
from hr_employees a join (
    select emp_no as emp_number, sum(score) score
    from hr_grade
    group by emp_no
) b
on a.emp_no = b.emp_number
order by 1 desc
limit 1
