---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-08-23
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

AutoBNN is a novel probabilistic time series forecasting technique that leverages compositional Bayesian neural networks (CNNs) to achieve improved accuracy over traditional recurrent neural networks (RNNs). This method employs a compositional approach by representing time series data as a sequence of independent, locally stationary processes. This allows AutoBNN to capture both the temporal dependencies and the structural patterns within the data, leading to enhanced forecasting performance.

## Why It Matters

AutoBNN offers several key advantages over traditional RNNs:

* **Improved accuracy:** Empirical results demonstrate that AutoBNN outperforms RNNs in forecasting various time series tasks, including stock prices, commodity prices, and economic indicators.
* **Capture of temporal and structural dependencies:** The compositional approach allows AutoBNN to learn complex temporal relationships and structural patterns within the data, leading to more accurate predictions.
* **Reduced computational cost:** AutoBNN's compositional structure reduces the computational complexity compared to RNNs, making it suitable for real-time applications.

## Context & Background

AutoBNN builds upon the success of CBOW (Conditional Random Fields with Bayesian Optimization), another CNN-based approach for time series forecasting. CBOW utilizes a conditional random field framework to model the dependence between different time series. However, AutoBNN introduces a new component: the compositional structure.

This compositional approach offers several advantages:

* **Independence within and dependence between variables:** CBOW focuses on capturing the conditional independence between variables within a time series.
* **Temporal dependence captured implicitly:** The compositional structure implicitly captures the temporal dependencies between variables, leading to a more accurate representation of complex relationships.

The incorporation of the compositional structure allows AutoBNN to achieve improved forecasting accuracy while maintaining computational efficiency.

## What to Watch Next

Researchers are actively exploring the potential of AutoBNN for various forecasting applications. Future work includes:

* **Developing more efficient training algorithms:** Optimizing the training process to improve computational efficiency.
* **Exploring the use of AutoBNN for multivariate time series forecasting.**
* **Evaluating the applicability of AutoBNN in different financial and economic domains.**

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28