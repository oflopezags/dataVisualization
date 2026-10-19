
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# --------------------------------------------------
# 1. Configuración visual
# --------------------------------------------------
sns.set_theme(
    style="whitegrid",
    font="DejaVu Sans",
    rc={
        "axes.titlesize": 16,
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "grid.color": "#E5E7EB",
        "grid.linewidth": 0.8,
    }
)

# Paleta intencional: azul general y naranja para destacar
COLOR_GENERAL = "#4472A8"
COLOR_DESTACADO = "#E87524"
COLOR_TEXTO = "#263238"
COLOR_SECUNDARIO = "#596579"

# --------------------------------------------------
# 2. Cargar el archivo CSV
# --------------------------------------------------
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "DATA (1).csv"

df = pd.read_csv(csv_path)

# --------------------------------------------------
# 3. Mapear las variables
# --------------------------------------------------
grade_map = {
    0: "Fail (0)",
    1: "DD (1)",
    2: "DC (2)",
    3: "CC (3)",
    4: "CB (4)",
    5: "BB (5)",
    6: "BA (6)",
    7: "AA (7)"
}

study_map = {
    1: "Ninguna",
    2: "<5 horas",
    3: "6-10 horas",
    4: "11-20 horas",
    5: ">20 horas"
}

scholarship_map = {
    1: "Ninguna (0%)",
    2: "25%",
    3: "50%",
    4: "75%",
    5: "Completa (100%)"
}

sex_map = {
    1: "Femenino",
    2: "Masculino"
}

df["Calificacion"] = df["GRADE"].map(grade_map)
df["Horas_Estudio"] = df["17"].map(study_map)
df["Tipo_Beca"] = df["4"].map(scholarship_map)
df["Sexo"] = df["2"].map(sex_map)

# --------------------------------------------------
# 4. Calcular frecuencias y porcentajes
# --------------------------------------------------
grade_order = [
    "Fail (0)", "DD (1)", "DC (2)", "CC (3)",
    "CB (4)", "BB (5)", "BA (6)", "AA (7)"
]

counts = (
    df["Calificacion"]
    .value_counts()
    .reindex(grade_order, fill_value=0)
)

total_calificados = counts.sum()

if total_calificados == 0:
    raise ValueError("No se encontraron calificaciones válidas.")

pcts = counts / total_calificados * 100

# Porcentaje conjunto de DD y DC
low_grades = ["DD (1)", "DC (2)"]
low_count = counts.loc[low_grades].sum()
low_pct = low_count / total_calificados * 100

print(f"Estudiantes en el archivo: {len(df)}")
print(f"Estudiantes con calificación válida: {total_calificados}")
print(f"Estudiantes con DD o DC: {low_count} ({low_pct:.1f}%)")

# --------------------------------------------------
# 5. Crear la gráfica
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7))

# Destacar DD y DC en naranja; el resto en azul
colors = [
    COLOR_DESTACADO if grade in low_grades else COLOR_GENERAL
    for grade in grade_order
]

bars = ax.bar(
    grade_order,
    counts.values,
    color=colors,
    edgecolor="white",
    linewidth=1.2,
    width=0.68,
    zorder=3
)

# Etiquetas de frecuencia y porcentaje
for bar, count, pct in zip(bars, counts.values, pcts.values):
    if count == 0:
        continue

    ax.annotate(
        f"{count}\n({pct:.1f}%)",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 7),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color=COLOR_TEXTO
    )

# --------------------------------------------------
# 6. Anotación del resultado principal
# --------------------------------------------------
# Ubicar la anotación por encima de las barras destacadas
dd_index = grade_order.index("DD (1)")
dc_index = grade_order.index("DC (2)")

dd_center = bars[dd_index].get_x() + bars[dd_index].get_width() / 2
dc_center = bars[dc_index].get_x() + bars[dc_index].get_width() / 2

target_x = (dd_center + dc_center) / 2
target_y = max(counts.loc[low_grades])

annotation_y = max(counts.max() + 5, total_calificados * 0.30)

ax.annotate(
    f"DD y DC concentran\n{low_count} estudiantes ({low_pct:.1f}%)",
    xy=(target_x, target_y),
    xytext=(4.7, annotation_y),
    textcoords="data",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
    color="#A84408",
    bbox=dict(
        boxstyle="round,pad=0.55",
        facecolor="#FFF3E8",
        edgecolor=COLOR_DESTACADO,
        linewidth=1.5
    ),
    arrowprops=dict(
        arrowstyle="->",
        color=COLOR_DESTACADO,
        linewidth=1.5,
        connectionstyle="arc3,rad=0.12"
    ),
    zorder=5
)

# --------------------------------------------------
# 7. Título, ejes y formato final
# --------------------------------------------------
fig.suptitle(
    "Distribución de las calificaciones finales",
    fontsize=17,
    fontweight="bold",
    color=COLOR_TEXTO,
    y=0.97
)

ax.set_title(
    f"Frecuencia y porcentaje de estudiantes (n = {total_calificados})",
    fontsize=11,
    color=COLOR_SECUNDARIO,
    pad=14
)

ax.set_xlabel(
    "Calificación final (orden ordinal de menor a mayor)",
    labelpad=12,
    fontweight="bold",
    color=COLOR_TEXTO
)

ax.set_ylabel(
    "Número de estudiantes",
    labelpad=10,
    fontweight="bold",
    color=COLOR_TEXTO
)

# Escala vertical con espacio para etiquetas y anotación
ax.set_ylim(0, max(counts.max() + 12, annotation_y + 7))

# Cuadrícula horizontal discreta
ax.set_axisbelow(True)
ax.grid(axis="y", linestyle="-", alpha=0.75)
ax.grid(axis="x", visible=False)

# Quitar bordes innecesarios
sns.despine(ax=ax, top=True, right=True)

ax.tick_params(axis="x", length=0, pad=9)
ax.tick_params(axis="y", length=0, colors=COLOR_SECUNDARIO)

# Nota metodológica
fig.text(
    0.10,
    0.025,
    "Nota: los porcentajes se calculan sobre los estudiantes "
    "con calificación válida.",
    fontsize=9,
    color=COLOR_SECUNDARIO
)

plt.tight_layout(rect=[0.04, 0.07, 0.98, 0.93])

# Guardar la gráfica en la carpeta del script
output_path = base_dir / "calificaciones_mejorada.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"Gráfica guardada en: {output_path}")
