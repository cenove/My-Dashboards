# Investment Portfolio BI Dashboard

# README in Portuguese
- [Português](PT/README.pt.md)

A Business Intelligence project focused on monitoring investment portfolios in a fictional scenario of high-net-worth clients. The project uses synthetic data to analyze assets under management, Banker performance, client segments, investment products, and completed or pending transactions.

The goal is to demonstrate a practical BI workflow: generate clean data, model the data in Power BI, and turn the information into business-oriented indicators and visualizations.

## Dashboard Preview

### 1. Executive Overview

Presents an overview of clients, assets under management, average assets per portfolio, net inflow, portfolio distribution by product, and transactions over time.

### 2. Banker Performance

Compares Bankers by gross transaction volume, number of portfolios, and net inflow. The analysis by transaction type helps show the share of investments, redemptions, and transfers.

### 3. Clients and Portfolios

Explores the distribution of assets and clients by segment, the value of client portfolios, and the value of pending transactions.

### 4. Transaction Trends

Tracks the volume of completed investments and redemptions, as well as net inflow over time. The charts help show general trends and investigate periods with positive or negative net inflow.

---

## Core Question of the Project

**How can investment portfolio data help monitor portfolio performance, understand client and Banker activity, and identify transactions that need attention?**

Additional questions:

- How are assets under management distributed across Bankers, client segments, and investment products?
- Which Bankers manage the largest portfolios and have the highest gross transaction volume?
- Which Bankers have the highest and lowest net inflow in the selected period?
- How does the volume of completed investments and redemptions evolve over time?
- Which clients or transactions account for the largest pending amounts?
- How does the number of clients in each segment compare to that segment's share of total assets?

## Data Flow

```text
Synthetic data generator in Python
                 ↓
          CSV files
                 ↓
Power BI data model (star schema)
                 ↓
DAX measures, dashboards, and business analysis
```

All generated records are synthetic and do not represent real clients, Bankers, or financial transactions.

## Power BI and Data Modeling

The report uses a star schema structure, including a calendar dimension (`dCalendario`) to support time-based analysis. The model was organized so that date, Banker, segment, and product filters affect the corresponding visuals.

### Key Indicators

- **Clients in Portfolio:** distinct count of clients in the selected context.
- **Assets Under Management:** current portfolio assets considered in the selected context.
- **Average Assets per Portfolio:** average calculated at the appropriate portfolio or client granularity.
- **Gross Transaction Volume:** total amount moved, according to the types and statuses defined by the visual or measure.
- **Net Inflow:** completed investments minus completed redemptions, respecting the report filters.
- **Pending Transactions Value:** value of transactions with pending status.

### Net Inflow DAX Measure

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

This measure defines net inflow as completed investments minus completed redemptions. Transfers are not included in this calculation.

> **Note:** The DAX code is kept unchanged because the measure, table, and column names are the actual identifiers in the Portuguese data model. "Captação Líquida" = Net Inflow, "Aplicação" = Investment, "Resgate" = Redemption, "Concluída" = Completed.

## Project Structure

```text
project/
├── data/
│   └── cleaned/          # Cleaned data exported by Python
├── reports/
│   └── investment_portfolio.pbix
└── .asset/
    ├── VisaoExecutiva.gif
    ├── EvolucaoMovimentacoes.gif
    ├── DesempenhodosBankers.gif
    └── ClientesCarteira.gif
```

## Limitations

- The dataset is synthetic and was created for demonstration and learning purposes.
- The dashboard is not connected to a financial institution or a production system.
- In this project, net inflow is defined as completed investments minus completed redemptions; other business rules may use different definitions.
- The charts support monitoring and investigation, but on their own they do not prove investment returns, client satisfaction, or risk level.

## Tools & Technologies Used

- **Claude**: Used to help with synthetic data generation and documentation
- **DAX (Data Analysis Expressions)**: Used to develop business metrics and formulas for KPIs and Cards
- **Power BI**: Used for data modeling and data visualization
- **Python**: The Pandas library was used for data modeling and data generation

## Developer

**Diogo Oliveira**
