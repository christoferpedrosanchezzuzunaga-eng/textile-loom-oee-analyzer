"""Textile Loom OEE and Reliability Diagnostic Module"""
import sys
from tabulate import tabulate

def main():
    print("=" * 65)
    print("  TEXTILE LOOM OEE & PRODUCTION LOSS ANALYZER - CS50P")
    print("  Author: Christofer Sanchez (Industrial Engineering)")
    print("=" * 65)
    
    try:
        # 1. Inputs de OEE
        print("\n--- 1. Overall Equipment Effectiveness (OEE) Data ---")
        avail = float(input("Enter Availability [%] (0-100): "))
        perf = float(input("Enter Performance [%] (0-100): "))
        qual = float(input("Enter Quality [%] (0-100): "))
        
        oee_val, oee_status = calculate_oee(avail, perf, qual)
        
        # 2. Inputs de Confiabilidad
        print("\n--- 2. Reliability & Maintenance Metrics ---")
        operating_time = float(input("Total Operating Time [Hours]: "))
        downtime = float(input("Total Unplanned Downtime [Hours]: "))
        failures = int(input("Number of Breakdown Failures: "))
        
        mtbf, mttr = calculate_reliability(operating_time, downtime, failures)
        
        # 3. Inputs de Impacto Financiero
        print("\n--- 3. Financial Loss Parameters ---")
        cost_per_hour = float(input("Hourly Loom Inactivity Cost [USD/hr]: "))
        scrap_kg = float(input("Total Defective Fabric Scrap [kg]: "))
        cost_per_kg = float(input("Cost per kg of Defective Fabric [USD/kg]: "))
        
        total_loss, downtime_loss, scrap_loss = calculate_financial_loss(
            downtime, cost_per_hour, scrap_kg, cost_per_kg
        )
        
    except ValueError as e:
        sys.exit(f"Input Error: {e}")
    except KeyboardInterrupt:
        sys.exit("\nExecution cancelled by user.")

    # Presentación ejecutiva con tabulate
    summary_data = [
        ["Metric Category", "Calculated Metric", "Value", "Benchmark / Status"],
        ["OEE", "Composite OEE", f"{oee_val:.2f}%", oee_status],
        ["Reliability", "MTBF (Mean Time Between Failures)", f"{mtbf:.2f} hrs", "Target: >= 20 hrs"],
        ["Reliability", "MTTR (Mean Time to Repair)", f"{mttr:.2f} hrs", "Target: <= 1.0 hr"],
        ["Financial", "Downtime Cost", f"${downtime_loss:,.2f}", "Capacity Loss"],
        ["Financial", "Scrap Material Cost", f"${scrap_loss:,.2f}", "Defect Waste"],
        ["Financial", "TOTAL PRODUCTION LOSS", f"${total_loss:,.2f}", "Priority Bottleneck"]
    ]
    
    print("\n" + "=" * 65)
    print("  EXECUTIVE DIAGNOSTIC REPORT (TEXTILE WEAVING LINE)")
    print("=" * 65)
    print(tabulate(summary_data, headers="firstrow", tablefmt="grid"))
    print("\nAnalysis successfully completed.\n")


def calculate_oee(availability, performance, quality):
    """
    Calcula el OEE compuesto y determina su estatus operacional.
    Retorna (oee_porcentaje, estatus_str).
    """
    if not (0 <= availability <= 100 and 0 <= performance <= 100 and 0 <= quality <= 100):
        raise ValueError("Availability, Performance and Quality must be between 0 and 100")
        
    oee = (availability / 100) * (performance / 100) * (quality / 100) * 100
    
    if oee >= 85:
        status = "World Class (Optimal)"
    elif oee >= 65:
        status = "Acceptable (Standard)"
    else:
        status = "Critical (High Losses)"
        
    return round(oee, 2), status


def calculate_reliability(operating_hours, downtime_hours, failures_count):
    """
    Calcula MTBF y MTTR para una línea o máquina.
    Retorna (mtbf, mttr).
    """
    if operating_hours < 0 or downtime_hours < 0 or failures_count < 0:
        raise ValueError("Operating hours, downtime and failures count must be non-negative")
        
    if failures_count == 0:
        mtbf = float(operating_hours)
        mttr = 0.0
    else:
        mtbf = round(operating_hours / failures_count, 2)
        mttr = round(downtime_hours / failures_count, 2)
        
    return mtbf, mttr


def calculate_financial_loss(downtime_hours, cost_per_hour, scrap_kg, cost_per_kg):
    """
    Calcula el impacto económico por paradas y merma de tejido.
    Retorna (total_loss, downtime_loss, scrap_loss).
    """
    if downtime_hours < 0 or cost_per_hour < 0 or scrap_kg < 0 or cost_per_kg < 0:
        raise ValueError("Cost and quantity metrics must be non-negative")
        
    downtime_loss = round(downtime_hours * cost_per_hour, 2)
    scrap_loss = round(scrap_kg * cost_per_kg, 2)
    total_loss = round(downtime_loss + scrap_loss, 2)
    
    return total_loss, downtime_loss, scrap_loss


if __name__ == "__main__":
    main()
