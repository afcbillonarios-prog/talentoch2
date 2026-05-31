import pandas as pd
import numpy as np
import os

def run_etl():
    print("Iniciando pipeline ETL...")
    df = pd.read_csv('data/creditos_rurales.csv')
    print(f"Dataset cargado: {len(df)} registros, {df.isnull().sum().sum()} nulos totales")

    nulos_antes = df.isnull().sum().sum()

    if 'Cedula' in df.columns:
        df['Cedula'] = df['Cedula'].fillna('SIN_CEDULA')

    if 'Experiencia_Anios' in df.columns:
        mediana_exp = df['Experiencia_Anios'].median()
        df['Experiencia_Anios'] = df['Experiencia_Anios'].fillna(mediana_exp)

    if 'Garantia_Respaldada' in df.columns:
        moda_gar = df['Garantia_Respaldada'].mode()[0]
        df['Garantia_Respaldada'] = df['Garantia_Respaldada'].fillna(moda_gar)

    df['Experiencia_Anios'] = df['Experiencia_Anios'].astype(int)
    df['Garantia_Respaldada'] = df['Garantia_Respaldada'].astype(int)
    df['Tiene_Energia_Solar'] = df['Tiene_Energia_Solar'].astype(int)
    df['Tiene_Riego'] = df['Tiene_Riego'].astype(int)
    df['Exporta_Productos'] = df['Exporta_Productos'].astype(int)
    df['Credito_Aprobado'] = df['Credito_Aprobado'].astype(int)

    df['Tasa_Interes_EA'] = df['Tasa_Interes_EA'].clip(6.0, 31.0)
    df['Monto_Prestamo_COP'] = df['Monto_Prestamo_COP'].clip(5000000, None)
    df['Edad'] = df['Edad'].clip(18, 75)

    nulos_despues = df.isnull().sum().sum()
    print(f"Nulos eliminados: {nulos_antes} -> {nulos_despues}")

    os.makedirs('data', exist_ok=True)
    df.to_csv('data/creditos_rurales_limpio.csv', index=False)
    print(f"Dataset limpio guardado: creditos_rurales_limpio.csv ({len(df)} registros)")

    return df

if __name__ == '__main__':
    run_etl()
