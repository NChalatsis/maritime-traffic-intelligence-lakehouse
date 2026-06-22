# Orchestration

Workflow order:
1. 00_generate_sample_data
2. 01_bronze_ingestion
3. 02_silver_transformation
4. 03_gold_metrics
5. 04_quality_checks

Dependencies:
- Silver depends on Bronze
- Gold depends on Silver
- Quality checks depend on Bronze/Silver/Gold