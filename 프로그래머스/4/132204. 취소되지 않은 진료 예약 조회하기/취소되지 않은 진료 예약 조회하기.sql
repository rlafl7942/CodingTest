with A as (
    select a.apnt_no, b.pt_name, a.pt_no, a.mcdp_cd, a.apnt_ymd,
           a.mddr_id, a.apnt_cncl_yn
    from appointment a join patient b
    on a.pt_no = b.pt_no
)

select a.apnt_no, a.pt_name, a.pt_no, a.mcdp_cd, b.dr_name, a.apnt_ymd
from A a join doctor b
on a.mddr_id = b.dr_id
where a.apnt_cncl_yn = "N" and date_format(a.apnt_ymd, "%Y-%m-%d") = "2022-04-13"
order by a.apnt_ymd