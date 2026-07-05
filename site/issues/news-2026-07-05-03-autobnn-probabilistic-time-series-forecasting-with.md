---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-07-05
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

AutoBNN is a novel probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) to generate probabilistic forecasts. This approach allows for a more flexible and robust forecasting approach compared to traditional methods that rely on deterministic neural networks.

The key idea behind AutoBNN is to represent the underlying process dynamics as a latent space with a set of latent variables. CBNNs are then used to learn this latent space and generate probabilistic forecasts by sampling from the learned distribution.

The method has been successfully applied to various time series forecasting problems, including stock market returns, economic indicators, and system failures. It achieves significantly improved forecast accuracy and robustness compared to traditional methods, particularly when dealing with high-dimensional and complex data.

## Why It Matters

AutoBNN holds significant importance in the field of time series forecasting due to the following reasons:

- **Flexibility:** CBNNs allow for a high degree of flexibility in modeling the underlying process dynamics, enabling the model to capture complex and nonlinear relationships in the data.
- **Robustness:** CBNNs are robust to outliers and noise in the data, making them more resilient to real-world applications.
- **Improved accuracy:** Empirical results demonstrate that AutoBNN outperforms traditional forecasting methods in terms of accuracy and robustness.

## Context & Background

AutoBNN is a relatively new method, having been published in the Google AI blog in March 2024. The authors have extensive experience in developing and applying deep learning techniques for time series forecasting. The method draws upon the strengths of CBNNs, which have been shown to be effective in modeling complex and high-dimensional data.

## What to Watch Next

The future direction for AutoBNN research involves exploring the use of advanced regularization techniques to further enhance the model's performance. Additionally, investigating the application of AutoBNN to other forecasting problems in different industries is an exciting area for further exploration.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28