---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-06-14
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

AutoBNN is a new probabilistic time series forecasting method that uses compositional Bayesian neural networks (cBNNs) to generate high-fidelity forecasts for complex systems. This method significantly improves upon traditional time series forecasting by incorporating prior information into the model through a compositional approach.

The cBNN model consists of two parts: a recurrent neural network (RNN) and a dynamic Bayesian network (DBN). The RNN captures the temporal dependencies in the data, while the DBN integrates prior information through a conditional random field (CRF). This enables the model to capture and utilize both temporal and contextual information for accurate forecasting.

## Why It Matters

AutoBNN offers several advantages over traditional time series forecasting methods:

- Incorporation of prior information: The cBNN model explicitly captures prior knowledge through the compositional CRF, leading to improved forecasting accuracy.
- High-fidelity forecasts: The model generates accurate forecasts even for systems with complex dynamics and multiple covariate inputs.
- Robustness to noise: AutoBNN is robust to measurement errors and noise in the data, making it suitable for real-world forecasting applications.

## Context & Background

AutoBNN builds upon the successful foundation of BNNs, which have achieved remarkable success in various forecasting tasks due to their ability to leverage both temporal and contextual information. The compositional approach in AutoBNN further enhances its capabilities by incorporating prior knowledge into the model.

The model is particularly suitable for forecasting problems where historical data is incomplete or when dealing with high-dimensional data with complex relationships. It finds applications in various fields, including finance, logistics, and healthcare, where accurate forecasting is crucial.

## What to Watch Next

The release of AutoBNN is a significant milestone in probabilistic time series forecasting. With its improved accuracy and robustness, AutoBNN holds the potential to revolutionize forecasting in various domains. The model is expected to achieve significant improvements in forecast accuracy compared to traditional forecasting methods.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28