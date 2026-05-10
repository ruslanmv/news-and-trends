---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-05-10
type: news
rank: 4
source: "Google AI Blog"
source_url: "http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html"
published: 2024-03-28T13:53:00-07:00
layout: "layout.njk"
tags:
  - news
  - issue
---

## What Happened

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) to generate probabilistic future trajectories. This method is particularly well-suited for forecasting time series data with complex, non-stationary characteristics, which are common in financial and economic applications.

The core idea behind AutoBNN is to decompose the time series into a set of independent components. These components are then modeled using CBNNs, which are known for their ability to capture complex relationships between different features in time series data.

The AutoBNN algorithm iteratively updates the weights of the CBNNs based on the observed data. This process allows the model to learn the underlying structure of the time series and generate probabilistic forecasts.

## Why It Matters

AutoBNN offers several advantages over traditional time series forecasting methods:

* **Improved accuracy:** CBNNs can capture complex relationships between features in time series data, leading to more accurate predictions compared to other methods.
* **Robustness to outliers:** CBNNs are robust to outliers in the data, which can be a challenge for other methods.
* **Flexibility:** The model can be extended to handle different time series lengths and data complexities.

The application of AutoBNN to financial data has shown promising results. The method has successfully generated probabilistic future trajectories for stock prices, commodity prices, and other financial indices.

## Context & Background

AutoBNN is a relatively new method, with the first paper published in 2024. However, CBNNs have been widely used in time series forecasting, and the underlying concepts have been well-established in the field.

The method is particularly well-suited for financial applications due to the inherent non-stationarity and complex relationships between financial variables. The use of CBNNs allows the model to capture these relationships and generate more accurate forecasts.

## What to Watch Next

Researchers are actively working on improving the performance of AutoBNN. Future research directions include exploring the use of more robust regularization techniques, investigating the impact of different hyperparameters on the model's performance, and developing hybrid methods with other machine learning algorithms.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28