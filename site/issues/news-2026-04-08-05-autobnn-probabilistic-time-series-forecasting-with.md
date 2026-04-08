---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-04-08
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

AutoBNN is a new probabilistic time series forecasting model that can generate continuous, accurate predictions for time series data. This model builds upon AutoNLP by introducing a compositional approach to generate the underlying signal, capturing complex relationships between variables.

The model consists of two components: a recurrent neural network (RNN) for generating the baseline signal and a conditional random neural network (CRNN) for generating the noise. This architecture allows the model to capture both the long-term dependencies and the high-frequency dynamics of the underlying signal.

AutoBNN was developed by researchers at Google AI and has been shown to achieve state-of-the-art performance on various forecasting tasks, including stock market, economic, and financial data.

## Why It Matters

AutoBNN is a significant advancement in probabilistic time series forecasting due to its ability to generate accurate predictions while capturing complex relationships between variables. This model is particularly suitable for high-dimensional data with long-term dependencies, which are common in various applications such as financial forecasting, climate modeling, and biological data analysis.

The model's composable architecture allows researchers to integrate different components and customize the model to address specific research questions. This flexibility makes it a powerful tool for various forecasting problems.

## Context & Background

AutoBNN is a recent breakthrough in probabilistic time series forecasting. The model builds upon previous work on AutoNLP, which introduced the concept of symbolic regression for generating high-dimensional time series data.

AutoBNN also draws upon the field of conditional random fields, which are a powerful tool for modeling complex relationships between variables. By incorporating conditional random fields into the model, AutoBNN can learn how the underlying signal affects the noise, improving the accuracy of the forecasts.

AutoBNN is a significant addition to the field of machine learning, offering a powerful and flexible model for generating accurate and reliable time series forecasts.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28