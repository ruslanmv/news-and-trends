---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-07-02
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

AutoBNN is a novel probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (CBNNs) to generate probabilistic forecasts. Unlike traditional CBNNs, which rely on sequential data, AutoBNN can handle multiple time series simultaneously and jointly, making it suitable for forecasting complex systems.

The model is based on the idea that time series data can be represented as a composition of simpler, underlying components. CBNNs are particularly well-suited for this task, as they can automatically discover and learn these underlying components from the data.

The AutoBNN architecture consists of three main components:

- **Input layer**: This component receives the multiple time series data as input and projects them onto the underlying components.
- **Hidden layers**: These layers learn the representations of the underlying components from the input data.
- **Output layer**: This component combines the learned representations to generate the final forecast.

The model is trained using a variational inference approach, which allows the parameters of the CBBNs to be learned automatically from the data. This approach is particularly effective for high-dimensional data, where traditional CBNNs can become computationally expensive.

## Why It Matters

AutoBNN has several key advantages over traditional CBNNs:

* **Parallelism**: CBNNs are inherently sequential, but AutoBNN can handle multiple time series simultaneously, making it significantly faster than traditional CBNNs for high-dimensional data.
* **Robustness**: CBNNs are robust to changes in the data, which can lead to improved forecasts in dynamic environments.
* **Interpretability**: The learned representations in AutoBNN are interpretable, which allows us to understand how the model makes predictions.

These advantages make AutoBNN a promising method for forecasting complex time series data. It has the potential to improve the accuracy and robustness of forecasters in various domains, including finance, healthcare, and manufacturing.

## Context & Background

AutoBNN is a relatively new method, with the first paper describing it in 2024. However, it builds upon the foundations of CBBNs, which have been successfully applied to various forecasting tasks.

AutoBNN is particularly well-suited for problems where the data is high-dimensional and complex. This is because CBNNs can automatically discover and learn the underlying components from the data, which can make them more accurate than traditional CBNNs that rely on explicit hand-picking of components.

Traditional CBNNs can be computationally expensive due to their sequential nature. However, AutoBNN uses a variational inference approach that allows the parameters of the CBBNs to be learned automatically from the data. This approach significantly reduces computational requirements while maintaining model accuracy.

## What to Watch Next

The research team is actively working on improving the performance of AutoBNN. They are currently exploring the use of additional regularization techniques and optimizing the learning process to further enhance the model's accuracy and robustness.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28