# 📈 Gold Price & Returns Prediction

This project is my first data science exploratory project regarding creating a model to predict future gold prices and also predicting the daily returns of gold

---

## 🚀 Overview
This project serves as an exploratory deep-dive into financial forecasting. The primary goal was to build a robust pipeline capable of predicting not just the absolute price of gold, but also the volatility and direction of daily returns.

### Key Objectives:
* **Price Forecasting:** Predicting the future closing price of Gold.
* **Returns Analysis:** Estimating daily percentage changes (returns) to understand market momentum.
* **Time-Series Engineering:** Leveraging historical lags to capture temporal dependencies.

---

## 🛠️ Tech Stack
|  | |
| :--- | :--- |
| **Language** | Python 3.14.2 |
| **Data Manipulation** | Pandas 3.0.1, NumPy 2.4.3 |
| **Machine Learning** | Scikit-Learn 1.8.0 |
| **Visualization** | Matplotlib 3.10.8, Seaborn 0.13.2 |

---

## 📚 Concepts & Techniques
This project covers the end-to-end Data Science lifecycle:

* **Data Preprocessing:** Handling null values, data cleaning, and lowering skewness via transformations.
* **Feature Engineering:** Implementing **Feature Lagging** (essential for time-series) and technical indicator creation.
* **Exploratory Data Analysis (EDA):** Correlation analysis and distribution visualization.
* **Pipeline Architecture:** Using Scikit-Learn pipelines for reproducible data transformations and model training.
* **Model Evaluation:** Performance metric analysis (MAE, RMSE, $R^2$) and residual visualization.

---

## 📊 Dataset
The project utilizes the [Gold Price Forecasting Dataset](https://www.kaggle.com/datasets/vishardmehta/gold-price-forecasting-dataset) from Kaggle, which includes historical open, high, low, and close prices.

---
## Installation
Clone the repository
```bash
git clone https://github.com/SrujanBali/Gold_Price_DS
```
Install Dependencies
```bash
pip install -r requirements.txt
```
---

## 📂 Project Organization
The project follows a structured modular approach for scalability:

```text
├── LICENSE            <- Open-source license
├── Makefile           <- Commands for `make data` or `make train`
├── README.md          <- Project overview
├── data
│   ├── external       <- Third party sources
│   ├── interim        <- Intermediate transformed data
│   ├── processed      <- Final, canonical data sets for modeling
│   └── raw            <- Original, immutable data dump
├── docs               <- Project documentation (MkDocs)
├── models             <- Serialized models (.pkl) and summaries
├── notebooks          <- Structured Jupyter notebooks (e.g., 1.0-eda, 2.0-modeling)
├── pyproject.toml     <- Build system dependencies and tool configs
├── references         <- Data dictionaries and manuals
├── reports            <- Generated analysis (HTML, PDF)
│   └── figures        <- Visualizations for reports
├── requirements.txt   <- File for reproducing the environment
└── gold_price_ds      <- Source code
    ├── __init__.py    <- Module initialization
    ├── config.py      <- Configuration & constants
    ├── dataset.py     <- Data ingestion scripts
    ├── features.py    <- Feature engineering logic
    ├── plots.py       <- Visualization functions
    └── modeling       
        ├── predict.py <- Inference logic
        └── train.py   <- Model training scripts
