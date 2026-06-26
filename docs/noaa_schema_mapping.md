# NOAA AIS Schema Mapping

## Purpose

This document describes how NOAA AIS source fields are mapped into the project's canonical data model.

The objective is to normalize different data sources into a common schema before they are processed by the Silver layer.

## Source System

Source:

- NOAA AIS

Format:

- CSV / GeoParquet (depending on source)

Target Layer:

- bronze_ais_noaa

Target Model:

- Canonical AIS Schema

## Canonical Mapping

| NOAA Field | Canonical Field | Description |
|------------|-----------------|-------------|
| MMSI | vessel_id | Vessel unique identifier |
| BaseDateTime | event_timestamp | Event timestamp |
| LAT | latitude | Latitude |
| LON | longitude | Longitude |
| SOG | speed_knots | Speed over ground |
| COG | heading | Course over ground |

## Audit Metadata

The ingestion process enriches the incoming NOAA records with standard audit metadata:

- source_system
- ingestion_timestamp
- record_id

## Future Enhancements

Future versions will extend the canonical model with additional NOAA attributes including:

- Vessel Name
- IMO Number
- Vessel Type
- Cargo Type
- Vessel Dimensions
- Navigation Status