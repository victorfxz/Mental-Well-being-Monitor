select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select geography_id
from "mental_health"."main"."fact_mental_health"
where geography_id is null



      
    ) dbt_internal_test