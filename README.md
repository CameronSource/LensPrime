# LensPrime
Author: Cameron Garner

## Overview

LensPrime is a guided SQL query generation platform designed to help users extract insights from data without requiring extensive SQL knowledge.

The long-term vision of LensPrime is to allow businesses and analysts to upload datasets, automatically detect table structures and relationships, answer business-focused questions through a guided interface, and generate executable SQL queries automatically.

Rather than functioning as a database hosting service, LensPrime acts as a temporary analysis workspace where users can import data, explore relationships, generate queries, and export results.

---

## Current Status

**Version:** Early Prototype (v0.01)

LensPrime is currently in active development and serves as a proof-of-concept demonstrating the core architecture required for future expansion.

Current functionality includes:

* Importing CSV files
* Creating a local SQLite workspace database
* Detecting tables and columns
* Detecting primary keys
* Detecting potential table relationships
* Generating SQL queries
* Executing SQL queries
* Displaying query results

Future versions will expand upon these capabilities with a user interface, dynamic query generation, advanced relationship detection, data editing tools, and business intelligence integrations.

---

## Software Tools Used

### Programming Language

* Python

### Database

* SQLite

### Libraries

* Pandas
* sqlite3
* pathlib

### Development Environment

* Visual Studio Code

### Version Control

* Git
* GitHub

---

## Project Structure

```text
LensPrime/
├── backend/
│   ├── import_csvs.py
│   ├── schema_detector.py
│   └── query_builder.py
│
├── database/
│   └── lensprime.db
│
├── docs/
│   ├── vision.md
│   ├── mvp.md
│   ├── roadmap.md
│   └── devlog.md
│
├── sample_data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
└── notes/
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
cd LensPrime
```

### 2. Install Dependencies

```bash
pip install pandas
```

### 3. Import CSV Files Into SQLite

Run:

```bash
python backend/import_csvs.py
```

This will:

* Read CSV files from the sample_data folder
* Create a SQLite database
* Create tables automatically
* Display detected tables and columns

### 4. Detect Schema Relationships

Run:

```bash
python backend/schema_detector.py
```

This will:

* Identify likely primary keys
* Identify likely relationships between tables
* Display discovered relationships

### 5. Generate and Execute Queries

Run:

```bash
python backend/query_builder.py
```

Choose one of the available business questions.

LensPrime will:

* Generate the SQL query
* Display the generated SQL
* Execute the query
* Display the results

---

## Long-Term Vision

LensPrime aims to bridge the gap between business users and SQL databases.

Many users understand the questions they want answered but do not possess the technical knowledge required to write SQL queries.

The long-term goal is to create a guided query generation system that allows users to:

1. Upload data
2. Confirm detected relationships
3. Select metrics and dimensions
4. Apply filters and sorting
5. Generate SQL automatically
6. Execute and export results

Example:

```text
Metric:
Total Sales

Group By:
State

Filter:
Customer Type = Retail

Sort:
Highest First

Limit:
10
```

LensPrime would then construct the appropriate SQL query automatically.

---

## Future Roadmap

### Phase 1

* CSV import
* SQLite workspace creation
* Relationship detection
* Query execution

### Phase 2

* Dynamic query builder
* Metric selection
* Grouping options
* Filtering options
* Sorting options
* Result limits

### Phase 3

* Graphical user interface
* Relationship editor
* Project saving
* Query history

### Phase 4

* Excel/XLSX imports
* Enhanced schema detection
* Data editing tools
* Export functionality

### Phase 5

* Power BI integration
* Tableau integration
* Advanced analytics features

---

## Project Goal

The primary goal of LensPrime is to reduce the technical barrier between business questions and data-driven answers.

Instead of requiring users to understand SQL syntax, LensPrime will guide users through a structured workflow and generate the necessary SQL automatically.

The vision is:

**Business Intent → Query Components → SQL → Results**

By focusing on business questions rather than SQL syntax, LensPrime aims to make data analysis more accessible, efficient, and intuitive.
