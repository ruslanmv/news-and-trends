---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-10-16
type: news
rank: 2
source: "Google AI Blog"
source_url: "http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html"
published: 2024-03-28T13:53:00-07:00
layout: "layout.njk"
tags:
  - news
  - issue
---

## What Happened

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (cDNNs) to generate probabilistic forecasts for sequential data. This approach offers several advantages over traditional recurrent neural networks (RNNs), including the ability to model complex relationships in the data while also being robust to vanishing and exploding data issues.

The cDNN architecture utilizes a hierarchical structure, with multiple layers of feedforward and recurrent connections. This architecture allows the model to capture both long-term dependencies and short-term dynamics in the data, resulting in more accurate forecasts.

AutoBNN is particularly suitable for problems with high-dimensional and irregularly formatted data, such as financial time series and sensor measurements. Its probabilistic nature allows for the quantification of forecast uncertainty, providing valuable insights into the reliability of the predictions.

## Why It Matters

AutoBNN significantly improves upon existing time series forecasting methods by achieving:

* **Reduced prediction error:** cDNNs effectively address the vanishing and exploding data issues inherent in time series, leading to more accurate forecasts.
* **Improved probabilistic uncertainty estimation:** The probabilistic nature of cDNNs allows for the propagation of forecast uncertainty, providing a more comprehensive understanding of the forecast outcomes.
* **Enhanced generalization ability:** AutoBNN demonstrates improved generalization performance compared to traditional RNN-based methods, indicating its effectiveness across diverse datasets.

## Context & Background

AutoBNN builds upon the successes of cDNNs, which have gained significant attention in recent years. These models leverage the power of recurrent connections to capture long-term dependencies in data, leading to improved forecasting performance.

AutoBNN also addresses the limitations of traditional RNNs, such as the high computational complexity and difficulty in handling high-dimensional data. The hierarchical structure of cDNNs allows for efficient training and reduces the computational requirements.

## What to Watch Next

AutoBNN is a promising advancement in time series forecasting, showcasing the effectiveness of cDNNs for complex and high-dimensional data. As a result, further research and experimentation are required to explore the potential applications and real-world success of this novel method.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28