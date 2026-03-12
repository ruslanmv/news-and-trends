---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-03-12
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

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (cBNNs) to generate accurate and robust forecasts for a wide range of tasks. This approach combines the strengths of both BNNs and probabilistic modeling, allowing for the capture of complex relationships in the data.

The cBNN architecture consists of a recurrent neural network (RNN) and a causal graphical model. The RNN captures the temporal dependencies between observations, while the causal graphical model allows for the modeling of causal relationships between variables.

The model is particularly suitable for tasks where the underlying data exhibits complex dynamics and multiple long-term dependencies. It has been successfully applied to various problems such as financial forecasting, natural language processing, and disease prediction.

## Why It Matters

AutoBNN offers several advantages over traditional forecasting methods:

- **Robustness:** cBNNs are known to be much more robust to noise and outliers compared to other neural network architectures.
- **Temporal dependency modeling:** The RNN component captures the temporal dependencies between observations, while the causal graphical model allows for the modeling of causal relationships.
- **Improved accuracy:** Empirical results demonstrate that AutoBNN can achieve significant improvements in forecasting accuracy compared to conventional BNNs.

## Context & Background

AutoBNN builds upon the successes of previous probabilistic modeling approaches for time series analysis, such as LSTMs and GNNs. However, cBNNs offer several advantages, including superior robustness and the ability to handle complex data with multiple long-term dependencies.

The model is particularly well-suited for financial forecasting, where historical data often exhibits complex patterns and multiple long-term dependencies. The healthcare and finance industries are among the key sectors benefiting from the advancements offered by AutoBNN.

## What to Watch Next

The development of AutoBNN is ongoing, and the team is actively working on improving the model's performance. Future research directions include exploring the use of ensemble methods to combine multiple cBNNs and investigating the application of the model to other forecasting tasks.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28