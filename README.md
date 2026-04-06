#  Prism Insurance Dashboard – Power BI Project

## 📊 Dashboard Link

*(https://app.powerbi.com/links/2ZlAM1wYDC?ctid=0ecde1b1-6118-4880-9c6b-491c76d96b71&pbi_source=linkShare&bookmarkGuid=12c470a4-f08f-49eb-939c-03682c70668e)*

---

## 📌 Problem Statement

This dashboard helps the insurance company better understand its customers, policies, and claims behavior. It enables stakeholders to analyze policy distribution, claim trends, and customer demographics effectively.

Through this dashboard, the company can:

* Identify high-claim areas and risky customer segments
* Monitor total premium vs. claims ratio
* Understand customer distribution by age, gender, and policy type
* Improve decision-making for pricing and risk management

---

## ⚙️ Steps Followed

### 🔹 Data Preparation

* Loaded dataset into Power BI Desktop (CSV/Excel format including policy, customer, and claims data)
* Opened Power Query Editor and enabled:

  * Column Distribution
  * Column Quality
  * Column Profile
* Set profiling to **“Based on entire dataset”**

### 🔹 Data Cleaning

* Handled missing/null values (e.g., Claim Amount, Premium)
* Removed duplicate records
* Ensured correct data types (Date, Currency, Whole Number, etc.)

### 🔹 Data Modeling

* Created relationships between tables:

  * Customers
  * Policies
  * Claims

### 🔹 Report Design

* Applied a suitable theme
* Added slicers for:

  * Policy Type
  * Gender
  * Region / Location
  * Claim Status

---

## 📈 Key Metrics (KPIs)

Created card visuals for:

* **Total Customers**
* **Total Policies**
* **Total Premium Collected**
* **Total Claims Amount**

---

## 📊 Visualizations

* Claims by Policy Type (Bar Chart)
* Customers by Age Group (Column Chart)
* Premium by Region
* Claim Status Distribution (Approved / Rejected / Pending)
* Monthly Claims Trend
* Policy Type Comparison

---

## 🧮 Calculations

### 🔸 Age Group (Calculated Column)

```DAX
Age Group = 
IF(Insurance[Age] <= 25, "0-25",
IF(Insurance[Age] <= 50, "25-50",
IF(Insurance[Age] <= 75, "50-75",
"75+")))
```

### 🔸 Measures

**Total Customers**

```DAX
Total Customers = COUNT(Insurance[CustomerID])
```

**Total Premium**

```DAX
Total Premium = SUM(Insurance[Premium Amount])
```

**Total Claims**

```DAX
Total Claims = SUM(Insurance[Claim Amount])
```

**Claim Ratio (%)**

```DAX
Claim Ratio = DIVIDE([Total Claims], [Total Premium]) * 100
```

---

## 🖼️ Dashboard Snapshots


*(https://github.com/user-attachments/assets/d222d92d-d304-4d96-a8cb-923da64163b8")*

---

## 🔍 Insights

### 📌 [1] Overall Metrics

* **Total Customers** 
* **Total Policies** 
* **Total Premium Collected** 
* **Total Claims** 

### 📌 [2] Claims Analysis

* Claim ratio shows how much premium is paid out as claims
* High claim ratio may indicate a risk-heavy portfolio
* Certain policy types show higher claim frequency

### 📌 [3] Customer Distribution

* Majority of customers belong to: *(add age group)*
* Gender distribution insight: *(add insight)*
* Region-wise distribution highlights key customer hubs

### 📌 [4] Policy Insights

* Most popular policy type: *(add value)*
* Least preferred policy type: *(add value)*
* Some policies generate significantly higher revenue

### 📌 [5] Risk & Business Insights

* High-claim regions require further investigation
* Certain customer segments show frequent claims
* Useful for improving underwriting and pricing strategies

---

## ✅ Conclusion

This Power BI dashboard provides a comprehensive overview of insurance operations, enabling stakeholders to:

* Monitor business performance
* Identify and reduce risks
* Improve profitability
* Enhance customer targeting and segmentation

---

## 🚀 Future Enhancements

* Add predictive analytics for claim forecasting
* Integrate real-time data sources
* Drill-through pages for detailed analysis
* Advanced segmentation using AI visuals

---

## 📎 Author

*(Yash Gundewadi)*

*LinkedIn:- (www.linkedin.com/in/yash-gundewadi-9b852b320)*

*Portfolio:- (https://github.com/yash-gundewadi)*

---
