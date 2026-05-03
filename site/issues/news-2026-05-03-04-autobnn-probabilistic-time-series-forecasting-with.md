---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-05-03
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

AutoBNN, an AI research team at Google, unveiled their Probabilistic Time Series Forecasting with Compositional Bayesian Neural Networks (AutoBNN) model at the Google AI Blog. The model is designed to generate synthetic data for various time series forecasting tasks.

**Why It Matters**

AutoBNN offers several advantages for time series forecasting, including:

- **Generative capability:** It can generate data for various time series, including stock prices, economic indicators, and social media data.
- **Robustness:** The model is robust to noise and outliers, making it effective for forecasting under uncertainty.
- **Scalability:** It can be efficiently parallelized, making it suitable for large datasets.

**Context & Background**

AutoBNN builds upon AutoReg, another generative model for stock price forecasting. Composing AutoBNN with AutoReg allows for the joint learning of time series and external features. AutoBNN incorporates several innovative techniques, including hierarchical LSTM and a novel sampling approach called "reordering."

**What to Watch Next**

Researchers are actively exploring the use of AutoBNN in various forecasting tasks. They are particularly interested in incorporating external data sources and addressing the challenge of heterogeneous data distributions. Additionally, the team plans to evaluate the model's performance on real-world datasets.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28