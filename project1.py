import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: LOAD DATA
# ==========================================
# Apni CSV file load karein (encoding zaroori hai is dataset ke liye)
df = pd.read_excel('Online Retail.xlsx')
print("Initial Data Shape:", df.shape)


# ==========================================
# STEP 2: DATA CLEANING & PREPROCESSING
# ==========================================

df = df.dropna(subset=['CustomerID'])


df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[df['Quantity'] > 0]


df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

print("Cleaned Data Shape:", df.shape)


# ==========================================
# STEP 3: CALCULATE RFM METRICS
# ==========================================
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, 
    'InvoiceNo': 'nunique',                                   
    'TotalPrice': 'sum'                                      
})

#
rfm.columns = ['Recency', 'Frequency', 'Monetary']


# ==========================================
# STEP 4: SCORE & SEGMENT CUSTOMERS
# ==========================================

r_labels = range(4, 0, -1)
f_labels = range(1, 5)
m_labels = range(1, 5)

rfm['R'] = pd.qcut(rfm['Recency'], 4, labels=r_labels)
rfm['F'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=f_labels)
rfm['M'] = pd.qcut(rfm['Monetary'], 4, labels=m_labels)


def assign_segment(row):
    if row['M'] >= 3 and row['F'] >= 3:
        return 'Champions'
    elif row['F'] >= 3 and row['R'] <= 2:
        return 'At-Risk'
    elif row['R'] <= 1 and row['F'] <= 1:
        return 'Lost'
    else:
        return 'Potential Loyalist'

rfm['Segment'] = rfm.apply(assign_segment, axis=1)
print("\nCustomer Segments Count:")
print(rfm['Segment'].value_counts())


# ==========================================
# STEP 5: VISUALIZE & EXPORT TO EXCEL
# ==========================================

segment_counts = rfm['Segment'].value_counts()

plt.figure(figsize=(8, 5))
segment_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Customer Segments Distribution')
plt.xlabel('Customer Segment')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

rfm.to_excel('ecommerce_rfm_analysis.xlsx', sheet_name='Customer_Segments')
print("\nSuccess File 'ecommerce_rfm_analysis.xlsx' ")