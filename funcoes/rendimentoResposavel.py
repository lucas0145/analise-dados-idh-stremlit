import pandas as pd
import numpy as np
import matplotlib.pyplot as mt
import seaborn as sb

def grafico_rendimento_responsavel():

    dados = pd.read_csv('./dados/idh_idhm_municipios_consorcios_renda.csv')
    dados["idhm_educacao"] = dados["idhm_educacao"].round(2)

    fig, ax = mt.subplots(figsize=(12, 6))

    sb.boxplot(
        data=dados,
        x="rendimento_medio_responsavel",
        y="uf",
        hue="consorcio_governadores",
        dodge=False,
        palette="vlag",
        whis=1.5,
        fliersize=0,
        ax=ax,
    )

    ax.set_title("Renda e Educação com base nos Governadores", fontsize=14, fontweight="bold")
    ax.set_xlabel("Rendimento Medio Responsavel", fontsize=12)
    ax.set_ylabel("UF", fontsize=12)
    ax.legend(title="consorcio_governadores", frameon=True)

    fig.tight_layout(h_pad=800, w_pad=400)

    return fig
