# Hospital Resource Utilization Prediction System

## Overview

Efficient resource planning is critical for hospital operations, directly impacting patient care, staff allocation, and infrastructure utilization. In many healthcare settings, fluctuations in patient volume can lead to either resource shortages or underutilization.

This project develops a predictive modeling system to forecast short-term hospital resource utilization using historical patient visit data. By modeling temporal patterns in patient flow, the system aims to support data-driven operational planning and decision-making.

---

## Problem Statement

Hospital systems must anticipate variations in patient demand to allocate resources effectively. However, patient inflow often exhibits temporal patterns influenced by factors such as day-of-week effects, seasonality, and behavioral trends.

The objective of this project is to:

> **Predict daily patient volume using historical time-series data, enabling short-term forecasting of hospital resource utilization.**

This problem is formulated as a **time-series regression task**, where the goal is to estimate future patient counts based on past observations.

---

## Dataset

This project uses the **Medical Appointment No-Shows dataset**, a publicly available healthcare dataset containing patient appointment records.

The dataset includes:

- patient identifiers
- appointment dates
- demographic information
- appointment attendance behavior

For this project, the data is transformed into a **daily time series**, where each observation represents the total number of attended patient visits per day.

---

## Methodology

The project follows a structured time-series modeling workflow:

1. Data preprocessing and filtering of attended visits
2. Aggregation of appointment-level data into daily patient counts
3. Feature engineering using lag variables and rolling statistics
4. Exploratory analysis of temporal patterns
5. Training and evaluation of regression models

Feature engineering includes:

- lag features (previous days' patient counts)
- rolling averages and variability measures
- calendar-based features (day of week, month)

---

## Evaluation

Model performance is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

A **time-based train-test split** is used to ensure realistic forecasting conditions and prevent data leakage.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## Project Structure

data/
notebooks/
src/
outputs/


---

## Expected Outcomes

The project aims to:

- Identify temporal patterns in hospital patient volume
- Build models capable of short-term demand forecasting
- Provide insights into factors influencing resource utilization

---

## Future Improvements

Potential extensions include:

- advanced time-series models (e.g., ARIMA, LSTM)
- multivariate forecasting with additional hospital data
- real-time prediction pipelines for operational deployment
