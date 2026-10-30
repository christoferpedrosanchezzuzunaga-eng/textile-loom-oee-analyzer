import pytest
from project import calculate_oee, calculate_reliability, calculate_financial_loss

def test_calculate_oee():
    # Caso 1: Caso real planta textil (Línea base La Parcela)
    oee, status = calculate_oee(62.4, 82.1, 91.3)
    assert oee == 46.77
    assert status == "Critical (High Losses)"
    
    # Caso 2: Clase mundial
    oee_wc, status_wc = calculate_oee(90.0, 95.0, 99.5)
    assert oee_wc == 85.07
    assert status_wc == "World Class (Optimal)"
    
    # Caso 3: Aceptable
    oee_std, status_std = calculate_oee(80.0, 85.0, 96.0)
    assert oee_std == 65.28
    assert status_std == "Acceptable (Standard)"
    
    # Excepciones: porcentajes fuera de rango
    with pytest.raises(ValueError):
        calculate_oee(-5, 80, 90)
    with pytest.raises(ValueError):
        calculate_oee(105, 80, 90)
    with pytest.raises(ValueError):
        calculate_oee(80, -10, 90)


def test_calculate_reliability():
    # Caso 1: Con fallas
    mtbf, mttr = calculate_reliability(100.0, 20.0, 4)
    assert mtbf == 25.0
    assert mttr == 5.0
    
    # Caso 2: Cero fallas (evita división por cero)
    mtbf_zero, mttr_zero = calculate_reliability(120.0, 0.0, 0)
    assert mtbf_zero == 120.0
    assert mttr_zero == 0.0
    
    # Excepciones: valores negativos
    with pytest.raises(ValueError):
        calculate_reliability(-10, 5, 2)
    with pytest.raises(ValueError):
        calculate_reliability(100, -2, 2)
    with pytest.raises(ValueError):
        calculate_reliability(100, 5, -1)


def test_calculate_financial_loss():
    # Caso 1: Cálculo estándar
    total, downtime_loss, scrap_loss = calculate_financial_loss(20.0, 50.0, 30.0, 12.0)
    assert downtime_loss == 1000.0
    assert scrap_loss == 360.0
    assert total == 1360.0
    
    # Caso 2: Cero paradas y cero merma
    total_zero, dt_zero, scrap_zero = calculate_financial_loss(0.0, 50.0, 0.0, 12.0)
    assert total_zero == 0.0
    assert dt_zero == 0.0
    assert scrap_zero == 0.0
    
    # Excepciones: valores negativos
    with pytest.raises(ValueError):
        calculate_financial_loss(-5, 50, 10, 10)
    with pytest.raises(ValueError):
        calculate_financial_loss(10, -50, 10, 10)
    with pytest.raises(ValueError):
        calculate_financial_loss(10, 50, -10, 10)
