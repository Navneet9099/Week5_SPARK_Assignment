# Week 5 - Apache Spark Data Cleaning & DataFrame Operations

## 📌 Overview

This repository contains the solution for **Week 5 Assignment** on **Apache Spark**. The assignment focuses on understanding Spark fundamentals and performing data cleaning, filtering, transformation, aggregation, and schema modification using **PySpark DataFrames**.

The project demonstrates how Spark's in-memory processing enables efficient big data analytics compared to the traditional Hadoop MapReduce framework.

---

## 🎯 Objective

The main objectives of this assignment are:

- Understand the limitations of Hadoop MapReduce.
- Learn the advantages of Apache Spark and in-memory computing.
- Work with Spark DataFrames.
- Perform data cleaning operations.
- Apply filtering conditions.
- Handle null values and duplicate records.
- Perform aggregation and grouping operations.
- Modify DataFrame schema.
- Build an end-to-end Spark data processing pipeline.

---

## 🛠️ Technologies Used

- Python 3.x
- Apache Spark (PySpark)
- VS Code
- Java JDK 17

---

## 📂 Project Structure

```
Week5_Task_Spark/
│── asssignment.py
│── sales.csv
│── README.md
```

---

## 📊 Dataset

A sample **sales.csv** dataset was used containing information such as:

- User ID
- Transaction Date
- Region
- Product Category
- Sale Amount
- City
- Age
- Subscription
- Email
- Username
- Price
- Store ID
- Status
- Raw Timestamp

The dataset intentionally contains:

- Duplicate records
- Null values
- Empty values

to demonstrate Spark data cleaning techniques.

---

## 📖 Assignment Tasks

The assignment includes the following tasks:

- Understanding Spark vs MapReduce
- In-Memory Computing
- Removing duplicate records
- Filtering datasets
- Handling null values
- GroupBy and aggregation
- DataFrame immutability
- Schema modification
- Shuffle operations
- Data cleaning
- Building a complete Spark processing pipeline

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/Navneet9099/Week5_SPARK_Assignment.git
```

### Install PySpark

```bash
pip install pyspark
```

### Run the Program

```bash
python asssignment.py
```

---

## 📚 Spark Concepts Covered

- SparkSession
- DataFrames
- Transformations
- Actions
- Filtering
- dropDuplicates()
- groupBy()
- agg()
- count()
- sum()
- avg()
- min()
- max()
- withColumn()
- withColumnRenamed()
- cast()
- TimestampType
- Null Handling
- Data Cleaning
- Shuffle
- Wide Transformations

---

## 📈 Learning Outcomes

After completing this assignment, I learned:

- Why Spark is preferred over Hadoop MapReduce.
- How Spark uses in-memory processing to improve performance.
- Data cleaning techniques using PySpark.
- Working with DataFrame transformations and actions.
- Filtering and aggregation of large datasets.
- Schema modification and type casting.
- Understanding shuffle operations.
- Building complete ETL-style data processing pipelines.

---

## 📷 Sample Output

The project demonstrates:

- Duplicate removal
- Null value replacement
- Filtering datasets
- Aggregation using groupBy()
- Revenue calculation by Store ID
- Timestamp conversion
- Data cleaning pipeline

---

## 📌 Author

**Navneet Kesarwani**

B.Tech Computer Science Engineering

DIT University, Dehradun

---

## ⭐ Repository Purpose

This repository was created as part of the Week 5 Apache Spark assignment to demonstrate practical knowledge of PySpark DataFrame operations, data preprocessing, and distributed data processing concepts.
