E-Commerce Customer Segmentation using RFM Analysis

A complete end-to-end Data Analysis project that leverages Python (Pandas, Matplotlib) and Excel to analyze customer transactional data, segment customers based on purchasing behavior, and drive strategic business decisions.

Project Overview
In modern e-commerce, understanding customer value is critical for retention and revenue growth. This project implements RFM (Recency, Frequency, Monetary) Analysis on a retail dataset to identify high-value customers, at-risk buyers, and lost accounts, enabling targeted marketing strategies.

 Tech Stack & Libraries Used
Python: Core programming language
Pandas: Data cleaning, preprocessing, and aggregation
Matplotlib: Data visualization (customer distribution charts)
Excel (.xlsx): Final reporting and stakeholder-ready output generation


Project Workflow & Code Logic
1. Data Loading & Preprocessing: 
    Loaded the transactional retail data using Pandas.
    Cleaned the data by handling missing values (dropna on CustomerID) and removing returns/cancellations (Quantity > 0).
    Created a calculated TotalPrice` column (Quantity * UnitPrice) and formatted invoice dates.
2. RFM Metric Calculation:
   Recency (R): Calculated how recently a customer made a purchase relative to the latest dataset date.
   Frequency (F): Counted the total number of unique purchases/transactions per customer.
   Monetary (M): Calculated the total revenue generated from each customer.
3. Customer Segmentation:
    Grouped customers into actionable tiers (e.g. Champions, Potential Loyalists, At-Risk, and Lost) based on their RFM behavior.
4. Export & Reporting:
    Exported the final segmented dataset into an organized Excel report (ecommerce_rfm_analysis) for business stakeholders.

 Final Output Snapshot
The processed output categorizes customers clearly with metrics and segmentation labels:
CustomerID | Recency | Frequency | Monetary | Segment

 How to Run the Project
1. Clone this repository or download the files.
2. Place your raw dataset (Online Retail.xlsX) in the project directory.
3. Run the Python script:
   
