---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-09-20
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

AutoBNN is a novel probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) to generate probabilistic forecasts. This approach tackles the limitations of traditional recurrent neural networks (RNNs) by jointly modeling both the state dependence and the temporal dependence in a single model.

The method employs a hierarchical architecture, with the CBNN serving as the core predictor. It incorporates a recurrent neural network (RNN) for temporal dependencies and a Bernoulli neural network (BNN) for capturing state dependencies.

AutoBNN achieves superior performance compared to existing methods in terms of accuracy and diversity of generated forecasts. This is particularly evident in long-term forecasting tasks, where the RNN and BBN components effectively complement each other.

## Why It Matters

AutoBNN offers significant advancements in probabilistic time series forecasting by:

* **Joint modeling of dependencies:** CBNN captures both temporal and state dependencies in a unified framework.
* **Improved accuracy and diversity:** By leveraging the strengths of both the RNN and BNN, AutoBNN generates more accurate and diverse forecasts.
* **Enhanced computational efficiency:** The hierarchical structure and the use of BNNs allow for efficient training and inference.

## Context & Background

AutoBNN builds upon the foundations of CBNNs and RNNs. CBNNs have successfully captured temporal dependencies in various domains, while RNNs excel in capturing state dependencies. By combining these two approaches, AutoBNN presents a novel and effective solution for time series forecasting.

The method has the potential to revolutionize various applications, including financial forecasting, weather forecasting, and healthcare data analysis. Its ability to generate accurate and diverse forecasts opens up new possibilities for decision-making and problem-solving.

## What to Watch Next

Researchers are actively exploring the potential of AutoBNN and its applications in different domains. The development of ensemble methods and the investigation of novel regularization techniques are ongoing areas of investigation. As the field of probabilistic time series forecasting continues to evolve, AutoBNN is poised to make significant contributions to the future of data analytics.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28