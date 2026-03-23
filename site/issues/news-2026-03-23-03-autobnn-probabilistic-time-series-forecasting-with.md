---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-03-23
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

AutoBNN is a novel probabilistic time series forecasting technique that utilizes compositional Bayesian neural networks (CBNNs) for anomaly detection and outlier identification. The technique builds upon the existing CBNN framework by incorporating a probabilistic approach that allows the model to account for both the deterministic and stochastic aspects of the underlying data. This approach results in improved robustness and accuracy in identifying anomalies.

## Why It Matters

AutoBNN offers several advantages over traditional CBNNs, including:

* **Robustness:** CBNNs are known to be sensitive to overfitting and parameter initialization. AutoBNN addresses this by employing a probabilistic approach that encourages the model to explore a wide range of possible parameter combinations, leading to increased robustness.
* **Stochasticity:** CBNNs typically rely on specific parameter distributions for training. However, AutoBNN allows for the incorporation of arbitrary probability distributions, enabling it to capture the inherent stochasticity of real-world data.
* **Anomaly detection:** AutoBNN utilizes a novel anomaly detection strategy that focuses on identifying anomalies in the tails of the probability distribution. This approach allows the model to capture both the local and global anomalies, resulting in improved accuracy.

## Context & Background

AutoBNN is particularly suitable for financial time series analysis, where dealing with rare and extreme events is crucial. By leveraging a probabilistic approach, AutoBNN can effectively handle such challenging data, leading to more reliable anomaly detection.

## What to Watch Next

The research team plans to conduct further experiments to optimize the model's hyperparameters and explore the potential of incorporating additional data sources. They also intend to investigate the generalization performance of AutoBNN on a wider range of datasets.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28