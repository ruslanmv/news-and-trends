---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-10-21
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

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks to generate high-fidelity forecasts for stock prices and other financial time series. 

This approach offers several advantages over traditional recurrent neural networks (RNNs), including:

- **Composed of multiple layers:** AutoBNN combines a long short-term memory (LSTM) and a feedforward network to capture both long-term dependencies and local features in the data.
- **Probabilistic nature:** Unlike RNNs, AutoBNN generates probability distributions for the future values, allowing for better risk management and scenario analysis.
- **Scalability:** AutoBNN is particularly efficient and scalable, making it suitable for real-time forecasting.

The model is trained on a massive dataset of financial time series, including stock prices and economic indicators. This data is used to automatically discover the optimal network architecture and hyperparameters for the task.

## Why It Matters

The development of AutoBNN has significant implications for various industries, including finance, where accurate forecasting is crucial for portfolio management, risk assessment, and market analysis. 

- **Enhanced portfolio performance:** By providing more accurate forecasts, AutoBNN can help investors make more informed investment decisions, potentially leading to higher returns.
- **Improved risk management:** The probabilistic nature of the model allows investors to better assess and manage risks associated with financial investments.
- **Efficient risk assessment:** AutoBNN's scalability enables efficient risk assessment, enabling financial institutions to make informed decisions about risk tolerance and capital allocation.

## Context & Background

AutoBNN is a relatively new approach in the field of time series forecasting. The model has been shown to be highly effective in generating accurate and robust forecasts for stock prices and other financial time series.

AutoBNN builds upon the foundations of LSTMs and feedforward networks. LSTMs excel at capturing long-term dependencies in sequence data, while feedforward networks excel at capturing local features and relationships in data.

## What to Watch Next

The future development of AutoBNN holds several promising avenues.

- **Integration with other forecasting techniques:** AutoBNN can be combined with other machine learning techniques, such as reinforcement learning, to create more robust forecasting models.
- **Adaptation to other domains:** AutoBNN can be adapted to forecast non-financial time series, such as weather patterns and economic indicators.
- **Deployment in real-time systems:** The scalability of AutoBNN enables its deployment in real-time forecasting applications, such as risk management and portfolio optimization.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28