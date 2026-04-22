---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-04-22
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

AutoBNN is a novel probabilistic time series forecasting model that utilizes compositional Bayesian neural networks (CBNNs) for generating probabilistic forecasts for time series data. This approach addresses the limitations of traditional recurrent neural networks (RNNs) by capturing the spatial dependencies and latent variables in the data through a compositional approach.

CBNNs are an extension of the deep Bayesian belief networks (DBNs) framework, which has been successfully applied to various time series forecasting tasks. Unlike DBNs, CBNNs incorporate a generative component that allows them to sample new time series trajectories from the posterior distribution of the underlying data.

The model is particularly suitable for data with long memory and high dimensionality, as it effectively captures the complex temporal dependencies between variables. Moreover, its ability to generate new trajectories enables it to generate more accurate forecasts compared to traditional RNNs.

## Why It Matters

AutoBNN significantly advances the field of time series forecasting by achieving:

- Improved accuracy and generalization performance compared to conventional RNNs
- Reduced computational cost by leveraging a simpler architecture
- Ability to generate new time series trajectories, enabling more flexible forecasting

This advancement has the potential to revolutionize various industries, including finance, logistics, and healthcare, where real-time forecasting is crucial for decision-making.

## Context & Background

AutoBNN builds upon the successful application of CBNNs to sparse regression problems. By leveraging a compositional approach, it can effectively handle high-dimensional data with complex temporal dependencies. Furthermore, its generative component allows it to generate new time series trajectories, enabling more flexible forecasting.

The authors acknowledge the limitations of CBNNs and propose a two-stage learning approach to improve their performance. The first stage focuses on learning the latent variables in the data, while the second stage utilizes these learned latent variables to generate new trajectories.

## What to Watch Next

The development of AutoBNN holds significant implications for various fields, including finance and logistics. With its improved accuracy and computational efficiency, it has the potential to transform real-time forecasting by enabling more accurate decision-making under uncertainty.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28