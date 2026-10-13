# Data Directory

## Primary Dataset

**File:** `AIID_Excel_Export-20261005.xlsx`  
**Source:** AI Incident Database (AIID)  
**Provider:** Responsible AI Collaborative  
**Snapshot date:** October 5, 2026  
**Download:** https://incidentdatabase.ai/research/snapshots  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

Download the Excel export from the official AIID snapshots page and place it in this folder as `AIID_Excel_Export-20261005.xlsx` (or update `DATA_FILE` in `notebooks/00_data_exploration.ipynb`).

### Required Attribution

> McGregor, S. (2021). Preventing repeated real world AI failures by cataloging incidents: The AI incident database. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(17), 15458-15463.

---

## Workbook Structure

| Sheet | Rows | Columns | Description |
|---|---|---|---|
| Incidents | 1,711 | 59 | Primary analytical table |
| Reports | 7,840 | 12 | Source articles linked to each incident |
| Entities | 7,410 | 2 | Organisations and individuals named in the database |
| Data Dictionary | 60 | varies | Column definitions and fill rates |
| Coverage Map | 7 | varies | Which taxonomy classified each incident |

---

## Key Variables Used in This Study

| Variable | Type | Units / Coding | Fill Rate | Source | Description |
|---|---|---|---|---|---|
| Incident ID | Integer | Count (ID) | 100% | AIID core | Unique identifier |
| Date | Date | Calendar date | 100% | AIID core | Date harm occurred |
| Year | Integer | Calendar year | 100% | Derived | Year for time series |
| Deployer | Text | Organisation name | 100% | AIID core | Deploying organisation |
| Developer | Text | Organisation name | 100% | AIID core | Building organisation |
| Harmed Parties | Text | Named party labels | 100% | AIID core | Parties harmed |
| Risk Domain | Categorical | MIT taxonomy codes | 87% | MIT | High-level risk category |
| Risk Subdomain | Categorical | MIT taxonomy codes | 87% | MIT | Sub-category |
| Intent | Categorical | Intentional / Unintentional / Other | 87% | MIT | Intent classification |
| Responsible Entity | Categorical | AI system / Human / Other | 87% | MIT | Who caused the risk |
| Timing | Categorical | Pre- / Post-deployment | 87% | MIT | When failure occurred |
| Sector of Deployment | Categorical | ISIC sector codes | 12% | CSETv1 | Industry sector |
| Autonomy Level | Categorical | CSETv1 autonomy codes | 12% | CSETv1 | Human oversight level |

---

## Missing Data

CSETv1 fields (Sector of Deployment, Autonomy Level) are ~12% filled because that taxonomy was applied selectively. See `notebooks/00_data_exploration.ipynb` for the missingness analysis used in this study.
