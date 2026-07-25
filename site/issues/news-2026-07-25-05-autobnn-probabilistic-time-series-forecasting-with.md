---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-07-25
type: news
rank: 5
source: "Google AI Blog"
source_url: "http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html"
published: 2024-03-28T13:53:00-07:00
layout: "layout.njk"
tags:
  - news
  - issue
---

## What Happened

**AutoBNN: Probabilistic Time Series Forecasting with Compositional Bayesian Neural Networks**

AutoBNN is a novel approach to time series forecasting that utilizes compositional Bayesian neural networks (CBNNs) to generate probabilistic forecasts. This approach combines the strengths of CBNNs, known for their ability to capture complex temporal dependencies, and traditional time series models, which provide interpretability.

The main idea is to represent the underlying data generating process as a Markov chain and use a CBBN to learn the transition probabilities between states. This probabilistic approach allows AutoBNN to not only generate forecasts but also quantify their uncertainty.

**Why It Matters**

AutoBNN offers several advantages over traditional time series models:

- **Probabilistic forecasts:** It provides probabilistic forecasts, allowing for better risk management and scenario analysis.
- **Interpretability:** CBBNs offer interpretable forecasts, enabling users to understand the underlying dynamics of the system.
- **Robustness:** It is robust to outliers and seasonality, making it suitable for a wide range of time series problems.

**Context & Background**

AutoBNN is a recent breakthrough in time series forecasting, particularly for high-dimensional data. The authors draw inspiration from the success of CBBNs in natural language processing and integrate them into a probabilistic setting. The model is particularly effective when dealing with complex and seasonal time series.

**What to Watch Next**

The authors plan to explore the generalization of AutoBNN to multiple time series dimensions and develop a hierarchical CBBN architecture to improve its interpretability. Additionally, they aim to benchmark the model against existing time series forecasting methods on real-world datasets.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28