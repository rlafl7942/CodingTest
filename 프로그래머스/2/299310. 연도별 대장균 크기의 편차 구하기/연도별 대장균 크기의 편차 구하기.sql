select year(differentiation_date) year , 
(b.max_size - a.size_of_colony) year_dev, id
from ecoli_data a join (
    select year(differentiation_date) year, max(size_of_colony) max_size
    from ecoli_data
    group by year(differentiation_date)
) b
on year(a.differentiation_date) = b.year
order by year, year_dev