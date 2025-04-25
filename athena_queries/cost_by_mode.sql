# Executed in AWS Athena: delivery_analysis_db
# Purpose: Calculate average product cost by shipment mode

SELECT mode_of_shipment, 
AVG(CAST(cost_of_the_product AS DOUBLE)) AS avg_cost
FROM  processed
GROUP BY  mode_of_shipment;
