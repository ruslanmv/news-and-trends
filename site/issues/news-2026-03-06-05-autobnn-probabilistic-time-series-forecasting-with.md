---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-03-06
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

AutoBNN is a new probabilistic time series forecasting model that utilizes a compositional Bayesian neural network (cBNN) to generate high-fidelity forecasts for complex systems. The model leverages the inherent probabilistic nature of cBNNs to incorporate uncertainty into the forecast process.

AutoBNN significantly improves upon previous probabilistic forecasting methods by addressing the limitations of traditional approaches, including the inability to model complex relationships between variables and the lack of uncertainty quantification.

## Why It Matters

AutoBNN offers several key advantages over existing models:

- **Robustness against noise and outliers:** cBNNs naturally handle noisy data and outliers in the input data, providing more accurate forecasts compared to traditional probabilistic methods.
- **Improved uncertainty quantification:** AutoBNN provides probabilistic uncertainty estimates, allowing users to quantify the level of prediction uncertainty, leading to more informed decision-making.
- **Flexibility and adaptability:** The model can be easily adapted to different problem settings by modifying the network architecture and hyperparameters.

## Context & Background

AutoBNN builds upon the foundations of recent advances in deep learning and Bayesian modeling. The model draws inspiration from cGANs and autoencoders, utilizing a conditional Gating Network (CGN) for conditional variable selection and a hierarchical autoencoder for feature extraction.

AutoBNN addresses the limitations of previous probabilistic forecasting methods by introducing a mechanism for robust uncertainty estimation. The model effectively balances between capturing complex system dynamics and providing a comprehensive understanding of forecast uncertainty.

## What to Watch Next

The future development of AutoBNN holds immense potential for various applications. The model has the potential to revolutionize forecasting across diverse fields, including financial markets, healthcare, and climate science.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28