import joblib
import pandas as pd
import numpy as np

def predecir_tasa_credito(
    edad,
    experiencia_anios,
    hectareas,
    ingresos_mensuales_cop,
    monto_prestamo_cop,
    plazo_meses,
    garantia_respaldada,
    subsidio_gobierno,
    tecnologias_usadas,
    tiene_energia_solar,
    tiene_riego,
    model_path='modelo_creditos.pkl'
):
    """
    Carga el modelo de regresión lineal y calcula la tasa de interés E.A. estimada
    para un crédito rural colombiano.
    """
    try:
        data = joblib.load(model_path)
        modelo_cargado = data['modelo']
        columnas = data['caracteristicas']

        input_data = pd.DataFrame([{
            'Edad': edad,
            'Experiencia_Anios': experiencia_anios,
            'Hectareas': hectareas,
            'Ingresos_Mensuales_COP': ingresos_mensuales_cop,
            'Monto_Prestamo_COP': monto_prestamo_cop,
            'Plazo_Meses': plazo_meses,
            'Garantia_Respaldada': garantia_respaldada,
            'Subsidio_Gobierno': subsidio_gobierno,
            'Tecnologias_Usadas': tecnologias_usadas,
            'Tiene_Energia_Solar': tiene_energia_solar,
            'Tiene_Riego': tiene_riego
        }], columns=columnas)

        tasa_predicha = modelo_cargado.predict(input_data)[0]
        tasa_final = np.clip(tasa_predicha, 6.0, 31.0)

        return round(float(tasa_final), 2)
    except Exception as e:
        print(f"Error al predecir tasa: {e}")
        return None

def calcular_cuota(monto, tasa_ea, plazo_meses):
    """Calcula cuota mensual usando sistema francés."""
    tasa_mensual = (1 + tasa_ea / 100) ** (1 / 12) - 1
    if tasa_mensual > 0:
        cuota = monto * (tasa_mensual * (1 + tasa_mensual) ** plazo_meses) / ((1 + tasa_mensual) ** plazo_meses - 1)
    else:
        cuota = monto / plazo_meses
    return round(cuota, 0)

def generar_tabla_amortizacion(monto, tasa_ea, plazo_meses):
    """Genera tabla de amortización mes a mes."""
    tasa_mensual = (1 + tasa_ea / 100) ** (1 / 12) - 1
    cuota = calcular_cuota(monto, tasa_ea, plazo_meses)
    saldo = monto
    tabla = []
    for mes in range(1, plazo_meses + 1):
        int_mes = saldo * tasa_mensual
        capital = cuota - int_mes
        saldo -= capital
        if saldo < 0:
            saldo = 0
        tabla.append({
            'Mes': mes,
            'Cuota': round(cuota, 0),
            'Capital': round(capital, 0),
            'Interes': round(int_mes, 0),
            'Saldo': round(saldo, 0)
        })
    return pd.DataFrame(tabla)
