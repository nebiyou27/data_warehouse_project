
  create view "telegram_data"."public"."raw_data_transformation__dbt_tmp"
    
    
  as (
    SELECT *
FROM telegram_messages
WHERE date IS NOT NULL
  );