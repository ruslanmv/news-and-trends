---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-05-29
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

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks. This method offers several advantages over traditional recurrent neural networks (RNNs), including better temporal dependence modeling and superior interpretability.

The authors propose two key improvements for RNNs: (1) a novel attention mechanism that focuses on recent past observations, and (2) a hierarchical structure that captures long-term dependencies in the data.

AutoBNN is evaluated on various datasets, including financial, economic, and climate data. Results demonstrate that AutoBNN achieves state-of-the-art performance compared to other time series forecasting methods.

## Why It Matters

AutoBNN's improved performance stems from several factors. First, the attention mechanism allows the model to focus on relevant past observations, capturing long-term dependencies that are often missed by traditional RNNs. Second, the hierarchical structure facilitates the extraction of complex relationships between different parts of the data.

The application of AutoBNN to diverse datasets suggests potential applications in various fields, including finance, economics, and climate science.

## Context & Background

AutoBNN is a recent advancement in time series forecasting methods. The authors draw upon the successes of compositional neural networks, which have achieved remarkable performance in image and speech recognition. They further leverage the strengths of attention mechanisms, which have been successful in recent research on RNNs.

This combined approach provides a powerful tool for capturing both temporal dependencies and long-term relationships in data.

## What to Watch Next

AutoBNN is a promising method for improving time series forecasting. The authors plan to explore the use of AutoBNN on more challenging datasets, such as those with missing values or high dimensionality. Additionally, they intend to investigate the use of other attention mechanisms and hierarchical structures to further enhance the model's performance.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28