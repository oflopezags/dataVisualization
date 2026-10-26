"""
Dashboard: ¿Qué se relaciona más con el desempeño de estudiantes de educación superior?
Dataset: Higher Education Students Performance Evaluation (UCI, n = 145)

Uso:
    pip install dash plotly pandas scipy
    python dashboard.py        # abrir http://127.0.0.1:8050
El archivo DATA__1_.csv debe estar en la misma carpeta que este script.
"""
import pandas as pd
from scipy.stats import spearmanr
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

# ------------------------------------------------------------------ DATOS
df = pd.read_csv("DATA__1_.csv", encoding="utf-8-sig")
df.columns = [c.strip() for c in df.columns]
df = df.rename(columns={"COURSE ID": "curso", "GRADE": "nota"})

# Nivel de desempeño (agrupa la nota 0-7 en 3 niveles legibles)
NIVELES = ["Bajo", "Medio", "Alto"]
df["nivel"] = pd.cut(df["nota"], [-1, 2, 4, 7], labels=NIVELES)

# Colores con intención: el azul (Alto) es lo que debe verse primero.
COLOR = {"Bajo": "#D9822B", "Medio": "#C9CED3", "Alto": "#1F4E79"}
TEXTO, GRIS = "#222B33", "#6B7680"

# ------------------------------------------------------------------ DICCIONARIO
# columna -> (nombre corto, {código: etiqueta})
VARS = {
    "29": ("Promedio (GPA) del semestre anterior",
           {1: "<2.00", 2: "2.00–2.49", 3: "2.50–2.99", 4: "3.00–3.49", 5: ">3.49"}),
    "30": ("Promedio esperado al graduarse",
           {1: "<2.00", 2: "2.00–2.49", 3: "2.50–2.99", 4: "3.00–3.49", 5: ">3.49"}),
    "22": ("Asistencia a clases", {1: "Siempre", 2: "A veces", 3: "Nunca"}),
    "20": ("Asistencia a seminarios", {1: "Sí", 2: "No"}),
    "17": ("Horas de estudio semanales",
           {1: "Ninguna", 2: "<5 h", 3: "6–10 h", 4: "11–20 h", 5: ">20 h"}),
    "18": ("Lectura no científica", {1: "Nunca", 2: "A veces", 3: "Frecuente"}),
    "19": ("Lectura científica", {1: "Nunca", 2: "A veces", 3: "Frecuente"}),
    "25": ("Toma de apuntes", {1: "Nunca", 2: "A veces", 3: "Siempre"}),
    "26": ("Escucha en clase", {1: "Nunca", 2: "A veces", 3: "Siempre"}),
    "4": ("Tipo de beca", {1: "Ninguna", 2: "25%", 3: "50%", 4: "75%", 5: "Completa"}),
    "5": ("Trabajo adicional", {1: "Sí", 2: "No"}),
    "2": ("Sexo", {1: "Mujer", 2: "Hombre"}),
    "11": ("Educación de la madre",
           {1: "Primaria", 2: "Secundaria", 3: "Bachillerato", 4: "Universidad", 5: "Maestría", 6: "Doctorado"}),
    "12": ("Educación del padre",
           {1: "Primaria", 2: "Secundaria", 3: "Bachillerato", 4: "Universidad", 5: "Maestría", 6: "Doctorado"}),
}

# Nombres cortos para el ranking (las 30 variables)
NOMBRES = {
    "1": "Edad", "2": "Sexo", "3": "Tipo de preparatoria", "4": "Beca", "5": "Trabajo adicional",
    "6": "Actividad artística/deportiva", "7": "Pareja", "8": "Ingreso", "9": "Transporte",
    "10": "Alojamiento", "11": "Educación madre", "12": "Educación padre", "13": "Hermanos",
    "14": "Estado civil padres", "15": "Ocupación madre", "16": "Ocupación padre",
    "17": "Horas de estudio", "18": "Lectura no científica", "19": "Lectura científica",
    "20": "Asistencia a seminarios", "21": "Impacto de proyectos", "22": "Asistencia a clases",
    "23": "Examen: con quién", "24": "Examen: cuándo", "25": "Toma de apuntes",
    "26": "Escucha en clase", "27": "Discusión en clase", "28": "Aula invertida",
    "29": "GPA semestre anterior", "30": "GPA esperado",
}

CURSOS = sorted(df["curso"].unique())


# ------------------------------------------------------------------ FUNCIONES
def filtrar(curso):
    return df if curso == "todos" else df[df["curso"] == int(curso)]


