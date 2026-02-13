---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-02-13
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

AutoBNN is a new probabilistic time series forecasting model that utilizes compositional Bayesian neural networks (cBNNs) to generate probabilistic forecasts. This model builds on top of traditional LSTMs and is particularly effective for forecasting long-term dependencies in time series data.

The cBBN architecture consists of two main components: a recurrent neural network (RNN) and a variational autoencoder (VAE). The RNN captures long-term dependencies in the data through a self-attention mechanism, while the VAE compresses the data into a latent representation, promoting a better understanding of the underlying structure.

The model is trained using a variational inference approach, where the latent representation of the data is used to guide the generation of new samples. This approach allows the model to capture complex and diverse patterns in the data, leading to improved forecast accuracy.

The authors demonstrate the effectiveness of AutoBNN on various financial time series data, including stock prices, foreign exchange rates, and commodity prices. They show that the model can achieve significant improvements in forecast accuracy compared to other machine learning methods, such as LSTMs and ARIMA models.

## Why It Matters

AutoBNN has several important implications for the financial industry. First, the model can provide more accurate forecasts of complex financial time series, leading to improved risk management and portfolio optimization. Second, the model can facilitate the development of new financial products and services by enabling the creation of customized portfolios based on individual risk preferences. Third, the model can contribute to a deeper understanding of financial markets by providing insights into the underlying relationships between different assets.

## Context & Background

AutoBNN is a relatively new model in the field of time series forecasting. However, it builds upon the foundation of LSTMs, which have been successful in other forecasting tasks. cBNNs, in particular, have proven to be effective for capturing long-term dependencies in time series data.

The model's architecture and training approach also align with the recent trend of using deep learning techniques for time series analysis. This approach has shown to be highly effective in recent years, and AutoBNN is an example of how deep learning can be applied to this challenging problem.

## What to Watch Next

The future development of AutoBNN is promising. The authors plan to explore the use of other data augmentation techniques to improve the model's generalization ability. They also intend to investigate the integration of AutoBNN with other machine learning techniques, such as reinforcement learning.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28