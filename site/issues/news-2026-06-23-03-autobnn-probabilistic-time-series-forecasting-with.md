---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-06-23
type: news
rank: 3
source: "Google AI Blog"
source_url: "http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html"
published: 2024-03-28T13:53:00-07:00
layout: "layout.njk"
tags:
  - news
  - issue
---

## What Happened

AutoBNN is a novel probabilistic time series forecasting method that utilizes compositional Bayesian neural networks. This approach combines the advantages of both machine learning and statistical modeling, enabling the creation of highly accurate forecasts even with limited data.

The network consists of three main components:

* **Compositional priors:** These capture the underlying structure of the data, capturing relationships between different features.
* **Dynamic Bayesian inference:** This allows the network to update its parameters based on new data, leading to incremental improvement in forecasts.
* **Neural networks:** These learn complex relationships between the features, further enhancing the forecasting accuracy.

The AutoBNN algorithm has been empirically validated on various datasets, demonstrating significant improvements in forecasting accuracy compared to traditional methods such as ARIMA and LSTM. The network can handle a wide range of data types and feature dimensions.

## Why It Matters

AutoBNN offers several key benefits:

* **High accuracy:** It achieves comparable or even better forecasting accuracy compared to traditional methods, especially when dealing with limited data.
* **Flexibility:** It can handle various data types and feature dimensions, making it suitable for diverse forecasting problems.
* **Incremental learning:** It allows for continuous improvement in forecasts as new data becomes available, ensuring optimal performance.

This advancement holds significant implications for various industries, including finance, healthcare, and supply chain management. By providing accurate and timely forecasts, AutoBNN can optimize decision-making, improve resource allocation, and enhance risk management.

## Context & Background

AutoBNN is a relatively recent contribution to the field of time series forecasting. The compositional prior approach has proven to be particularly effective for capturing complex relationships in high-dimensional data. The network also leverages the power of neural networks for sophisticated feature learning, further enhancing its forecasting capabilities.

The authors also emphasize the importance of incorporating domain knowledge into the model through the compositional priors. This allows the network to leverage external information and improve its predictive power.

## What to Watch Next

The team plans to further explore the application of AutoBNN on more complex datasets, including financial and healthcare data. Additionally, they aim to investigate the impact of different hyperparameters on the network's performance.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28