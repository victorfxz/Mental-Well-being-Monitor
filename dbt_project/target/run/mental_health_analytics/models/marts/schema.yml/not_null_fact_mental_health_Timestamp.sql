select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select Timestamp
from "mental_health"."main"."fact_mental_health"
where Timestamp is null



      
    ) dbt_internal_test