select a.emp_no, a.emp_name,
       case when b.score >= 96 then "S"
            when b.score >= 90 then "A"
            when b.score >= 80 then "B"
            else "C"
        end grade,
        case when b.score >= 96 then a.sal * 0.2
             when b.score >= 90 then a.sal * 0.15
             when b.score >= 80 then a.sal * 0.1
             else 0
        end bonus
from hr_employees a join (
    select emp_no as emp_number, (sum(score)/2) score
    from hr_grade
    group by emp_no
) b
on a.emp_no = b.emp_number
