select a.id, a.genotype, b.parent_genotype
from ecoli_data a join (
    select id, genotype parent_genotype
    from ecoli_data
) b
on a.parent_id = b.id
where a.genotype & b.parent_genotype = b.parent_genotype
order by 1