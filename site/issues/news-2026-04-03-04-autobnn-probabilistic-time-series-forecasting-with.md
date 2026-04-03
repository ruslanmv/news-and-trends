---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-04-03
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

AutoBNN is a probabilistic time series forecasting model that uses compositional Bayesian neural networks to predict future values based on past observations. This model is a powerful tool for forecasting complex, high-dimensional time series data, and it has been shown to be effective in various financial and economic applications.

The model works by first creating a compositional prior for the underlying process driving the time series. This prior is then updated with new data using a particle filter, which iteratively samples from the posterior distribution and selects the most likely state. The final prediction is then made using the posterior distribution.

AutoBNN is particularly well-suited for forecasting problems where the underlying process is non-stationary or has a high dimensionality. This is because the model can handle these complexities by using a hierarchical representation of the data.

## Why It Matters

AutoBNN is a significant advancement in time series forecasting due to its several advantages:

* **Probabilistic nature:** The model naturally handles uncertainty in the data through the probabilistic nature of the posterior distribution.
* **Non-stationarity handling:** The hierarchical structure of the model allows it to capture non-stationarity in the underlying process.
* **High dimensionality:** The model can handle high-dimensional data by using a sparse, hierarchical representation.

These advantages make AutoBNN a powerful tool for forecasting complex time series data, particularly in financial and economic applications.

## Context & Background

AutoBNN is a relatively new model, having been published in 2024. However, it has quickly gained popularity in the financial industry due to its effectiveness. The model has been tested on a variety of financial datasets, and it has consistently performed well.

AutoBNN is a significant advance in time series forecasting. The model's probabilistic nature and non-stationarity handling capabilities make it well-suited for forecasting complex time series data. This is particularly relevant in financial and economic applications, where accurate forecasting is crucial for making informed decisions.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28