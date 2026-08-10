---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-08-10
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

AutoBNN is a novel probabilistic time series forecasting technique that utilizes a novel composition-based Bayesian neural network (CBBNN) to predict future values. This approach offers several advantages, including superior performance compared to traditional parametric models.

The key idea behind CBBNN is to decompose the time series into a hierarchy of hierarchical components. Each component is modeled by a separate CBBN, which is a more efficient and flexible variant of standard Bayesian neural networks. This approach allows CBBNN to capture complex dependencies and non-linear relationships in the data, leading to improved forecasting accuracy.

The model is specifically designed for forecasting continuous-valued time series. It utilizes a hierarchical structure with an outer CBBN layer responsible for generating long-term dynamics, and an inner CBBN layer for capturing short-term dependencies. This architecture effectively captures the interplay between different time series levels and allows for accurate forecasting across different time scales.

## Why It Matters

CBBNN offers several significant advantages over traditional parametric time series models. Firstly, it achieves higher forecasting accuracy by capturing complex relationships and dependencies in the data. This makes it particularly effective for forecasting time series with high noise levels or when the underlying dynamics are complex.

Secondly, CBBNN is computationally efficient, making it suitable for real-time applications. It utilizes a hierarchical structure that allows for parallel processing and reduces the computational complexity compared to traditional CBBN approaches.

Thirdly, CBBNN is robust to outliers and noise. This is achieved by employing a robust CBBN architecture that can effectively handle outliers and uncertainties in the data.

## Context & Background

AutoBNN is a relatively new technique, having been developed in 2024. However, it builds upon the foundations of CBBNs, which have been successfully applied to various time series forecasting problems.

The model's architecture is particularly well-suited for forecasting continuous-valued time series due to its hierarchical structure and focus on capturing long- and short-term dependencies. This approach allows CBBNN to leverage the strengths of CBBNs while addressing the challenges associated with forecasting continuous-valued data.

## What to Watch Next

The development of CBBNN is ongoing, and researchers are actively exploring its applicability to different forecasting problems. The authors are planning to compare CBBNN with other state-of-the-art time series forecasting techniques on various datasets to demonstrate its superior performance. Additionally, they aim to investigate the use of CBBNN for forecasting discrete-valued time series.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28