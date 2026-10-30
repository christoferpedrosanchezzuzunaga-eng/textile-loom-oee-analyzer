# 🏭 Textile Loom OEE & Production Loss Analyzer

[![Harvard CS50P](https://img.shields.io/badge/Harvard%20University-CS50P%20Certified-A51C30?style=for-the-badge&logo=harvard&logoColor=white)](https://cs50.harvard.edu/certificates/6077b36a-3ab8-4802-8f90-1cba16c59783)
[![Python 3.12](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tested with Pytest](https://img.shields.io/badge/Tested%20with-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **Official Final Project for Harvard University's CS50’s Introduction to Programming with Python (CS50P).**  
> Developed by **Christofer Pedro Sánchez Zuzunaga** (Industrial Engineering, UPC).  
> 📜 **Verified Academic Credential:** [Harvard Certificate ID: 6077b36a-3ab8-4802-8f90-1cba16c59783](https://cs50.harvard.edu/certificates/6077b36a-3ab8-4802-8f90-1cba16c59783)  
> 📺 **Official Video Demo:** [Watch on YouTube](https://youtu.be/8U4DbBvVXn8)

---

## 📌 Overview

The **Textile Loom OEE & Production Loss Analyzer** is an industrial engineering diagnostic software built in Python to evaluate, benchmark, and financially quantify operational inefficiencies in textile manufacturing plants, with a specialized focus on circular weaving textile looms.

In industrial textile operations, unplanned downtime, speed bottlenecks, and fabric defects cause massive economic leaks. Many manufacturing plants fail to spot root causes due to fragmented records. This computational tool bridges the gap by processing plant parameters, evaluating standardized World-Class Manufacturing (WCM) indicators, and generating an executive financial diagnostic formatted with 	abulate.

---

## ⚙️ Core Engineering Modules

### 1. Overall Equipment Effectiveness (OEE) — calculate_oee
- Computes composite OEE across the three fundamental industrial pillars:
  \text{OEE} = \text{Availability} \times \text{Performance} \times \text{Quality}
- Benchmarks operational health against international World-Class standards:
  - 🟢 **World Class:** $\ge 85\%$ (Global competitive benchmark).
  - 🟡 **Acceptable:** \% - 84.9\%$ (Industrial operational average).
  - 🔴 **Critical:** $< 65\%$ (Bottlenecks requiring immediate TPM / Lean intervention).
- Validates strict boundary conditions $, throwing handled ValueError exceptions for abnormal sensor or manual inputs.

### 2. Maintenance Reliability Metrics (TPM) — calculate_reliability
- **MTBF (Mean Time Between Failures):** Measures operational reliability by dividing net operating uptime by failure events.
- **MTTR (Mean Time to Repair):** Measures maintainability and technician response time by dividing downtime hours by incident counts.
- Implements zero-division protection safeguards for zero-failure continuous production runs.

### 3. Financial Loss Quantification — calculate_financial_loss
- Monetizes technical downtime by multiplying idle machine hours by hourly loom depreciation and direct labor cost.
- Monetizes scrap waste by multiplying defective fabric kilograms by unit raw material cost.
- Delivers an aggregated financial impact report, translating engineering metrics directly into executive P&L decision numbers.

---

## 📁 Repository Structure

`	ext
textile-loom-oee-analyzer/
│
├── project.py          # Central program logic & core engineering calculation functions
├── test_project.py     # Unit test suite verifying edge cases, zero-division & exceptions with Pytest
├── requirements.txt    # Production dependencies (tabulate, pytest)
├── README.md           # Engineering documentation and Harvard verification details
└── .gitignore          # Environment & cache exclusion rules
`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip package manager

### Installation & Execution

1. **Clone this repository:**
   `ash
   git clone https://github.com/christoferpedrosanchezzuzunaga-eng/textile-loom-oee-analyzer.git
   cd textile-loom-oee-analyzer
   `

2. **Install dependencies:**
   `ash
   pip install -r requirements.txt
   `

3. **Run the analyzer:**
   `ash
   python project.py
   `

4. **Run the comprehensive unit test suite:**
   `ash
   pytest
   `

---

## 👨‍💻 Author & Academic Verification

**Christofer Pedro Sánchez Zuzunaga**  
- Industrial Engineering Student — Universidad Peruana de Ciencias Aplicadas (UPC).
- Harvard University CS50P Certified.
- Six Sigma Yellow Belt (SSYB™) & Scrum Fundamentals Certified (SFC™).
- GitHub: [@christoferpedrosanchezzuzunaga-eng](https://github.com/christoferpedrosanchezzuzunaga-eng)
