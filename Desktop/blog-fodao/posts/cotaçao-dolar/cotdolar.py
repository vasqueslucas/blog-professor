import calendar
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

def grafico_cotacao(mes_ano: str):
    first_date = datetime.strptime("082022", "%m%Y")
    last_date = first_date.replace(day=calendar.monthrange(first_date.year, first_date.month)[1])
    last_date

    
    data_inicial = first_date.strftime("%m-%d-%Y")
    data_final = last_date.strftime("%m-%d-%Y")

    url = url = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    f"CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?"
    f"@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'&$format=json"
)

  




    

    response = requests.get(url)
    print("Status code:", response.status_code)
    print("URL usada:", url)

    if response.status_code != 200:
        print(" Erro na requisição:", response.text)
        return

    dados = response.json()

    if not dados.get('value'):
        print(" Nenhum dado encontrado para esse período.")
        return

    df = pd.DataFrame(dados['value'])
    df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'])

    fig = px.line(
        df,
        x='dataHoraCotacao',
        y='cotacaoVenda',
        title=f"Cotação do Dólar - {first_date.strftime('%B/%Y').capitalize()}",
        labels={'dataHoraCotacao': 'Data', 'cotacaoVenda': 'Cotação Venda (R$)'},
        markers=True
    )
    fig.show()

# 🔹 Teste
grafico_cotacao("082021")
