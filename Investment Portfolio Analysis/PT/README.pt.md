# Dashboard de BI de Carteiras de Investimentos

Projeto de Business Intelligence voltado ao acompanhamento de carteiras de investimentos em um cenário fictício de clientes do segmento de alta renda. O projeto utiliza dados sintéticos para analisar patrimônio sob gestão, desempenho dos Bankers, segmentos de clientes, produtos de investimento e movimentações concluídas ou pendentes.

O objetivo é demonstrar um fluxo prático de BI: gerar dados brutos, modelar os dados no Power BI e transformar as informações em indicadores e visualizações voltados ao negócio.

## Prévia do Dashboard

### 1. Visão Executiva

![Visão Executiva](asset/VisaoExecutiva.gif)

Apresenta uma visão geral de clientes, patrimônio sob gestão, patrimônio médio por carteira, captação líquida, distribuição das carteiras por produto e movimentações ao longo do tempo.

### 2. Desempenho dos Bankers

![Desempenho dos Bankers](asset/DesempenhodosBankers.gif)

Compara os Bankers por volume bruto de movimentações, quantidade de carteiras e captação líquida. A análise por tipo de movimentação ajuda a entender a participação de aplicações, resgates e transferências.

### 3. Clientes e Carteiras

![Clientes e Carteiras](asset/ClientesCarteira.gif)

Explora a distribuição do patrimônio e dos clientes por segmento, os valores das carteiras dos clientes e o valor das movimentações pendentes.

### 4. Evolução das Movimentações

![Evolução das Movimentações](asset/EvolucaoMovimentacoes.gif)

Acompanha o volume de aplicações e resgates concluídos, além da captação líquida ao longo do tempo. Os gráficos ajudam a observar tendências gerais e investigar períodos com captação líquida positiva ou negativa.

---

## Pergunta Central do Projeto

**Como os dados das carteiras de investimentos podem ajudar a acompanhar o desempenho das carteiras, entender a atividade de clientes e Bankers e identificar movimentações que exigem atenção?**

Perguntas complementares:

- Como o patrimônio sob gestão está distribuído entre Bankers, segmentos de clientes e produtos de investimento?
- Quais Bankers administram as maiores carteiras e apresentam maior volume bruto de movimentações?
- Quais Bankers apresentam a maior e a menor captação líquida no período selecionado?
- Como o volume de aplicações e resgates concluídos evolui ao longo do tempo?
- Quais clientes ou movimentações concentram os maiores valores pendentes?
- Como a quantidade de clientes de cada segmento se compara à participação desse segmento no patrimônio total?

## Fluxo de Dados

```text
Gerador de dados sintéticos em Python
                 ↓
       Arquivos CSV tratados
                 ↓
Modelo de dados no Power BI (star schema)
                 ↓
Medidas DAX, dashboards e análise de negócio
```

Todos os registros gerados são sintéticos e não representam clientes, Bankers ou movimentações financeiras reais.

## Power BI e Modelagem de Dados

O relatório utiliza uma estrutura de modelo estrela (*star schema*), incluindo uma dimensão calendário (`dCalendario`) para apoiar as análises temporais. O modelo foi organizado para permitir que filtros de data, Banker, segmento e produto afetem os visuais correspondentes.

### Principais indicadores
- **Clientes na Carteira:** contagem distinta dos clientes no contexto selecionado.
- **Patrimônio Sob Gestão:** patrimônio atual das carteiras considerado no contexto selecionado.
- **Patrimônio Médio por Carteira:** média calculada na granularidade apropriada de carteira ou cliente.
- **Volume Bruto de Movimentações:** valor total movimentado, conforme os tipos e status definidos pelo visual ou pela medida.
- **Captação Líquida:** aplicações concluídas menos resgates concluídos, respeitando os filtros do relatório.
- **Valor de Movimentações Pendentes:** valor das movimentações com status pendente.

### Medida DAX de Captação Líquida

```DAX
Captação Líquida =
VAR TotalAplicacoes =
    CALCULATE(
        SUM(Movimentacoes[Valor]),
        Movimentacoes[Tipo de Movimentação] = "Aplicação",
        Movimentacoes[Status da Movimentação] = "Concluída"
    )
VAR TotalResgates =
    CALCULATE(
        SUM(Movimentacoes[Valor]),
        Movimentacoes[Tipo de Movimentação] = "Resgate",
        Movimentacoes[Status da Movimentação] = "Concluída"
    )
RETURN
    TotalAplicacoes - TotalResgates
```

Essa medida define a captação líquida como aplicações concluídas menos resgates concluídos. Transferências não são incluídas nesse cálculo.

## Estrutura do Projeto

```text
projeto/
├── data/
│   └── cleaned/          # Dados gerados pelo Python
├── reports/
│   └── investment_portfolio.pbix
└── .asset/
    ├── VisaoExecutiva.gif
    ├── EvolucaoMovimentacoes.gif
    ├── DesempenhodosBankers.gif
    └── ClientesCarteira.gif
```

## Limitações

- A base é sintética e foi criada para demonstração e aprendizagem.
- O dashboard não está conectado a uma instituição financeira nem a um sistema de produção.
- Neste projeto, a captação líquida é definida como aplicações concluídas menos resgates concluídos; outras regras de negócio podem utilizar definições diferentes.
- Os gráficos apoiam o acompanhamento e a investigação, mas não comprovam, isoladamente, rentabilidade dos investimentos, satisfação dos clientes ou nível de risco.

## Ferramentas & Tecnologias utilizadas

* **Claude**: Utilizado para ajudar na geração de dados sintéticos e na documentação
* **DAX (Data Analysis Expressions)**: Utilizado para desenvolver métricas de negócios e fórmulas para KPIs e Cards
* **Power BI**: Usado para modelação de dados, visualização de dados
* **Python**: Foi utilizado a biblioteca do Pandas para geração e modelação de dados

## Desenvolvedor

**Diogo Oliveira**
