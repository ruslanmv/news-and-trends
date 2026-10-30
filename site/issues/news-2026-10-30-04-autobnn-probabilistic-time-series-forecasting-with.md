---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-10-30
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

AutoBNN is a novel probabilistic time series forecasting approach that utilizes compositional Bayesian neural networks (CBNNs) for data generation and uncertainty estimation. The method leverages the compositional nature of CBNNs to model complex relationships in time series data while enabling probabilistic inference, leading to more accurate forecasts and reduced model overfitting.

## Why It Matters

AutoBNN offers several advantages over traditional time series models:

- **Probabilistic forecasting:** CBNNs naturally incorporate uncertainty into the forecasting process, providing more robust predictions that are not susceptible to outliers or specific data points.
- **Compositional representation:** CBNNs represent time series as a composition of multiple causal factors, enabling comprehensive understanding and modeling of complex relationships.
- **Data-driven approach:** The model is trained directly on the data, eliminating the need for manual selection of parameters, which can be subjective and prone to biases.

## Context & Background

AutoBNN builds upon the success of Autoencoders, another probabilistic neural network architecture. While Autoencoders focus on data compression, AutoBNN extends this concept to generate new data samples while preserving the underlying structure and statistics of the source data.

## What to Watch Next

The release of AutoBNN signifies a significant advancement in probabilistic time series forecasting, offering a more robust and flexible approach than previous methods. The model's ability to generate new data points and provide uncertainty estimates will have significant implications in various fields, including finance, healthcare, and engineering.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28