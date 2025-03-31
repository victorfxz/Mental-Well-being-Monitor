
    
    

select
    geography_id as unique_field,
    count(*) as n_records

from "mental_health"."main"."dim_geography"
where geography_id is not null
group by geography_id
having count(*) > 1