def tabla_pct(d, col):
    """% de estudiantes por nivel de desempeño dentro de cada categoría de `col`."""
    etiquetas = VARS[col][1]
    ct = pd.crosstab(d[col], d["nivel"]).reindex(columns=NIVELES, fill_value=0)
    ct = ct.reindex([k for k in etiquetas if k in ct.index])
    n = ct.sum(axis=1)
    pct = ct.div(n, axis=0) * 100
    return pct, n, ct


def figura_agrupada(d, col, altura, tam_texto, modo="pct"):
    """modo="pct": eje Y en % dentro de cada categoría; modo="n": eje Y en número de alumnos."""
    pct, n, ct = tabla_pct(d, col)
    datos = pct if modo == "pct" else ct
    etiquetas = VARS[col][1]
    x = [f"{etiquetas[k]}<br><span style='color:{GRIS}'>n={n[k]}</span>" for k in pct.index]
    fig = go.Figure()
    for nivel in NIVELES:
        fig.add_bar(
            x=x, y=datos[nivel].round(0), name=nivel, marker_color=COLOR[nivel],
            text=[f"{v:.0f}%" if modo == "pct" else f"{int(v)}" for v in datos[nivel]],
            textposition="outside",
            textfont=dict(size=tam_texto, color=TEXTO if nivel != "Medio" else GRIS),
            hovertemplate=("%{y:.0f}% de los estudiantes" if modo == "pct" else "%{y:.0f} alumnos")
            + "<extra>" + nivel + "</extra>",
        )
    fig.update_layout(
        barmode="group", bargap=0.25, bargroupgap=0.06, height=altura,
        template="simple_white", margin=dict(l=10, r=10, t=30, b=10),
        font=dict(family="Arial", color=TEXTO), plot_bgcolor="white",
        legend=dict(orientation="h", y=1.12, x=0, title_text="Desempeño: "),
        yaxis=dict(visible=False, range=[0, 112 if modo == "pct" else max(1, datos.max().max()) * 1.18]),
        xaxis=dict(title=VARS[col][0], showline=False, ticks=""),
    )
    return fig


def figura_ranking(d):
    filas = []
    for c in [str(i) for i in range(1, 31)]:
        if d[c].nunique() < 2:
            continue
        rho, p = spearmanr(d[c], d["nota"])
        filas.append((c, abs(rho), p))
    top = sorted(filas, key=lambda t: -t[1])[:8]
    colores = ["#1F4E79" if c == "29" else "#C9CED3" for c, _, _ in top]
    fig = go.Figure(go.Bar(
        x=[NOMBRES[c] for c, _, _ in top], y=[r for _, r, _ in top],
        marker_color=colores, text=[f"{r:.2f}" for _, r, _ in top], textposition="outside",
        customdata=[p for _, _, p in top],
        hovertemplate="|ρ| = %{y:.2f}<br>p = %{customdata:.3f}<extra></extra>",
    ))
    fig.update_layout(
        height=360, template="simple_white", margin=dict(l=10, r=10, t=10, b=10),
        font=dict(family="Arial", color=TEXTO), showlegend=False,
        yaxis=dict(visible=False, range=[0, max(0.1, top[0][1] * 1.2)]),
        xaxis=dict(tickangle=-35, ticks="", showline=False),
    )
    return fig


def kpi(valor, texto, color):
    return html.Div([
        html.Div(valor, style={"fontSize": "44px", "fontWeight": "700", "color": color, "lineHeight": "1"}),
        html.Div(texto, style={"fontSize": "14px", "color": GRIS, "marginTop": "6px"}),
    ], style={"flex": "1"})


# ------------------------------------------------------------------ LAYOUT
app = Dash(__name__)
app.title = "Desempeño estudiantil"

opciones_curso = [{"label": "Todos los cursos", "value": "todos"}] + [
    {"label": f"Curso {c} (n={int((df['curso'] == c).sum())})", "value": str(c)} for c in CURSOS
]
opciones_var = [{"label": v[0], "value": k} for k, v in VARS.items() if k not in ("29",)]

CARD = {"background": "white", "padding": "18px 22px", "borderRadius": "6px"}

