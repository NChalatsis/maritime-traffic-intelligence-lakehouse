        `00_generate_sample_data`

                    │
                    ▼
            `bronze_ais_events`

                    │
                    ▼
        `02_silver_transformation`

                    │
            ┌───────┴────────────────┐
            ▼                        ▼
    `silver_ais_events`     `bronze_ais_rejects`

                    │
                    ▼
            `03_gold_metrics`

                    │
            ┌───────┴────────────────────┐
            ▼                            ▼
    `gold_traffic_daily`     `gold_speed_distribution`

                    │
                    ▼
            `04_quality_checks`
                    │
                    ▼
            `quality_summary`