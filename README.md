Real-Time E-Commerce Lakehouse Platform
Overview

This project simulates a real-time e-commerce analytics platform built using Databricks, PySpark Structured Streaming, and Delta Lake.

The goal was to design and implement a modern Lakehouse architecture capable of processing streaming order data and transforming it into business-ready analytics using the Medallion Architecture (Bronze, Silver, and Gold layers).

Problem Statement

E-commerce businesses generate large volumes of transactional data every second. To support reporting and decision-making, this data must be ingested, cleaned, and transformed into meaningful business metrics.

This project demonstrates how streaming order events can be processed through a Lakehouse architecture to produce analytical datasets for revenue monitoring, customer analysis, payment tracking, and suspicious transaction detection.

Architecture

Streaming Source (Rate Source)
→ Bronze Layer (Raw Orders)
→ Silver Layer (Cleaned Orders)
→ Gold Layer (Business Analytics)

Gold tables include:

Revenue by Product
Payment Status Summary
Customer Spending Analysis
Suspicious Orders Detection
Technologies Used
Databricks
PySpark
Structured Streaming
Delta Lake
SQL
Git & GitHub
Medallion Architecture
Bronze Layer

Stores raw order events as they arrive from the streaming source.

Silver Layer

Applies data quality checks and transformations including:

Duplicate removal
Null handling
Data validation
Standardization
Gold Layer

Provides business-ready datasets used for reporting and analytics.

Business Insights Generated
Revenue by Product

Identifies products generating the highest revenue.

Payment Status Monitoring

Tracks paid, failed, and pending transactions.

Customer Spending Analysis

Identifies high-value customers and purchasing behavior.

Suspicious Order Detection

Flags unusually large transactions for further investigation.

Key Learnings

Through this project I gained hands-on experience with:

PySpark DataFrames and transformations
Structured Streaming concepts
Delta Lake storage and management
Medallion Architecture design
Building analytical data models in Databricks
