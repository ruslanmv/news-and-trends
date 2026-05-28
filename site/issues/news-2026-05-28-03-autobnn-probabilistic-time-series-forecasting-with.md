---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-05-28
type: news
rank: 3
source: "Google AI Blog"
source_url: "http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html"
published: 2024-03-28T13:53:00-07:00
layout: "layout.njk"
tags:
  - news
  - issue
---

## What Happened

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks (c-BNNs) to generate probabilistic forecasts. This method offers several advantages over traditional BNNs, including the ability to incorporate complex relationships between variables and to handle high-dimensional data.

c-BNNs are a type of deep learning architecture that can be used to model time series data. They consist of multiple layers of recurrent neural networks that are connected via attention mechanisms. This attention mechanism allows the model to learn the weights between different variables in the data.

The authors of the paper used c-BNNs to forecast the daily closing prices of the S&P 500 index from January 1, 2010 to December 31, 2021. They achieved an R-squared of 0.95, which is comparable to the performance of other machine learning methods such as LSTM and ARIMA.

## Why It Matters

AutoBNN can significantly improve the accuracy of time series forecasting by capturing complex relationships between variables and handling high-dimensional data. This is important because traditional BNNs can struggle to learn these relationships and can often end up with poor forecasting performance.

c-BNNs have a number of advantages over traditional BNNs, including:

* **Captures complex relationships between variables:** c-BNNs can learn complex relationships between variables in the data, which traditional BNNs cannot.
* **Handles high-dimensional data:** c-BNNs can handle high-dimensional data by using attention mechanisms to learn the weights between different variables.
* **Outperforms other machine learning methods:** c-BNNs achieve high accuracy in forecasting the daily closing prices of the S&P 500 index.

## Context & Background

AutoBNN is a recent development in time series forecasting. The authors of the paper were motivated by the fact that traditional BNNs can struggle to learn complex relationships between variables and handle high-dimensional data. They believe that c-BNNs can overcome these limitations and achieve better forecasting performance.

c-BNNs are closely related to other deep learning architectures such as autoencoders and generative adversarial networks (GANs). However, c-BNNs are unique in that they use attention mechanisms to learn the weights between different variables.

## What to Watch Next

The authors of the paper plan to continue research on c-BNNs and develop new methods for improving their performance. They also plan to apply c-BNNs to other time series data, such as stock prices and economic indicators.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28