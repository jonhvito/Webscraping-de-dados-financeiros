# 🕷️ Analisador de Fundos Imobiliários com Web Scraping

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Licença](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

Um sistema automatizado para análise de Fundos Imobiliários (FIIs) brasileiros utilizando técnicas de web scraping para coleta de dados e estratégias personalizadas de filtragem.

<!-- ![Exemplo de Saída](https://via.placeholder.com/600x200?text=Exemplo+de+Tabela+de+FIIs+Filtrados) -->    <!-- Adicione uma imagem real posteriormente -->

## 🌐 Contexto: O que é Web Scraping?
Web scraping é a técnica de extração automatizada de dados estruturados da web. Neste projeto:
- **Rastreador (Crawler)**: Navega até a página de FIIs do [Fundamentus](https://www.fundamentus.com.br/fii_resultado.php)
- **Raspador (Scraper)**: Extrai e processa dados financeiros usando BeautifulSoup
- **Aplicação Típica**: Ideal para investidores que desejam identificar oportunidades com base em múltiplos indicadores financeiros

## ⚡ Funcionalidades Principais
- ✅ Coleta em tempo real de 13 indicadores financeiros por FII
- ✅ Filtragem inteligente com 11 critérios ajustáveis
- ✅ Formatação profissional de dados monetários (R$) e percentuais
- ✅ Saída em tabela formatada com `tabulate`
- ✅ Arquitetura modular para fácil expansão

## 🛠️ Tecnologias Utilizadas
| **Tecnologia**       | **Função**                                 |
|-----------------------|--------------------------------------------|
| Python 3.9+          | Lógica principal do sistema               |
| BeautifulSoup 4      | Parsing de HTML e extração de dados       |
| Requests             | Requisições HTTP para obtenção de páginas |
| Tabulate             | Formatação de tabelas no terminal         |
| locale               | Internacionalização de formatos numéricos |

## 🚀 Como Executar

### Pré-requisitos
- Python 3.9+ instalado
- Acesso à internet
- Terminal/CMD funcionando

### Passo a Passo
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/analisador-fiis.git
cd analisador-fiis

# 2. Crie e ative o ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o analisador
python main.py
```

## 📊 Estratégia de Filtragem (Personalizável)
Configure os parâmetros no arquivo `modelos.py`:

```python
# Exemplo de estratégia conservadora
estrategia = Estrategia(
    segmento="Shoppings",               # Filtra por segmento específico
    cotacao_atual_minima=50.0,          # Cotação mínima de R$ 50,00
    dividiend_yield_minimo=6.0,         # DY mínimo de 6% ao ano
    p_pv_minimo=0.70,                   # Preço/Valor Patrimonial mínimo de 0.70
    valor_mercado_minimo=2000000000,    # Valor de mercado mínimo de R$ 2 Bi
    maxima_vacancia_media=10.0          # Vacância máxima de 10%
)
```

## 📁 Estrutura do Projeto
```plaintext
.
├── main.py             # Script principal de execução
├── modelos.py          # Definição das classes FundoImobiliario e Estrategia
├── requirements.txt    # Dependências: beautifulsoup4, requests, tabulate
└── README.md           # Documentação do projeto
```

## 🔍 Detalhes Técnicos de Implementação

### Fluxo de Web Scraping
1. **Requisição HTTP**: Simula navegador com headers personalizados
2. **Parseamento HTML**: Identifica tabela de resultados pelo ID `tabelaResultado`
3. **Tratamento de Dados**:
   - Conversão de valores monetários com `locale`
   - Normalização de porcentagens
   - Validação de tipos numéricos
4. **Aplicação de Filtros**: Utiliza padrão Strategy para decisões de investimento

### Classes Principais (modelos.py)
| **Classe**            | **Responsabilidade**                          |
|-----------------------|-----------------------------------------------|
| `FundoImobiliario`    | Modela entidade FII com 13 atributos financeiros |
| `Estrategia`          | Encapsula regras de seleção de investimentos  |

## 📈 Próximos Passos (Roadmap)
- [ ] Adicionar persistência em banco de dados
- [ ] Implementar interface gráfica (GUI)
- [ ] Criar histórico temporal de indicadores
- [ ] Adicionar comparação com índices de mercado
- [ ] Desenvolver módulo de alertas por e-mail

## ⚠️ Considerações Legais
Este projeto é para fins **educacionais** e **não constitui recomendação de investimento**. Respeite:
- [Política de Robots do Fundamentus](https://www.fundamentus.com.br/robots.txt)
- Termos de Uso do site alvo
- Intervalos entre requisições para não sobrecarregar servidores

## 🤝 Como Contribuir
1. Reporte issues com exemplos reproduzíveis
2. Envie PRs com testes unitários
3. Discuta melhorias nas [Issues](https://github.com/jonhvito/Webscraping-de-dados-financeiros/issues)

## 📜 Licença
Distribuído sob [Licença MIT](LICENSE). Veja `LICENSE` para detalhes.
