select a.dept_id, a.dept_name_en, round(b.sal) avg_sal
from hr_department a join (
    select dept_id as department_id, avg(sal) sal
    from hr_employees
    group by 1
) b
on a.dept_id = b.department_id
order by 3 desc