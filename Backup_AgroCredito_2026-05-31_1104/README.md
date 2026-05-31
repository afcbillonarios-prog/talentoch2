# AgroCredito Colombia - Seguridad Alimentaria 🌾

Plataforma de creditos rurales inteligentes con Inteligencia Artificial para garantizar la seguridad alimentaria de Colombia.

## Miembros del Equipo
- Andres
- Sebastian
- Julian
- Yuri

**Talento Tech 2**

## Caracteristicas

- Consulta de credito por cedula
- 7 sectores productivos (Agricultura, Ganaderia, Piscicultura, Porcicola, Avicultura, Energia Solar, Tecnologia Agricola)
- Simulador de creditos con tabla de amortizacion
- Graficos interactivos con Chart.js
- Modelo de Machine Learning (R2: 89.2%)

## Instalacion

```bash
pip install -r requirements.txt
python generate_data.py
python run_etl.py
python run_modeling.py
streamlit run app.py
```

## Archivos

- `app.py` - Aplicacion Streamlit
- `index.html` - Landing page
- `dashboard_avanzado.html` - Dashboard interactivo
- `generate_data.py` - Generador de datos
- `run_etl.py` - Pipeline ETL
- `run_modeling.py` - Entrenamiento del modelo
- `modelo_creditos.pkl` - Modelo serializado

## Licencia

MIT
