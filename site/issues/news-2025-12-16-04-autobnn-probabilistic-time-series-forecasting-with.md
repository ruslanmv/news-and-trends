---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2025-12-16
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

AutoBNN is a novel probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) to generate highly accurate forecasts for complex systems like financial markets. This method surpasses existing approaches due to its ability to capture and represent both the underlying structure and the temporal dynamics of the data.

## Why It Matters

AutoBNN significantly advances the field of time series forecasting by addressing several limitations of existing methods. These limitations include:

- Difficulty in capturing the underlying structure of complex systems.
- Lack of ability to handle high-dimensional data with complex temporal dependencies.
- Inability to generate accurate forecasts for rare and outlier data points.

AutoBNN overcomes these limitations by employing a novel CBBN architecture that allows it to capture the intricate relationships and dependencies between variables in the data. This enables it to generate accurate forecasts even for data with complex temporal dynamics.

## Context & Background

AutoBNN builds upon the groundbreaking work of Huang et al. (2021) who introduced the first CBBN model for time series forecasting. While the original model achieved impressive results, it suffered from limited ability to handle high-dimensional data and rare data points. AutoBNN addresses these limitations by introducing several novel components:

- A novel CBBN architecture that incorporates a hierarchical structure to capture the underlying structure of the data.
- A novel sampling method that allows the model to handle high-dimensional data with complex temporal dependencies.
- A novel loss function that incorporates both the reconstruction error and the Kullback-Leibler divergence between the posterior and prior distributions.

## What to Watch Next

Researchers are actively working on improving the performance of AutoBNN by exploring additional optimization techniques and loss functions. Moreover, they are investigating the applications of this innovative method to various other data science and machine learning tasks.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28