# Textile Loom OEE & Production Loss Analyzer

[![Harvard CS50P](https://img.shields.io/badge/Harvard%20University-CS50P%20Certified-A51C30?style=flat&logo=harvard&logoColor=white)](https://cs50.harvard.edu/certificates/6077b36a-3ab8-4802-8f90-1cba16c59783)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Test%20Suite-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-gray.svg?style=flat)](https://opensource.org/licenses/MIT)

Final engineering project for Harvard University's CS50 Introduction to Programming with Python (CS50P).  
Author: **Christofer Pedro Sánchez Zuzunaga** (Industrial Engineering, UPC).  
Credential verification: [Harvard Certificate ID 6077b36a-3ab8-4802-8f90-1cba16c59783](https://cs50.harvard.edu/certificates/6077b36a-3ab8-4802-8f90-1cba16c59783)  
Video demonstration: [YouTube Video Demo](https://youtu.be/8U4DbBvVXn8)

---

## Overview

The **Textile Loom OEE & Production Loss Analyzer** is a Python-based diagnostic system developed to calculate, benchmark, and quantify operational losses in manufacturing lines, specifically circular weaving textile looms.

In industrial textile manufacturing, unscheduled downtime, sub-optimal machine speed, and fabric defects represent significant financial losses. This tool provides deterministic metrics following World-Class Manufacturing (WCM) standards and formats an executive breakdown using `tabulate`.

---

## Mathematical Formulation & Engineering Modules

### 1. Overall Equipment Effectiveness (OEE) — `calculate_oee`
The composite OEE indicator is calculated as:

$$\text{OEE} = \text{Availability} \times \text{Performance} \times \text{Quality}$$

Where:
- Availability: ratio of operating time to planned production time.
- Performance: ratio of actual operating speed to ideal run rate.
- Quality: ratio of conforming output to total units produced.

Operational status classification:
- **World Class**: $\ge 85\%$ (International manufacturing benchmark).
- **Acceptable**: $65\% \text{ to } 84.9\%$ (Industry operational average).
- **Critical**: $< 65\%$ (Requires TPM and root-cause intervention).

Input domain constraints: all percentages must be bounded between $0$ and $100$. Out-of-range values raise a `ValueError`.

### 2. Equipment Reliability & Maintenance (TPM) — `calculate_reliability`
- **Mean Time Between Failures (MTBF)**:
  $$\text{MTBF} = \frac{\text{Operating Time}}{\text{Number of Failures}}$$
- **Mean Time to Repair (MTTR)**:
  $$\text{MTTR} = \frac{\text{Total Downtime}}{\text{Number of Failures}}$$

Edge case handling: When zero breakdowns occur during an observation window, MTBF is defined as total operating time, and MTTR defaults to zero.

### 3. Financial Loss Quantification — `calculate_financial_loss`
Translates technical parameters into direct financial impact:
- **Downtime Cost**:
  $$\text{Cost}_{\text{downtime}} = \text{Downtime Hours} \times \text{Loom Hourly Rate}$$
- **Scrap Material Cost**:
  $$\text{Cost}_{\text{scrap}} = \text{Defective Fabric (kg)} \times \text{Raw Material Unit Cost}$$
- **Total Operational Loss**:
  $$\text{Loss}_{\text{total}} = \text{Cost}_{\text{downtime}} + \text{Cost}_{\text{scrap}}$$

---

## Project Structure

```text
textile-loom-oee-analyzer/
├── project.py          # Core calculation logic and CLI interface
├── test_project.py     # Unit test suite verifying boundary conditions and exceptions
├── requirements.txt    # Project dependencies (tabulate, pytest)
├── .gitignore          # Environment and cache ignore rules
└── README.md           # Engineering documentation
```

---

## Setup and Execution

### Requirements
- Python 3.10 or higher
- `pip`

### Installation

```bash
git clone https://github.com/christoferpedrosanchezzuzunaga-eng/textile-loom-oee-analyzer.git
cd textile-loom-oee-analyzer
pip install -r requirements.txt
```

### Execution

Run the CLI analyzer:
```bash
python project.py
```

Run test suite:
```bash
pytest
```

---

## Technical Author & Academic Credentials

- **Christofer Pedro Sánchez Zuzunaga**
- Industrial Engineering student at Universidad Peruana de Ciencias Aplicadas (UPC).
- Harvard University CS50P Certified.
- Six Sigma Yellow Belt (SSYB™) & Scrum Fundamentals Certified (SFC™).
- GitHub: [@christoferpedrosanchezzuzunaga-eng](https://github.com/christoferpedrosanchezzuzunaga-eng)

## Citation & Academic Reference

If referencing this work in industrial case studies, cite as:

```text
Sánchez Zuzunaga, C. P. (2026). Textile Loom OEE and Production Loss Analyzer. Harvard CS50P.
```
