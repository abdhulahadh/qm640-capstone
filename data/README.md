# Data Directory

## Primary Dataset

**File:** `AIID_Excel_Export-20261005.xlsx`  
**Source:** AI Incident Database (AIID)  
**Provider:** Responsible AI Collaborative  
**Snapshot date:** October 5, 2026  
**Official download URL:** https://incidentdatabase.ai/research/snapshots  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

The Excel snapshot used in this capstone is intended to live in this folder so the repository is fully reproducible from a single clone. If the binary is not yet present on your checkout, download the matching export from the official AIID snapshots page above and place it here with the same filename.

### Required Attribution

> McGregor, S. (2021). Preventing repeated real world AI failures by cataloging incidents: The AI incident database. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(17), 15458-15463.

---

## Workbook Structure

The Excel file contains five sheets:

| Sheet | Rows | Columns | Description |
|---|---|---|---|
| Incidents | 1,711 | 59 | Primary analytical table. One row per documented AI incident. |
| Reports | 7,840 | 12 | Source articles and documents linked to each incident. |
| Entities | 7,410 | 2 | Normalised list of all organisations and individuals named in the database. |
| Data Dictionary | 60 | varies | Column-level definitions, fill rates, and taxonomy sources for the Incidents sheet. |
| Coverage Map | 7 | varies | Describes which taxonomy (MIT, GMF, CSETv1) has classified each incident. |

---

## Key Variables Used in This Study

| Variable | Type | Units / Coding | Fill Rate | Source Taxonomy | Description |
|---|---|---|---|---|---|
| Incident ID | Integer | Count (ID) | 100% | AIID core | Unique identifier for each incident |
| Date | Date | Calendar date | 100% | AIID core | Editor-verified date the harm occurred |
| Year | Integer | Calendar year | 100% | Derived | Year extracted from Date for time series |
| Deployer | Text | Organisation name | 100% | AIID core | Organisation that deployed the AI system |
| Developer | Text | Organisation name | 100% | AIID core | Organisation that built the AI system |
| Harmed Parties | Text | Named party labels | 100% | AIID core | Groups or individuals who experienced harm |
| Risk Domain | Categorical | MIT taxonomy codes | 87% | MIT taxonomy | High-level risk category |
| Risk Subdomain | Categorical | MIT taxonomy codes | 87% | MIT taxonomy | Granular sub-category within Risk Domain |
| Intent | Categorical | Intentional / Unintentional / Other | 87% | MIT taxonomy | Intent classification |
| Responsible Entity | Categorical | AI system / Human / Other | 87% | MIT taxonomy | Who caused the risk |
| Timing | Categorical | Pre- / Post-deployment | 87% | MIT taxonomy | When the failure occurred |
| Sector of Deployment | Categorical | ISIC sector codes | 12% | CSETv1 | Industry sector |
| Autonomy Level | Categorical | CSETv1 autonomy codes | 12% | CSETv1 | Degree of human oversight |

---

## Notes on Missing Data

Variables sourced from the CSETv1 taxonomy (Sector of Deployment, Autonomy Level) have a fill rate of approximately 12%, covering roughly 205 of the 1,711 records. This is because the CSETv1 taxonomy was applied selectively to a subset of incidents. See `notebooks/00_data_exploration.ipynb` for the missingness mechanism analysis and the imputation strategy used in this study.

---

## How to Refresh the Dataset

1. Visit https://incidentdatabase.ai/research/snapshots
2. Download the latest Excel export
3. Replace `AIID_Excel_Export-20261005.xlsx` in this directory (or update the filename)
4. Update the filename reference in `notebooks/00_data_exploration.ipynb` (variable `DATA_FILE`)
