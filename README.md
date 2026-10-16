# Proyecto de Analítica de Datos: Avance 3 - Visualización Profesional y Reproducibilidad

Este repositorio contiene el desarrollo del Avance 3 del proyecto, enfocado en elevar la calidad técnica de las visualizaciones del Avance 2 utilizando herramientas estáticas avanzadas, mapas geoespaciales e interactividad, cumpliendo además con los criterios de reproducibilidad.

---

## 🚀 Estructura del Repositorio

Para garantizar la reproducibilidad y el orden del proyecto completo, los archivos se distribuyen de la siguiente manera:

```text
├── data/               # Datasets originales (CSV, JSON, Shapefiles/GeoJSON)
├── notebooks/          # Notebooks de Jupyter (.ipynb) numerados secuencialmente
│   ├── 1_carga_y_limpieza.ipynb      # Consumo de APIs (requests) y normalización de texto
│   ├── 2_eda_exploratorio.ipynb       # Análisis exploratorio inicial (pandas, numpy)
│   └── 3_visualizaciones_finales.ipynb # Generación de mapas y gráficas avanzadas (matplotlib, geopandas)
├── dashboard/          # Archivo o enlace del componente de Business Intelligence (Power BI / Tableau)
├── README.md           # Este documento de presentación del proyecto
└── requirements.txt    # Archivo con las dependencias del entorno de Python
```

---

## 📊 1. Reconstrucción y Ampliación de Visualizaciones

### a) Visualización Estática y Geoespacial (GeoPandas + Matplotlib)
*Aquí debes colocar el nombre de tu mapa/gráfica (Ej: Mapa Coroplético de Ventas por Región)*

*   **Mejoras introducidas:** [Reemplaza con tu justificación de 3-4 líneas. Ejemplo: "Se transformaron los datos crudos en un mapa coroplético utilizando GeoPandas, aplicando una paleta de color secuencial continua adaptada para daltonismo. Se implementó 'unicodedata' para estandarizar los nombres de los estados y asegurar un cruce de datos limpio, además de usar 'StrMethodFormatter' en la barra de color para dar formato de moneda profesional a los ejes."]
*   **Captura de pantalla:**
    ![Visualización Estática o Mapa](https://placeholder.com)

### b) Visualización Interactiva 
*Aquí debes colocar el nombre de tu gráfica interactiva (Ej: Análisis de Dispersión Dinámico)*

*   **Funciones de interactividad:** Implementación de `hover` con tooltips detallados (información extra al pasar el cursor), herramientas de zoom y paneo por zonas.
*   **Aporte de la interactividad:** [Reemplaza con tu justificación. Ejemplo: "A diferencia de la versión estática que encimaba los nombres de las regiones, la interactividad resuelve la saturación visual permitiendo inspeccionar cada punto individualmente mediante ventanas emergentes (hover), facilitando la exploración de valores atípicos (outliers) de forma dinámica."]
*   **Captura de pantalla / Enlace:**
    ![Visualización Interactiva](https://placeholder.com)

---

## 💼 2. Componente en Herramienta de BI (Power BI / Tableau)

Se diseñó un componente analítico utilizando herramientas líderes de Business Intelligence para complementar los hallazgos del análisis en Python.

*   **Características del componente:** Incorporación de tarjetas de KPIs principales, segmentadores de fecha interactivos y paneles interactivos cruzados.
*   **Enlace público (Si aplica):** [Inserta el link a Tableau Public o Power BI Cloud aquí]
*   **Captura de pantalla:**
    ![Dashboard BI](https://placeholder.com)

---

## 📋 3. Documentación de Reproducibilidad

El flujo de trabajo fue diseñado para ser completamente reproducible de inicio a fin:

1.  **Origen y Consumo de Datos:** Los datos se consumen mediante la librería `requests` desde [Especificar API/URL Fuente] o se leen localmente desde la carpeta `/data`.
2.  **Limpieza de Texto:** Se utilizó `unicodedata` para remover acentos, diéresis y caracteres especiales, garantizando que el mapeo geoespacial no falle por discrepancias de texto.
3.  **Análisis Lineal:** Cada notebook está documentado internamente con celdas Markdown que explican las transformaciones críticas (tratamiento de nulos con `numpy`, agrupaciones con `pandas` y formateo con `matplotlib.ticker`).

---

## 🛠️ Instrucciones de Ejecución Local

1.  **Clonar este repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO>
    cd <NOMBRE_DE_TU_REPOSITORIO>
    ```
2.  **Crear un entorno virtual e instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Si usas Windows, se recomienda instalar GeoPandas mediante Conda o verificar la instalación de sus dependencias nativas como GDAL y Fiona).*
3.  **Ejecutar:** Abre tu entorno de Jupyter favorito y corre los notebooks dentro de la carpeta `/notebooks` en orden numérico.

