import pandas as pd
import matplotlib.pyplot as mt
import seaborn as sb

def grafico_alfabetizacao():

    dados = pd.read_csv('./dados/idh_alfabetizacao_sexo_raca_municipios.csv')

    grafico = sb.catplot(
        data=dados,
        x="raca_cor",
        y="taxa_alfabetizacao_pct",
        hue="sexo",
        kind="box",
        height=5,
        aspect=1.2,
    )


    grafico.set_axis_labels("Raça/Cor", "Taxa de Alfabetização (%)")
    grafico.legend.set_title("Sexo")


    return grafico
