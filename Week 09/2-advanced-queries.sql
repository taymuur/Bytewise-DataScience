CREATE TABLE disease;
select * from Types, disease
where Types.ID=disease.ID;

select Types.Name AS "Plant Name", disease.dname as "Disease Name"
from Types t, disease d
where t.ID=d.ID;

select a.disease , b.disease
from disease a
inner join disease b
on a.dname=b.dname;

select disease.dname, Types.Season
from disease 
join Types
on disease.ID=Types.ID
order by disease.ID;

select l.dname, r.Season
from disease l
right join Types r
on l.ID=r.ID
order by l.ID;

select count(*) AS "Number_of_disease"
from disease;

select 'Total:' sum(Types)
from Types
group by ID;

select max(Types) 
from Types;

select * , Types*ID AS total_types
from Types
where Types>4
group by ID;
