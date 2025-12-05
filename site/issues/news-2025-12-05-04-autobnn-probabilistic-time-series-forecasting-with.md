---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2025-12-05
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

AutoBNN is a new probabilistic time series forecasting method that can generate high-fidelity predictions for complex, high-dimensional data. It builds on the successes of AutoGAN, a generative adversarial network that can be used to learn long-range dependencies in time series data.

The new method uses a compositional Bayesian neural network (cBNN) to model the underlying relationships between variables in the data. The cBNN combines the strengths of autoencoders and normalizing flows to achieve better performance than traditional probabilistic modeling methods.

The cBNN learns a joint probability distribution of the data, which allows it to generate new samples that are similar to the training data. This enables the cBNN to generate high-fidelity forecasts, even for data that is not available during training.

## Why It Matters

AutoBNN has several important features that make it a powerful tool for time series forecasting:

* **High-fidelity predictions:** The cBNN can generate high-fidelity predictions for complex, high-dimensional data.
* **Probabilistic nature:** The cBNN is a probabilistic model, which allows it to generate new samples that are similar to the training data.
* **Joint probability distribution learning:** The cBNN learns a joint probability distribution of the data, which allows it to generate new samples that are similar to the training data.

These features make AutoBNN ideal for a wide range of time series forecasting applications, including financial markets, healthcare, and climate science.

## Context & Background

AutoBNN is a relatively new method, with the first paper published in 2024. However, the underlying concepts are closely related to other probabilistic modeling methods, such as autoencoders and normalizing flows.

The cBNN architecture is particularly well-suited for high-dimensional data. The use of a neural network to learn the joint probability distribution of the data allows the cBNN to capture complex relationships between variables.

AutoBNN has been shown to be effective on a variety of time series forecasting tasks, including stock market returns, mortgage defaults, and weather patterns. The method is particularly promising for data that is complex or high-dimensional.

## What to Watch Next

The future direction of AutoBNN is promising. The authors plan to explore the use of Bayesian optimization to improve the training process and to investigate the use of other neural network architectures, such as deep neural networks.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28