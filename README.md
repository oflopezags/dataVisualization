# Proyecto de Analítica de Datos: Avance 3 - Visualización Profesional y Reproducibilidad

Este repositorio contiene el desarrollo del Avance 3 del proyecto, enfocado en elevar la calidad técnica de las visualizaciones del Avance 2 utilizando herramientas estáticas y dinámicas avanzadas, cumpliendo además con los criterios de reproducibilidad.

---

## 🚀 Estructura del Repositorio

Para garantizar la reproducibilidad y el orden del proyecto completo, los archivos se distribuyen de la siguiente manera:

```text
├── data/               # Datasets originales (CSV, JSON, Shapefiles/GeoJSON)
├── pys/          # Archivos python (.py) numerados secuencialmente
│   ├── 1_carga_y_limpieza.ipynb      # Consumo de APIs (requests) y normalización de texto
│   ├── 2_eda_exploratorio.ipynb       # Análisis exploratorio inicial (pandas, numpy)
│   └── 3_visualizaciones_finales.ipynb # Generación de  gráficas avanzadas (matplotlib, geopandas)
├── dashboard/          # Archivo o enlace del componente de Business Intelligence (Power BI / Tableau / Python streamlit)
├── README.md           # Este documento de presentación del proyecto
└── requirements.txt    # Archivo con las dependencias del entorno de Python
```

---

## 📊 1. Reconstrucción y Ampliación de Visualizaciones

### a) Visualización Estática 
*Distribución de la calificación final*

*   **Mejoras introducidas:** Respecto a la versión anterior, se mejoró la presentación mediante una paleta de colores
intencional que utiliza el azul para las categorías generales y el naranja para destacar las
calificaciones DD y DC. Se agregaron etiquetas con frecuencias y porcentajes, además de
una anotación que permite identificar rápidamente la concentración de estudiantes en
estas dos categorías. También mejoré el título, los nombres de los ejes para facilitar la
lectura. Estos cambios aplican los principios de contraste visual, jerarquía y claridad para
dirigir la atención hacia los resultados más relevantes sin distorsionar la información.
*   **Captura de pantalla:**
    ![Visualización Estática ](https://nose.com)

### b) Visualización Interactiva 
*Relación entre horas de estudio y rendimiento académico desagregada por sexo*

*   **Funciones de interactividad:** Implementación de `Filtros` .
*   **Aporte de la interactividad:** La interactividad aporta la posibilidad de explorar y comparar cómo se relacionan las horas
de estudio con el rendimiento académico según el sexo, algo que en la versión estática
requiere observar simultáneamente todos los grupos de la gráfica.
La interactividad mejora la comprensión de esta visualización al permitir seleccionar el sexo
del estudiante (femenino, masculino o ambos) y observar cómo cambia la distribución de
las calificaciones según las horas de estudio. A diferencia de la versión estática, el usuario
puede concentrarse en un grupo específico, comparar las medianas, la dispersión y los
posibles valores atípicos, así como consultar información de las observaciones
individuales. Esto facilita identificar patrones y diferencias entre grupos sin saturar la
visualización. Sin embargo, las diferencias observadas son descriptivas y no demuestran
por sí mismas que las horas de estudio causen un mejor rendimiento académico.
*   **Captura de pantalla / Enlace:**
    ![Visualización Interactiva](https://nose.com)

---

## 💼 2. Componente en Herramienta de BI (Power BI / Tableau)

Se diseñó un componente analítico utilizando herramientas líderes de Business Intelligence para complementar los hallazgos del análisis en Python.

*   **Características del componente:** pendiente.
*   **Enlace público (Si aplica):** pendiente
*   **Captura de pantalla:**
    ![Dashboard BI](https://nose.com)

---

## 📋 3. Documentación de Reproducibilidad

El flujo de trabajo fue diseñado para ser  reproducible :

1.  **Origen y Consumo de Datos:** Los datos se leen de  la carpeta `/data`.
2.  **Limpieza de Texto:** Se debe de asociar etiqueta de acuerdo al indice.
3.  **Análisis Lineal:** solo se generan las graficas a partir del archivo csv.

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
3.  **Ejecutar:** Abre tu entorno de python favorito y corre los notebooks dentro de la carpeta `/pys`  por tiempo no alcance a terminar todo como se debe. Importante para correr el los archivos de python, el archivo .csv debe de encontrarse en la misma carpeta donde se encuentre el .py .
2.  **Carpeta visualizaciones:** Esta carpeta esta el ejemplo de la herramienta dinámica.