app.layout = html.Div(style={"fontFamily": "Arial", "background": "#F4F5F7", "padding": "24px 32px",
                             "color": TEXTO, "maxWidth": "1300px", "margin": "0 auto"}, children=[

    # 1) Título = insight principal (lo primero que se lee)
    html.H1("El promedio del semestre anterior es la señal más fuerte del desempeño",
            style={"fontSize": "30px", "margin": "0 0 4px 0"}),
    html.Div("145 estudiantes de Ingeniería y Ciencias de la Educación · nota final agrupada en "
             "Bajo (Fail–DC), Medio (CC–CB) y Alto (BB–AA)",
             style={"color": GRIS, "fontSize": "14px", "marginBottom": "14px"}),

    # Filtro
    html.Div([
        html.Span("Filtrar por curso: ", style={"fontSize": "14px", "marginRight": "8px"}),
        dcc.Dropdown(id="f-curso", options=opciones_curso, value="todos", clearable=False,
                     style={"width": "240px", "display": "inline-block", "verticalAlign": "middle"}),
        html.Span(id="aviso-n", style={"marginLeft": "14px", "fontSize": "13px", "color": "#B3541E"}),
    ], style={"marginBottom": "16px"}),

    # 2) Fila principal: KPIs + gráfica protagonista
    html.Div([
        html.Div([
            html.Div(id="kpis", style={"display": "flex", "gap": "24px", "marginBottom": "10px"}),
            dcc.Graph(id="g-main", config={"displayModeBar": False}),
        ], style={**CARD, "flex": "2"}),

        html.Div([
            html.Div("Fuerza de asociación con la nota final (|ρ| de Spearman, top 8)",
                     style={"fontWeight": "700", "fontSize": "14px", "marginBottom": "6px"}),
            dcc.Graph(id="g-rank", config={"displayModeBar": False}),
        ], style={**CARD, "flex": "1"}),
    ], style={"display": "flex", "gap": "16px", "marginBottom": "16px"}),

    # 3) Fila secundaria: explorador (visualmente más discreto)
    html.Div([
        html.Div([
            html.Span("Explorar otra variable: ", style={"fontSize": "14px", "marginRight": "8px"}),
            dcc.Dropdown(id="f-var", options=opciones_var, value="22", clearable=False,
                         style={"width": "320px", "display": "inline-block", "verticalAlign": "middle"}),
        ]),
        dcc.Graph(id="g-sec", config={"displayModeBar": False}),
    ], style={**CARD, "marginBottom": "16px"}),

    # 4) Misma idea, pero con el eje Y en número de alumnos
    html.Div([
        html.Div([
            html.Span("Número de alumnos según: ", style={"fontSize": "14px", "marginRight": "8px"}),
            dcc.Dropdown(id="f-var2", options=opciones_var, value="20", clearable=False,
                         style={"width": "320px", "display": "inline-block", "verticalAlign": "middle"}),
        ]),
        dcc.Graph(id="g-sec2", config={"displayModeBar": False}),
    ], style={**CARD, "marginBottom": "10px"}),

    html.Div("Asociación no implica causalidad. Muestra pequeña: al filtrar por curso, interpretar con cautela. "
             "Fuente: UCI Machine Learning Repository (Yilmaz & Şekeroğlu, CC BY 4.0).",
             style={"fontSize": "12px", "color": GRIS}),
])


# ------------------------------------------------------------------ CALLBACKS
@app.callback(
    Output("g-main", "figure"), Output("g-rank", "figure"),
    Output("kpis", "children"), Output("aviso-n", "children"),
    Input("f-curso", "value"),
)
def actualizar_principal(curso):
    d = filtrar(curso)
    alto_gpa = d[d["29"] >= 4]
    bajo_gpa = d[d["29"] < 4]

    def pct(sub, nivel):
        return f"{(sub['nivel'] == nivel).mean() * 100:.0f}%" if len(sub) else "—"

    kpis = [
        kpi(f"{pct(alto_gpa, 'Alto')} vs {pct(bajo_gpa, 'Alto')}",
            "alcanza nota alta (BB–AA): promedio previo ≥3.00 vs <3.00", COLOR["Alto"]),
        kpi(f"{pct(alto_gpa, 'Bajo')} vs {pct(bajo_gpa, 'Bajo')}",
            "termina con nota baja (Fail–DC): promedio previo ≥3.00 vs <3.00", COLOR["Bajo"]),
    ]
    aviso = f"n = {len(d)}" + ("  ⚠ muestra muy pequeña" if len(d) < 30 else "")
    return figura_agrupada(d, "29", 380, 12), figura_ranking(d), kpis, aviso


@app.callback(Output("g-sec", "figure"), Input("f-curso", "value"), Input("f-var", "value"))
def actualizar_secundaria(curso, var):
    return figura_agrupada(filtrar(curso), var, 300, 11)


@app.callback(Output("g-sec2", "figure"), Input("f-curso", "value"), Input("f-var2", "value"))
def actualizar_secundaria_n(curso, var):
    return figura_agrupada(filtrar(curso), var, 300, 11, modo="n")


if __name__ == "__main__":
    app.run(debug=False)
