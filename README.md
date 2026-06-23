# maritime-traffic-intelligence-lakehouse

## Overview
An end-to-end lakehouse solution for maritime traffic analytics, transforming vessel movement data into trusted analytical datasets and operational insights using Databricks, PySpark and Delta Lake.
## Business Problem
Maritime traffic generates large volumes of vessel movement data that must be ingested, validated and transformed before it can be used for operational reporting and analytics.

The objective of this project is to build a scalable data pipeline capable of processing vessel movement events, applying data quality controls, and serving business-ready datasets for traffic monitoring, congestion analysis and operational reporting.
## Architecture
This project follows the Medallion Architecture pattern:

Raw Events

        ↓
Bronze Layer

        ↓
Silver Layer

        ↓
Reject Records

        ↓
Gold Layer
## Data Model

### Bronze Layer
Stores raw AIS-like vessel events enriched with audit metadata.

Main table:
`bronze_ais_events`

Metadata columns:

- source_system
- ingestion_timestamp
- record_id
### Silver Layer
Applies data quality validations and business transformations.

Main table:
`silver_ais_events`

Transformations:

Geographic coordinate validation
- Duplicate handling
- Event date extraction
- Event hour extraction
- Speed categorization
- Movement flag generation

Invalid records are redirected to:
`bronze_ais_rejects`
### Gold Layer
Provides business-ready datasets and aggregated metrics.

Main tables:
`gold_traffic_daily`
`gold_speed_distribution`

Examples of generated metrics:

- Daily vessel activity
- Unique vessel counts
- Average vessel speed
- Speed category distribution
- Moving vs stationary vessel events
## Data Quality Framework
The pipeline validates incoming records and separates invalid data into a dedicated reject table.

Current validation rules include:

- Invalid latitude detection
- Invalid longitude detection
- Missing vessel identifiers
- Missing event timestamps

Quality monitoring output:

- Bronze record count
- Silver record count
- Reject record count
- Gold record count
- Reject percentage

Example run:

- Bronze records: 50,000
- Silver records: 49,010
- Rejected records: 990
- Reject rate: 1.98%
## Workflow Orchestration
The pipeline is orchestrated using Databricks Jobs.

Execution flow:

1. Generate Sample Data
2. Bronze Processing
3. Silver Transformation
4. Gold Aggregations
5. Quality Checks
## Technologies Used
- Databricks
- PySpark
- Delta Lake
- GitHub
- Databricks Workflows
## Project Structure

## How to Run

## Sample Results

## Future Enhancements
- Real NOAA AIS data ingestion
- Weather data enrichment
- Incremental processing
- Partition optimization
- Monitoring dashboards
- Advanced traffic and congestion analytics