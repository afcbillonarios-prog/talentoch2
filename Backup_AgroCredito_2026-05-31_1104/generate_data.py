import os
import numpy as np
import pandas as pd

DEPARTAMENTOS = [
    "Antioquia", "Atlántico", "Bolívar", "Boyacá", "Caldas",
    "Cauca", "Cesar", "Córdoba", "Cundinamarca", "Chocó",
    "Huila", "La Guajira", "Magdalena", "Meta", "Nariño",
    "Norte de Santander", "Quindío", "Risaralda", "Santander",
    "Sucre", "Tolima", "Valle del Cauca", "Arauca", "Caquetá",
    "Guainía", "Guaviare", "Putumayo", "Vaupés", "Vichada"
]

SECTORES = [
    "Agricultura", "Ganadería", "Piscicultura", "Porcícola",
    "Avicultura", "Energía_Solar", "Tecnología_Agrícola"
]

PRODUCTOS_POR_SECTOR = {
    "Agricultura": ["Café", "Cacao", "Arroz", "Maíz", "Frutas", "Hortalizas", "Plátano", "Yuca", "Papa", "Cebolla"],
    "Ganadería": ["Leche", "Carne_Bovina", "Carne_Ovina", "Carne_Caprina", "Cuero"],
    "Piscicultura": ["Tilapia", "Trucha", "Camarón", "Pez_Libri", "Pez_Gato"],
    "Porcícola": ["Cerdo_Encaste", "Cerdo_Mestizo", "Lechón", "Chancho_Gordo"],
    "Avicultura": ["Pollo_Parrillero", "Huevo_Posterior", "Pavo", "Codorniz"],
    "Energía_Solar": ["Placa_Fotovoltaica", "Bomba_Solar", "Secador_Solar", "Iluminación_Solar"],
    "Tecnología_Agrícola": ["Riego_Goteo", "Drones_Agrícolas", "Sensores_Humedad", "Automatización_Invernadero"]
}

TECNOLOGIAS = [
    "Riego_Goteo", "Drones_Agrícolas", "Paneles_Solares", "Sensores_IoT",
    "Automatización_Invernadero", "Bomba_Solar", "GPS_Agrícola", "App_Monitoreo"
]

def generate_dataset():
    np.random.seed(42)
    n_samples = 2000

    cedulas = [f"{np.random.randint(10000000, 99999999)}" for _ in range(n_samples)]
    departamentos = np.random.choice(DEPARTAMENTOS, n_samples)
    sectores = np.random.choice(SECTORES, n_samples, p=[0.30, 0.20, 0.15, 0.10, 0.08, 0.07, 0.10])
    productos = [np.random.choice(PRODUCTOS_POR_SECTOR[s]) for s in sectores]

    edades = np.random.randint(18, 75, n_samples)
    experiencia = np.random.randint(0, 45, n_samples)
    hectareas = np.random.uniform(0.5, 50, n_samples).round(2)
    ingresos_mensuales = np.random.uniform(800000, 15000000, n_samples).round(0)

    monto_prestamo = np.random.uniform(5000000, 200000000, n_samples).round(0)
    plazo_meses = np.random.choice([12, 24, 36, 48, 60], n_samples)
    garantia = np.random.choice([0, 1], n_samples, p=[0.35, 0.65])
    subsidio = np.random.choice([0, 1], n_samples, p=[0.40, 0.60])

    tecnologia_count = np.random.randint(0, 5, n_samples)
    tiene_energia_solar = np.random.choice([0, 1], n_samples, p=[0.6, 0.4])
    tiene_riego = np.random.choice([0, 1], n_samples, p=[0.5, 0.5])

    produccion_anual_ton = np.random.uniform(1, 200, n_samples).round(2)
    exportaciones = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])

    tasa_base = 18.0
    tasa = (
        tasa_base
        - garantia * 3.2
        - subsidio * 5.5
        - experiencia * 0.06
        - (ingresos_mensuales / 1000000) * 0.3
        - tecnologia_count * 0.5
        - tiene_energia_solar * 1.0
        + (plazo_meses - 12) * 0.03
    )
    ruido = np.random.normal(0, 0.8, n_samples)
    tasa = (tasa + ruido).clip(6.0, 31.0).round(2)

    calificacion_credito = np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.05, 0.15, 0.30, 0.35, 0.15])

    aprobado = np.where(
        (calificacion_credito >= 3) & (tasa < 25) & (experiencia > 0),
        1, 0
    )

    mask_cedula = np.random.rand(n_samples) < 0.02
    mask_experiencia = np.random.rand(n_samples) < 0.025
    mask_garantia = np.random.rand(n_samples) < 0.015

    cedulas_arr = np.array(cedulas, dtype=object)
    cedulas_arr[mask_cedula] = np.nan

    df = pd.DataFrame({
        'Cedula': cedulas_arr,
        'Departamento': departamentos,
        'Sector_Productivo': sectores,
        'Producto': productos,
        'Edad': edades,
        'Experiencia_Anios': experiencia,
        'Hectareas': hectareas,
        'Ingresos_Mensuales_COP': ingresos_mensuales,
        'Monto_Prestamo_COP': monto_prestamo,
        'Plazo_Meses': plazo_meses,
        'Garantia_Respaldada': garantia,
        'Subsidio_Gobierno': subsidio,
        'Tecnologias_Usadas': tecnologia_count,
        'Tiene_Energia_Solar': tiene_energia_solar,
        'Tiene_Riego': tiene_riego,
        'Produccion_Anual_Ton': produccion_anual_ton,
        'Exporta_Productos': exportaciones,
        'Tasa_Interes_EA': tasa,
        'Calificacion_Credito': calificacion_credito,
        'Credito_Aprobado': aprobado
    })

    df.loc[mask_experiencia, 'Experiencia_Anios'] = np.nan
    df.loc[mask_garantia, 'Garantia_Respaldada'] = np.nan

    os.makedirs('data', exist_ok=True)
    df.to_csv('data/creditos_rurales.csv', index=False)
    print(f"Dataset creditos_rurales.csv generado: {len(df)} registros en 'data/'")

if __name__ == '__main__':
    generate_dataset()
