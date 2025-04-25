# Query executed in Amazon Athena Console under 'delivery_analysis_db'
# Exported to GitHub for reproducibility


CREATE EXTERNAL TABLE IF NOT EXISTS delivery_analysis_db.delivery_parquet (
  ID STRING,
  Warehouse_block STRING,
  Mode_of_Shipment STRING,
  Customer_care_calls INT,
  Customer_rating INT,
  Cost_of_the_Product INT,
  Prior_purchases INT,
  Product_importance STRING,
  Gender STRING,
  Discount_offered INT,
  Weight_in_gms INT,
  Reached_on_Time_Y_N INT,
  On_Time STRING
)
