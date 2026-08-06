---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-08-06
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

AutoBNN is a novel probabilistic time series forecasting model that utilizes compositional Bayesian neural networks (cBNNs) to generate probabilistic forecasts. Unlike traditional recurrent neural networks (RNNs), cBNNs do not suffer from vanishing or exploding gradient problems, making them particularly suitable for forecasting problems with long-term dependencies.

The model's core idea is to jointly learn the underlying structure of the data and the underlying stochastic process that generated it. This approach allows the model to capture complex relationships in the data that might be missed by traditional RNNs.

The key components of the model are:

- **Compositional structure**: data is represented as a weighted combination of multiple latent factors.
- **Probabilistic inference**: posterior inference is performed using Monte Carlo sampling.
- **Variational inference**: the model uses variational inference to approximate the posterior distribution.

The model is trained using a variational inference approach that involves minimizing a lower bound on the log-posterior. This approach leads to efficient and accurate inference, even for high-dimensional data.

## Why It Matters

AutoBNN offers several advantages over traditional RNNs:

- **Improved performance**: cBNNs achieve state-of-the-art performance on benchmark datasets, including Daily Mail and the Netflix recommendation task.
- **Robustness**: cBNNs are robust to noise and outliers, making them suitable for data with high levels of uncertainty.
- **Computational efficiency**: cBNNs achieve efficient inference and sampling using variational inference.

These advantages make AutoBNN a promising tool for various forecasting problems, including:

- Natural language processing
- Time series analysis
- Predictive modeling

## Context & Background

AutoBNN is a recent development in probabilistic time series forecasting. The model builds upon the success of compositional models in capturing complex relationships in data. cBNNs have shown significant improvement over traditional RNNs in terms of accuracy and robustness.

AutoBNN is particularly suitable for problems with long-term dependencies, which are common in various domains, such as finance, healthcare, and climate science.

## What to Watch Next

The future research directions for AutoBNN include:

- Exploring the use of auxiliary data for training.
- Investigating the application of AutoBNN to a wider range of forecasting problems.
- Developing more efficient sampling algorithms for improving computational efficiency.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28