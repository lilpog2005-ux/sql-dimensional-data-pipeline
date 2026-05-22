# SQL Dimensional Data Pipeline

Automated ETL and dimensional data warehousing pipeline built using Python and SQL Server for business intelligence and analytical workflows.

## Project Overview

This project implements a dimensional data pipeline that automates:
- SQL Server database workflows
- ETL processing
- Dimensional table creation
- Logging and execution tracking
- Configuration-based pipeline execution
- Data warehouse preparation for analytics and dashboards

The project follows a modular data engineering structure with reusable utilities, testing, and workflow orchestration.


## Technologies Used

- Python
- SQL Server
- SQL
- Pytest
- ConfigParser
- Logging
- Pandas
- Git & GitHub

## Project Features

- Automated pipeline execution
- SQL script management
- Configurable SQL Server connections
- Logging system for pipeline monitoring
- Utility functions for reusable workflows
- Unit testing with pytest
- Dimensional data modeling structure
- Dashboard-ready analytical datasets


## Repository Structure

sql-dimensional-data-pipeline/
│
├── dashboard/
├── data/
├── infrastructure_initiation/
├── logs/
├── pipeline_dimensional_data/
├── tests/
├── logging_setup.py
├── main.py
├── sql_server_config.cfg
├── utils.py
└── README.md

## Workflow

1. Read configuration settings
2. Connect to SQL Server
3. Load and execute SQL scripts
4. Build dimensional tables
5. Log execution details
6. Prepare analytical outputs for dashboards

## Testing

The project includes unit tests for:
- SQL file reading
- Configuration parsing
- SQL formatting
- Execution ID generation
- Error handling validation


## Future Improvements

- Airflow pipeline orchestration
- Automated scheduling
- Cloud database integration
- Real-time ETL workflows
- Interactive dashboard deployment
