select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select Country
from "mental_health"."main"."dim_geography"
where Country is null



      
    ) dbt_internal_test