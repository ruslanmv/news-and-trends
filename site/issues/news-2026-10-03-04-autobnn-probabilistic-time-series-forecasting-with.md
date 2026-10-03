---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-10-03
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

AutoBNN is a novel probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) for forecasting continuous variables. This approach offers several advantages over traditional recurrent neural networks (RNNs), including better long-term memory handling and increased robustness to noise.

The core idea of AutoBNN lies in the composition of two separate neural networks: a recurrent neural network (RNN) and a CBBN. The RNN captures long-term dependencies in the data through its recurrent structure, while the CBBN focuses on capturing short-term dependencies and dynamics in the data.

By combining the strengths of both networks, AutoBNN achieves improved forecasting performance compared to traditional RNNs. This is particularly beneficial for problems with long-term dependencies, such as financial data, weather patterns, and climate data.

## Why It Matters

AutoBNN holds significant implications for various industries and fields, including:

- **Finance**: Predicting stock prices, market trends, and economic indicators.
- **Weather**: Forecasting weather patterns, including temperature, precipitation, and extreme events.
- **Climate science**: Predicting future climate scenarios and impacts on ecosystems and infrastructure.

The improved accuracy and robustness of AutoBNN can lead to more reliable and robust predictions in these and other domains.

## Context & Background

AutoBNN is a relatively recent development in time series forecasting, first proposed in 2023. However, the underlying concepts of CBBNs and RNNs have been extensively studied in the field.

The popularity of AutoBNN is due to its ability to address the limitations of traditional RNNs while maintaining computational efficiency. This makes it suitable for real-world applications with large datasets.

## What to Watch Next

The research team plans to explore the use of AutoBNN on a wide range of datasets, including financial market data, weather patterns, and climate records. They also aim to investigate the impact of different hyperparameters and optimization algorithms on the forecasting performance.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28