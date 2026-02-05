# Binance Data Extractor

Python library to extract and update market data from the **Binance API** (including spot, futures, and more).  
This project enables retrieval of historical and current market data for different symbols for analysis, data pipelines, or storage.

---

## 📌 Description

`binance-data-extractor` is a Python tool designed to facilitate programmatic extraction of market data from Binance using the official API.  
It is intended for use in analysis, data science, backtesting, or integration with databases.  
Includes utilities to connect to public and authenticated endpoints (authentication required only if API credentials are provided).

---

## 🚀 Installation

### 📥 Prerequisites

- Python 3.8 or higher
- Binance API Key and API Secret (required only for authenticated endpoints)

### 🛠️ Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/fernk01/binance-data-extractor.git
    cd binance-data-extractor
    ```

2. Create and activate a virtual environment (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/macOS
    .venv\Scripts\activate      # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```