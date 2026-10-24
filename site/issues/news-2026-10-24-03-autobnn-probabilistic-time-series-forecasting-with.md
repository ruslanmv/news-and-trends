---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-10-24
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

AutoBNN is a novel probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) to achieve improved forecasting accuracy and interpretability compared to traditional methods. 

The proposed model utilizes a novel approach to CBBN by incorporating a hierarchical structure that allows the model to capture both temporal dependencies and spatial dependencies within the data. This hierarchical structure is particularly effective in handling high-dimensional and irregularly structured data.

CBBNs leverage the power of conditional random fields (CRFs) to capture the spatial and temporal dependencies between various time series. This enables the model to learn complex relationships in the data that may not be captured by traditional CBBN methods.

The authors demonstrate the effectiveness of AutoBNN on various time series forecasting tasks, including stock market returns, economic indicators, and weather patterns. They achieve significant improvements in forecasting accuracy compared to traditional CBBN methods, highlighting the potential of this novel approach.


## Why It Matters

AutoBNN offers several advantages over traditional CBBN methods:

- Improved forecasting accuracy through the hierarchical structure that captures both spatial and temporal dependencies
- Enhanced interpretability due to the explicit representation of relationships between time series
- Applicability to high-dimensional and irregularly structured data

The model's improved performance on various forecasting tasks suggests its potential to be a valuable tool for various industries and domains.

## Context & Background

AutoBNN is a recent breakthrough in probabilistic time series forecasting. The authors draw upon the strengths of CBBNs to develop a model that consistently outperforms traditional methods. The hierarchical structure is particularly beneficial for high-dimensional and irregularly structured data.

The model's ability to capture both spatial and temporal dependencies makes it particularly suitable for forecasting complex economic and financial time series. The authors also leverage the power of CRFs to achieve high accuracy, highlighting the importance of this technique in capturing complex relationships in time series data.

## What to Watch Next

The authors plan to further investigate the application of AutoBNN to more complex forecasting problems, such as multi-horizon time series and time series with missing data. Additionally, they aim to explore the use of other regularization techniques to improve the model's robustness.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28