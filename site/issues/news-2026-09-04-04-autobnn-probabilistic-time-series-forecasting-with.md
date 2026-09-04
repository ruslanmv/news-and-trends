---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-09-04
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

AutoBNN is a novel probabilistic time series forecasting technique that utilizes compositional Bayesian neural networks (CBNNs) to generate accurate probabilistic forecasts. This approach combines the strengths of CBNNs, which excel in capturing complex, long-term dependencies in data, with the interpretability and flexibility of traditional probabilistic forecasting methods.

The core idea behind AutoBNN is that it decomposes the dependence structure of the data into a hierarchy of independent components. These components are then represented as CBNNs, which are trained to learn the relationships between the variables in the data.

The training process of AutoBNN involves maximizing the conditional evidence lower bound (CELB), which measures the evidence gained by conditioning on additional variables. This leads to the discovery of functionally relevant relationships between the variables in the data.

The resulting CBNN-based model can generate probabilistic forecasts by sampling from the posterior distribution of the target variable. This allows for the incorporation of prior knowledge and uncertainty estimation into the forecasting process.

## Why It Matters

AutoBNN offers several advantages over traditional forecasting methods:

- **Interpretability:** The CBNN architecture allows for the visualization of the relationships between the variables in the data, facilitating a deeper understanding of the forecasting process.
- **Flexibility:** The model can be easily extended to different data types and problem structures by modifying the architecture of the CBNN layers.
- **High accuracy:** AutoBNN has been shown to achieve state-of-the-art accuracy on various forecasting benchmarks, including stock market and economic data.

The novel approach has the potential to revolutionize time series forecasting by providing a more accurate, interpretable, and flexible solution compared to traditional methods.

## Context & Background

AutoBNN is a recent breakthrough in time series forecasting, leveraging the power of CBNNs to capture complex and long-term dependencies. The technique has shown significant improvements in accuracy and interpretability compared to traditional forecasting methods.

The development of AutoBNN is closely tied to the advancements in artificial intelligence and machine learning, where CBNNs have demonstrated remarkable performance in various tasks. The research team behind AutoBNN consists of experts in machine learning, statistics, and financial mathematics, bringing together diverse skills and expertise.

## What to Watch Next

The future direction of research lies in exploring the use of AutoBNN on more complex and high-dimensional data. Additionally, investigating the integration of additional data sources and improving the model's interpretability are areas of active exploration.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28