import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os

def run_modeling():
    print("Iniciando pipeline de modelado...")
    df = pd.read_csv('data/creditos_rurales_limpio.csv')
    print(f"Dataset cargado: {len(df)} registros")

    features = [
        'Edad', 'Experiencia_Anios', 'Hectareas', 'Ingresos_Mensuales_COP',
        'Monto_Prestamo_COP', 'Plazo_Meses', 'Garantia_Respaldada',
        'Subsidio_Gobierno', 'Tecnologias_Usadas', 'Tiene_Energia_Solar',
        'Tiene_Riego'
    ]

    X = df[features].copy()
    y = df['Tasa_Interes_EA'].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"Entrenamiento: {len(X_train)} | Prueba: {len(X_test)}")

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(f"R2: {r2:.4f} ({r2*100:.2f}%)")
    print(f"MAE: {mae:.4f} puntos porcentuales")
    print(f"RMSE: {rmse:.4f}")

    coef_dict = dict(zip(features, modelo.coef_))
    print("\nCoeficientes del modelo:")
    for feat, coef in coef_dict.items():
        print(f"  {feat}: {coef:.6f}")
    print(f"  Intercepto: {modelo.intercept_:.6f}")

    model_data = {
        'modelo': modelo,
        'caracteristicas': features,
        'coeficientes': coef_dict,
        'intercepto': modelo.intercept_,
        'metricas': {'r2': r2, 'mae': mae, 'rmse': rmse}
    }

    joblib.dump(model_data, 'modelo_creditos.pkl')
    print("\nModelo guardado: modelo_creditos.pkl")

    return modelo, features, coef_dict

if __name__ == '__main__':
    run_modeling()
