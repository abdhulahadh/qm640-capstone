# QM 640 – Data Analytics Capstone

**Course:** QM 640 – Data Analytics Capstone  
**Institution:** Walsh College  
**Term:** Fall 2026 (Third Term)  
**Author:** Abdhul Ahadh  
**Instructor:** Professor Sharath Srivatsa  

---

## Project Title

**Governing Enterprise AI Adoption: A Data-Driven Analysis of Failure Patterns and Risk in Revenue-Generating Operations**

---

## Overview

This repository contains all data, analysis code, and documentation for the QM 640 capstone project. The study applies statistical and machine learning methods to the AI Incident Database (AIID) to identify failure patterns in enterprise AI deployments and evaluate the impact of regulatory interventions.

Four research questions are investigated:

| # | Research Question | Method |
|---|---|---|
| RQ1 | Do enterprise-deployed AI incidents differ in risk domain distributions from non-enterprise incidents? | Chi-square / Fisher's exact test |
| RQ2 | Can risk domain, deployer type, and intent predict high-severity incident outcomes? | Logistic Regression + Random Forest |
| RQ3 | Did regulatory milestones (EU AI Act 2021, U.S. EO 2023) measurably change enterprise incident rates? | Interrupted Time Series (Segmented Regression) |
| RQ4 | What natural clusters emerge from incident data, and do they map to the NIST AI RMF? | K-Means + Hierarchical Clustering |

---

## Repository Structure

```
qm640-capstone/
│
├── data/
│   ├── AIID_Excel_Export-20261005.xlsx   # Primary dataset (AIID snapshot, Oct 5 2026)
│   └── README.md                         # Data provenance, license, and variable notes
│
├── notebooks/
│   ├── 00_data_exploration.ipynb         # Initial EDA and fill-rate audit
│   ├── 01_rq1_chisquare.ipynb            # RQ1: Chi-square test of independence
│   ├── 02_rq2_severity_model.ipynb       # RQ2: Logistic regression + Random Forest
│   ├── 03_rq3_interrupted_ts.ipynb       # RQ3: Interrupted time series analysis
│   └── 04_rq4_clustering.ipynb           # RQ4: K-Means and hierarchical clustering
│
├── outputs/
│   └── figures/                          # All saved charts and visualisations
│
├── requirements.txt                      # Python library versions
├── LICENSE                               # MIT License
└── README.md                             # This file
```

---

## Dataset

**Source:** AI Incident Database (AIID)  
**Maintained by:** Responsible AI Collaborative (non-profit)  
**Snapshot date:** October 5, 2026  
**Direct download:** https://incidentdatabase.ai/research/snapshots  
**Records:** 1,711 incidents across 59 variables  
**Taxonomies:** MIT AI Risk taxonomy, GMF taxonomy, CSETv1 taxonomy  

See [`data/README.md`](data/README.md) for full variable definitions, fill rates, and licensing details.

---

## Setup and Reproduction

### Requirements

- Python 3.11 or later
- Jupyter Notebook or JupyterLab

### Installation

```bash
# Clone the repository
git clone https://github.com/abdhulahadh/qm640-capstone.git
cd qm640-capstone

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis

Open Jupyter and run notebooks in order:

```bash
jupyter notebook
```

Start with `notebooks/00_data_exploration.ipynb` and proceed through `01` to `04`. Each notebook is self-contained and loads the dataset from the `data/` directory using a relative path.

---

## Citation

If you reference this work, please cite:

```
Ahadh, A. (2026). Governing enterprise AI adoption: a data-driven analysis of failure
patterns and risk in revenue-generating operations [Capstone project].
Walsh College, QM 640 Data Analytics Capstone.
https://github.com/abdhulahadh/qm640-capstone
```

---

## License

Code in this repository is released under the [MIT License](LICENSE).  
The AIID dataset is provided by the Responsible AI Collaborative under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/). Attribution: McGregor, S. (2021). Preventing repeated real world AI failures by cataloging incidents. *AAAI 2021*.
