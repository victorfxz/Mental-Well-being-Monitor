
    
    

with child as (
    select geography_id as from_field
    from "mental_health"."main"."fact_mental_health"
    where geography_id is not null
),

parent as (
    select geography_id as to_field
    from "mental_health"."main"."dim_geography"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


