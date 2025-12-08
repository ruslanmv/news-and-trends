---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2025-12-08
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

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) for improved accuracy and interpretability. This method leverages the compositional aspect of CBNNs to incorporate prior knowledge and enhance the model's ability to capture complex temporal dependencies.

The algorithm utilizes a hierarchical structure with two levels. The first level consists of CBNNs that capture local dependencies in the data. These CBNNs are then combined in the second level, facilitating the transfer of learned knowledge across different temporal scales.

This approach significantly improves the forecasting performance compared to traditional CBNN models, achieving a reduction in Mean Squared Error (MSE) by 20%. Additionally, AutoBNN provides interpretable predictions, making it easier to understand how the model arrives at its predictions.

## Why It Matters

AutoBNN offers several key advantages over existing methods:

- Improved accuracy and interpretability: By incorporating prior knowledge and utilizing a hierarchical structure, AutoBNN provides more accurate and transparent predictions compared to traditional CBNN models.
- Enhanced performance: The algorithm outperforms other CBNN variants in terms of both accuracy and interpretability.
- Flexibility: The method can be applied to various time series data, making it versatile and applicable across different domains.

## Context & Background

AutoBNN builds upon the success of compositional neural networks (CNNs) in image processing. CBNNs have been successfully applied in time series forecasting, but their interpretability has been challenging. AutoBNN addresses this challenge by leveraging the compositional nature of CNNs to incorporate prior knowledge explicitly into the model.

The method also builds upon the growing field of interpretable AI, where models can provide insights into their predictions. By incorporating prior knowledge, AutoBNN facilitates the development of interpretable models that can be readily understood by domain experts.

## What to Watch Next

The future research directions for AutoBNN include exploring the use of attention mechanisms to enhance the model's ability to capture long-range dependencies. Additionally, investigating the integration of domain-specific knowledge into the model could lead to further improvements in accuracy and interpretability.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28