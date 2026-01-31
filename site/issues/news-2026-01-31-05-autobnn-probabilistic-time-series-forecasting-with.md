---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-01-31
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

AutoBNN is a new method for probabilistic time series forecasting with compositional Bayesian neural networks. This method combines the strengths of both traditional Bayesian networks and deep learning by using a novel approach to represent the underlying data distribution.

The model is particularly well-suited for long-horizon forecasting tasks, where traditional Bayesian networks can struggle due to the curse of dimensionality. AutoBNN overcomes this problem by using a new sampling technique that efficiently samples from the posterior distribution.

## Why It Matters

AutoBNN offers several advantages over traditional Bayesian networks, including:

* **Improved performance on long-horizon forecasting tasks.**
* **Robustness to noise and outliers.**
* **Flexibility for different data types.**

This makes it particularly well-suited for forecasting problems in diverse domains such as finance, healthcare, and climate.

## Context & Background

AutoBNN is a recent development in Bayesian time series forecasting, with the first public implementation in 2024. The model has been extensively evaluated on various datasets, demonstrating significant improvements in accuracy compared to traditional Bayesian networks.

AutoBNN builds upon the idea of conditional normalizing flows (cNFs), a class of neural networks that can be used to approximate complex probability distributions. cNFs are particularly well-suited for high-dimensional data, which is common in financial and climate applications.

## What to Watch Next

The future research direction for AutoBNN involves exploring the use of reinforcement learning to further improve the model's performance. Additionally, investigating the applicability of AutoBNN to real-world forecasting problems in different domains is an active area of investigation.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28