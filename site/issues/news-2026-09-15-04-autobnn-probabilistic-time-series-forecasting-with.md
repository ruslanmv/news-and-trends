---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-09-15
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

AutoBNN is a new probabilistic time series forecasting method that uses compositional Bayesian neural networks (CBNNs) to learn patterns in real-time data. This method is designed to be robust and efficient, making it suitable for a wide range of applications, including fraud detection, risk assessment, and supply chain management.

The core idea of AutoBNN is that it combines the strengths of CBNNs and probabilistic modeling to achieve accurate time series forecasting. CBNNs are deep neural networks that can learn complex relationships in data, while probabilistic modeling allows for uncertainty and missing data, which are common in real-world datasets.

AutoBNN uses a hierarchical structure to represent the dependencies between variables. At the bottom level, it consists of CBNNs that learn local relationships in the data. At the next level, the CBNNs are connected to each other through a global attention mechanism. This attention mechanism allows the network to learn long-range dependencies and capture complex patterns in the data.

The model is also robust to noise and outliers. This is achieved through the use of a dropout layer and a set of robust loss functions. The loss functions are designed to penalize models that deviate from the true underlying patterns in the data.

## Why It Matters

AutoBNN is a significant advancement in probabilistic time series forecasting due to the following reasons:

- **Robustness:** CBNNs are known to be robust to noise and outliers, making them suitable for real-world applications where data is often noisy or contains outliers.
- **Efficiency:** The hierarchical structure and attention mechanism allow AutoBNN to learn complex patterns in data while maintaining efficiency.
- **Versatility:** The model can be used for a wide range of applications, including fraud detection, risk assessment, and supply chain management.

The improved accuracy and efficiency of AutoBNN have the potential to revolutionize how businesses make decisions and predict market outcomes.

## Context & Background

AutoBNN is a recent breakthrough in artificial intelligence, specifically in the field of time series forecasting. The model draws upon the strengths of both CBNNs and probabilistic modeling to achieve improved results.

The model was developed by a team of researchers from Google AI. The team has a long history of developing innovative AI systems, including AlphaFold and Autoencoders.

AutoBNN builds upon the foundational work of CBNNs, a popular type of neural network for learning representations in data. However, it introduces a new hierarchical structure and attention mechanism that allows it to learn complex patterns in data with high accuracy and efficiency.

The model has been successfully applied to a variety of real-world datasets, achieving state-of-the-art results. It has the potential to revolutionize how businesses make decisions and predict market outcomes.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28