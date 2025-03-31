select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select geography_id
from "mental_health"."main"."dim_geography"
where geography_id is null



      
    ) dbt_internal_test