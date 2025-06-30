# NYC Taxi Data Engineering  🚖📊

## 📝 Project Overview

This project demonstrates a **real-time data engineering pipeline** using **Azure Data Factory**, **Databricks (PySpark)**, **Delta Lake**, and **Azure Data Lake Storage Gen2**.

The pipeline **pulls data directly from the NYC Taxi API**, eliminating the need for manual file uploads. It transforms and organizes data using the **Medallion Architecture** (Bronze → Silver → Gold) and ensures data is **secure, optimized, and analytics-ready**.

---

## 🔗 Dataset Source

**NYC Taxi Trip Record Data**  
[NYC TLC Official Data Page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

## 🏗️ Architecture

The pipeline follows the **Medallion Architecture**:

| Layer     | Description |
|-----------|-------------|
| 🥉 **Bronze** | Raw data ingested from the API |
| 🥈 **Silver** | Cleaned and transformed data |
| 🥇 **Gold**   | Modeled data used for analytics/reporting |

---

## 📌 Architecture Diagram

![Architecture Diagram](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo.png)

---

## 🔄 End-to-End Flow

1. **API Integration**:
   - Pulls live data from the official NYC Taxi API.
   
2. **Ingestion (ADF)**:
   - **Dynamic & parameterized pipelines** ingest data into **Bronze Layer** in Parquet format.

3. **Transformation (Databricks & PySpark)**:
   - Cleansing and data modeling happens here.
   - Output saved in the **Silver Layer**.

4. **Serving (Delta Lake + Parquet)**:
   - Modeled data stored in the **Gold Layer**.
   - Delta Lake enables:
     - Time travel
     - Version control
     - ACID compliance

5. **Security**:
   - Azure Active Directory + Key Vault + RBAC for safe access.

---

## 💾 Storage Format

All layers use **Parquet** for efficient storage.  
**Gold Layer** uses **Delta Lake** for advanced features.

---

## 🔐 Security Implementation

| Feature          | Use Case |
|------------------|----------|
| Azure Active Directory | Identity & access management |
| Azure Key Vault         | Secret management |
| Role-Based Access Control (RBAC) | Restrict data layer access |

---

## ⚙️ Tools & Services

| Tool               | Purpose                          |
|--------------------|----------------------------------|
| Azure Data Factory | Orchestration & API ingestion    |
| Databricks + PySpark | Data transformation            |
| Azure Data Lake Gen2 | Storage across all layers       |
| Delta Lake         | Time travel, version control     |
| Azure Key Vault    | Secret management                |
| Azure Active Directory | Secure authentication       |

---

## 📚 Topics Covered

Throughout this project, the following key topics and concepts were explored:

- Introduction to Real-Time Data Engineering
- Designing Scalable Data Architecture
- Understanding the Medallion Architecture: Bronze, Silver, Gold Layers
- Azure Fundamentals and Account Setup
- Exploring and Understanding the NYC Taxi Dataset
- Creating Azure Resource Groups and Storage Accounts
- Setting up Azure Data Lake Storage Gen2
- Building Azure Data Factory Pipelines
- Ingesting Data from Public APIs using Azure Data Factory
- Real-Time Data Ingestion Scenarios in ADF
- Creating Dynamic & Parameterized Pipelines in ADF
- Accessing Azure Data Lake using Databricks
- Working with Databricks Clusters
- Reading Data Using PySpark
- Data Transformation Using PySpark Functions
- Data Analysis in PySpark
- Difference Between Managed and External Delta Tables
- Creating and Managing Delta Tables in Databricks
- Exploring Delta Log Files
- Querying Delta Tables with Versioning
- Time Travel in Delta Lake
- Connecting Databricks to Business Intelligence Tools

---

## 📸 Project Screenshots

Below are the real implementation screenshots taken directly from the live project:

### 🖥️ Pipeline & Monitoring

- **Image 1**
  ![Photo1](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo1.png)

- **Image 2**
  ![Photo2](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo2.png)

- **Image 3**
  ![Photo3](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo3.png)

- **Image 4**
  ![Photo4](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo4.png)

- **Image 5**
  ![Photo5](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo5.png)

- **Image 6**
  ![Photo6](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo6.png)

- **Image 7**
  ![Photo7](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo7.png)

- **Image 8**
  ![Photo8](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo8.png)

- **Image 9**
  ![Photo9](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo9.png)

- **Image 10**
  ![Photo10](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo10.png)

- **Image 11**
  ![Photo11](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo11.png)

- **Image 12**
  ![Photo12](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo12.png)

- **Image 13**
  ![Photo13](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo13.png)

- **Image 14**
  ![Photo14](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo14.png)

- **Image 15**
  ![Photo15](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo15.png)

- **Image 16**
  ![Photo16](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo16.png)

- **Image 17**
  ![Photo17](https://github.com/neha-dev-dot/NYC-TAXI/blob/main/Images/Photo17.png)

---

## 🎯 Outcome

By the end of this project, we:
- Built a fully automated, real-time pipeline
- Followed best practices using Medallion Architecture
- Integrated security and transformation at scale
- Created data ready for business intelligence tools

---

## 🚀 Future Scope

- Add Power BI/Looker Studio dashboards for visualization
- Schedule CI/CD deployment with Azure DevOps
- Integrate alerts using Azure Monitor & Log Analytics

---

> 💡 Built with ❤️ by **Neha Bharti**  

