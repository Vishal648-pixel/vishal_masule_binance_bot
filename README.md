# vishal_masule_binance_bot

Project: Trading Bot Orders
📌 Overview
This project is a Python-based trading bot framework that demonstrates different order execution strategies:

Market Orders – immediate execution at current price

Limit Orders – execution at a specified price

OCO (One-Cancels-the-Other) – advanced conditional order strategy

TWAP (Time-Weighted Average Price) – algorithmic execution strategy

It includes logging, reporting, and modular source code for easy extension.

📂 Project Structure
Code
project_root/
│
├── src/
│   ├── market_orders.py      # Market order logic
│   ├── limit_orders.py       # Limit order logic
│   ├── advanced/
│   │   ├── oco.py            # OCO order logic
│   │   └── twap.py           # TWAP strategy
│
├── bot.log                   # Logs (API calls, errors, executions)
├── report.pdf                # Analysis (screenshots, explanations)
└── README.md                 # Setup, dependencies, usage


deactivate

Note-For setup read setup.txt file
