# Data Directory

## Primary Dataset

**File:** `AIID_Excel_Export-20261005.xlsx`  
**Source:** AI Incident Database (AIID)  
**Provider:** Responsible AI Collaborative  
**Snapshot date:** October 5, 2026  
**Download URL:** https://incidentdatabase.ai/research/snapshots  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

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

| Variable | Type | Fill Rate | Source Taxonomy | Description |
|---|---|---|---|---|
| Incident ID | Integer | 100% | AIID core | Unique identifier for each incident |
| Date | Date | 100% | AIID core | Editor-verified date the harm occurred |
| Year | Integer | 100% | Derived | Year extracted from Date for time series |
| Deployer | Text | 100% | AIID core | Organisation that deployed the AI system |
| Developer | Text | 100% | AIID core | Organisation that built the AI system |
| Harmed Parties | Text | 100% | AIID core | Groups or individuals who experienced harm |
| Risk Domain | Categorical | 87% | MIT taxonomy | High-level risk category |
| Risk Subdomain | Categorical | 87% | MIT taxonomy | Granular sub-category within Risk Domain |
| Intent | Categorical | 87% | MIT taxonomy | Intentional / Unintentional / Other |
| Responsible Entity | Categorical | 87% | MIT taxonomy | AI system / Human operator / Other |
| Timing | Categorical | 87% | MIT taxonomy | Pre-deployment / Post-deployment |
| Sector of Deployment | Categorical | 12% | CSETv1 | Industry sector (ISIC classification) |
| Autonomy Level | Categorical | 12% | CSETv1 | Degree of human oversight during operation |

---

## Notes on Missing Data

Variables sourced from the CSETv1 taxonomy (Sector of Deployment, Autonomy Level) have a fill rate of approximately 12%, covering roughly 205 of the 1,711 records. This is because the CSETv1 taxonomy was applied selectively to a subset of incidents. See `notebooks/00_data_exploration.ipynb` for the full missingness mechanism analysis and the imputation strategy applied in this study.

---

## How to Refresh the Dataset

If you want to use a more recent AIID snapshot:

1. Visit https://incidentdatabase.ai/research/snapshots
2. Download the latest Excel export
3. Replace `AIID_Excel_Export-20261005.xlsx` in this directory with the new file
4. Update the filename reference in `notebooks/00_data_exploration.ipynb` (cell 2, variable `DATA_FILE`)
