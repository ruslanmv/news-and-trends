---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-11-12
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

AutoBNN is a new probabilistic time series forecasting method that uses compositional Bayesian neural networks to generate accurate forecasts for various time series problems. This approach offers several advantages over traditional statistical methods, including the ability to handle high-dimensional data and account for uncertainties in the data.

The method involves a two-step process. First, an autoregressive model is trained on the data to capture the underlying relationships between variables. Second, a Bayesian neural network is used to incorporate the uncertainties and dependencies from the autoregressive model.

The use of compositional Bayesian neural networks allows AutoBNN to generate probabilistic forecasts that are not only accurate but also robust to changes in the data. This makes it particularly well-suited for forecasting problems where data is highly volatile or contains outliers.

The model was evaluated on various datasets, including financial market data, weather patterns, and economic indicators. The results showed that AutoBNN achieved significant improvements in forecast accuracy compared to traditional statistical methods.

## Why It Matters

AutoBNN offers several advantages over traditional statistical methods for time series forecasting. These advantages include:

* **High accuracy:** AutoBNN can generate accurate forecasts even for highly volatile data.
* **Robustness to uncertainties:** The model accounts for uncertainties and dependencies in the data, making it robust to changes in the data.
* **Ability to handle high-dimensional data:** AutoBNN can handle high-dimensional data by using a sparse representation of the data.
* **Improved interpretability:** The model provides insights into the relationships between variables, which can be valuable for decision-makers.

These advantages make AutoBNN a promising tool for a wide range of forecasting problems. It is particularly well-suited for forecasting problems where data is highly volatile or contains outliers.

## Context & Background

AutoBNN is a relatively new method, having been published in a Google AI blog in 2024. The method builds upon the foundations of existing probabilistic modeling techniques, such as particle filtering and Bayesian networks.

The development of AutoBNN has been motivated by the increasing availability of high-dimensional data. Traditional statistical methods can become computationally expensive and may not be able to handle the high-dimensional nature of many real-world datasets.

AutoBNN stands out from other probabilistic time series forecasting methods due to its ability to generate probabilistic forecasts. This allows it to capture the uncertainty and dependencies in the data, which is particularly important for forecasting problems.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28