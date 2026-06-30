"""Helpers for lakehouse layer names."""

from maritime_traffic_intelligence_lakehouse.config import (
    BRONZE_SCHEMA,
    SILVER_SCHEMA,
    GOLD_SCHEMA,
)

def get_layers() -> dict[str, str]:
    """Return the main lakehouse layers"""
    return {
        "bronze": BRONZE_SCHEMA,
        "silver": SILVER_SCHEMA,
        "gold": GOLD_SCHEMA,
    }
