
  
    
    

    create  table
      "mental_health"."main"."dim_geography__dbt_tmp"
  
    as (
      

SELECT
    ROW_NUMBER() OVER () as geography_id,
    Country,
    COUNT(*) as records_count
FROM "mental_health"."main"."stg_mental_health"
GROUP BY Country
    );
  
  