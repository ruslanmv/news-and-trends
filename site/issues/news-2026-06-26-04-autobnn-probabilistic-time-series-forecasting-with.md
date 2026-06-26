---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-06-26
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

AutoBNN is a new probabilistic time series forecasting model that utilizes a compositional Bayesian neural network (cBNN) to generate synthetic data with realistic statistical properties. It is particularly useful for generating synthetic data with complex temporal dependencies, a challenge in traditional time series forecasting methods.

The cBNN utilizes conditional random fields to model the underlying structure of the data. This allows it to generate data that closely resembles real-world data while being easier to learn than other generative models.

The model was developed by a team of researchers at Google AI and has been shown to generate high-quality synthetic data with various statistical properties, making it a promising tool for various applications such as:

* **Financial modeling:** Generating realistic stock prices and market dynamics.
* **Data-driven simulations:** Creating synthetic data for complex systems, such as economic models or physical systems.
* **Drug discovery:** Identifying potential drug candidates by generating realistic drug-like molecules.


## Why It Matters

By enabling the generation of realistic synthetic data, AutoBNN has several key benefits:

- **Reduced reliance on real data:** Traditional time series forecasting methods often rely on historical data, which can be limited or incomplete. AutoBNN can generate data that better reflects the underlying dynamics of the system being modeled.
- **Improved model accuracy:** The cBNN framework allows for the specification of complex relationships between variables, leading to more accurate models.
- **Enhanced interpretability:** The model's internal structure and decision-making process can be understood and analyzed, leading to greater transparency and trust.


## Context & Background

AutoBNN builds upon previous work in Bayesian neural networks, which have been successful in generating synthetic data with various statistical properties. The cBNN framework introduces several novel ideas, including the use of conditional random fields and the incorporation of a hierarchical structure in the model.

AutoBNN is particularly well-suited for generating data with complex temporal dependencies, which are common in various scientific and engineering fields. This makes it a valuable tool for researchers and practitioners working in areas such as finance, artificial intelligence, and materials science.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28