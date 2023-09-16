
#importações
import requests
from bs4 import BeautifulSoup
import locale

from tabulate import tabulate

from modelos import FundoImobiliario, Estrategia

#setando localização para tratamentos de dados, para pr-BR
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF8')


#Definindo função para tratar os dados de porcentagem
def trata_porcetagem(porcentagem_str):
    return locale.atof(porcentagem_str. split('%')[0])

#Definindo função para tratar os dados decimais
def trata_decimal(decimal_str):
    return locale.atof(decimal_str)


headers = {'user-Agent': 'Mozilla/5.0'}

resposta = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)

soup = BeautifulSoup(resposta.text, 'html.parser')

linhas = soup.find(id="tabelaResultado").find('tbody').find_all('tr')


resultado = []

estrategia = Estrategia(
    cotacao_atual_minima=50,
    dividiend_yield_minimo=5,
    p_pv_minimo=0.70,
    valor_mercado_minimo=2000000000,
    liquidez_mercado_minima=50000,
    qt_minima_imoveis=5,
    maxima_vacancia_media=10
)



for linha in linhas:
    dados_fundo = linha.find_all('td')
    codigo = dados_fundo[0].text
    segmento = dados_fundo[1].text
    cotacao = trata_decimal(dados_fundo[2].text)
    ffo_yield = trata_porcetagem(dados_fundo[3].text)
    dividiend_yield = trata_porcetagem(dados_fundo[4].text)
    p_pv = trata_decimal(dados_fundo[5].text)
    valor_mercado = trata_decimal(dados_fundo[6].text)
    liquidez = trata_decimal(dados_fundo[7].text)
    qt_imoveis = int(dados_fundo[8].text)
    preco_m2 = trata_decimal(dados_fundo[9].text)
    aluguel_m2 = trata_decimal(dados_fundo[10].text)
    cap_rate = trata_porcetagem(dados_fundo[11].text)
    vacancia = trata_porcetagem(dados_fundo[12].text)

    fundo_imobilario = FundoImobiliario(
        codigo, segmento, cotacao, ffo_yield, dividiend_yield, p_pv, valor_mercado, liquidez,
        qt_imoveis, preco_m2, aluguel_m2, cap_rate, vacancia
    )

    if estrategia.aplica_estrategia(fundo_imobilario):
        resultado.append(fundo_imobilario)


cabecalho = ["CÓDIGO", "SEGMENTO", "COTAÇÃO ATUAL", "DIVIDEND YIELD"]

tabela = []

for elemento in resultado:
    tabela.append([
        elemento.codigo,
        elemento.segmento,
        locale.currency(elemento.cotacao_atual),
        f'{locale.str(elemento.dividiend_yield)} %'
    ])
    
print(tabulate(tabela, headers=cabecalho, showindex='always',tablefmt='fancy_grid'))





