import pandas as pd
import matplotlib.pyplot as mt
import numpy as np
import seaborn as sb


def grafico_pessoas_indigenas():

    fig, ax = mt.subplots(figsize=(8, 5))

    df = pd.read_csv("./dados/idhm_pessoas_indigenas.csv", sep=';', encoding='utf-8-sig')

    sb.barplot(data= df, x= 'regiao', y = 'IDHM_Estimado_Indigena', hue = 'Situacao_Domicilio')

    ax.set_title("Dados Pessoas indigenas", fontsize=14, fontweight="bold")
    ax.set_xlabel("Região", fontsize=11)
    ax.set_ylabel("IDH Estimado Indigena", fontsize=11)
    ax.legend(title="Situacao_Domicilio", frameon=True)

    return fig