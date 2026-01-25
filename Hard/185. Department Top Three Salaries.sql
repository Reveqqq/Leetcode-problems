-- Write your PostgreSQL query statement below

with top_salaries as (
    select 
        d.name as department,
        e.name as employee,
        e.salary as salary,
        dense_rank() over(partition by d.id order by e.salary desc) as dr
    from Employee e
    join Department d on e.departmentId = d.id
)
select 
    department as "Department",
    employee as "Employee",
    salary as "Salary"
from top_salaries
where dr <= 3