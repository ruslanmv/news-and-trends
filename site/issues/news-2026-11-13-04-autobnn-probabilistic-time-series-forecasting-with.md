---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-11-13
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

AutoBNN is a new method for probabilistic time series forecasting with compositional Bayesian neural networks. This method combines the strengths of both Autoencoders and Conditional Generative Adversarial Networks (CGANs) to produce high-fidelity forecasts for a wide range of time series data.

The key idea behind AutoBNN is to learn a representation of the data through an Autoencoder and then use this representation to perform probabilistic forecasting using a CGAN. This approach allows AutoBNN to capture both the local and global dependencies in the data, leading to more accurate forecasts than traditional time series models.

## Why It Matters

AutoBNN has several advantages over other time series forecasting methods:

* It achieves higher accuracy than other CNN-based forecasting methods on various datasets
* It is robust to noise and outliers
* It can handle high-dimensional data efficiently

The application of AutoBNN to various datasets in the financial, healthcare, and weather forecasting industries suggests its potential to revolutionize how time series data is analyzed and forecasted.

## Context & Background

AutoBNN is a relatively new method in the field of time series forecasting. However, it draws upon the strengths of both Autoencoders and CGANs. Autoencoders excel at learning compact representations of data, while CGANs are powerful for generating realistic and diverse samples from the learned representation.

AutoBNN is particularly well-suited for forecasting problems where the underlying data is high-dimensional and complex, such as financial data. The method's ability to capture both local and global dependencies in the data makes it effective for capturing complex relationships between variables.

## What to Watch Next

The future development of AutoBNN is promising, and researchers are actively exploring ways to further improve the accuracy and robustness of the method. They are also investigating the application of AutoBNN to other data types, such as image and text data.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28