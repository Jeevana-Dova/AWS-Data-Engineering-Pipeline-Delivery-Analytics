# AWS-Data-Engineering-Pipeline-Delivery-Analytics

This project demonstrates an end-to-end data engineering workflow using AWS services. It focuses on analyzing delivery performance, customer satisfaction, discount strategies, and shipment modes by leveraging **Amazon S3**, **AWS Glue**, **Amazon Athena**, and **Amazon QuickSight**.

---

## **Project Overview**

**Goal:**  
To build a cloud-native pipeline that processes raw delivery data into actionable business insights through interactive dashboards.

**Key Questions Addressed:**
- Which shipment mode is most cost-effective?
- Do product importance levels affect discounts?
- What patterns exist in late deliveries?
- How does customer behavior vary by prior purchases?

---

## **Architecture**
Raw Dataset → Amazon S3 → AWS Glue (Crawler & ETL) → Athena SQL Queries → Amazon QuickSight Dashboards

----

##  **Tools & Services Used**

| **Layer**             | **Tool**              | **Purpose**                                 |
|-----------------------|-----------------------|---------------------------------------------|
| **Data Storage**      | Amazon S3             | Store raw and transformed data              |
| **Metadata Catalog**  | AWS Glue Crawler      | Auto-discover schema & create tables        |
| **ETL/Processing**    | AWS Glue Job          | Data cleaning & transformation              |
| **Query Layer**       | Amazon Athena         | SQL-based querying over S3 data             |
| **Visualization**     | Amazon QuickSight     | Dashboard creation and insight sharing      |

---

## **Dataset**

- **Source:** [Kaggle – Delivery Time Prediction Dataset](https://www.kaggle.com/datasets/prachi13/customer-analytics)  
- **Fields include:** `mode_of_shipment`, `product_importance`, `discount_offered`, `customer_rating`, `prior_purchases`, `on_time`, etc.  
- **Stored in:** `s3://deliveryefficiencyanalysisdata/raw/train.csv`

---

## **Process Steps**

### **1. Upload to Amazon S3**
- Raw dataset uploaded to:  
  `s3://deliveryefficiencyanalysisdata/raw/train.csv`

### **2. Glue Crawler Setup**
- Created database: `delivery_analysis_db`  
- Schema auto-generated for Athena

### **3. Glue Job (ETL)**
- Added `on_time` column to clarify delivery performance  
- Wrote cleaned data to:  
  `s3://deliveryefficiencyanalysisdata/processed/`

### **4. Athena Queries**
- Executed SQL to analyze:
  - Shipment mode costs
  - Discount impact vs product importance
  - Rating distribution
  - Late delivery counts by warehouse

### **5. QuickSight Dashboards**
**Visuals Include:**
- Avg. cost by shipment mode  
- Discounts vs prior purchases  
- Discount variation by product importance  
- Ratings vs mode of shipment (heatmap)  
- Delivery timeliness by warehouse  

---

