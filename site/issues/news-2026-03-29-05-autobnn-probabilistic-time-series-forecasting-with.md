---
title: "AutoBNN: Probabilistic time series forecasting with compositional bayesian neural networks"
date: 2026-03-29
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

AutoBNN is a new probabilistic time series forecasting method that utilizes compositional Bayesian neural networks to generate probabilistic predictions for a wide range of time series datasets. This approach combines the strengths of both Bayesian networks and recurrent neural networks, enabling AutoBNN to capture complex temporal dependencies and generate more accurate forecasts than traditional time series forecasting methods.

The model is particularly suitable for datasets with non-stationary or irregularly spaced data, where traditional time series methods may struggle to generate reliable forecasts. Additionally, AutoBNN is robust to outliers and can handle high-dimensional data efficiently.


## Why It Matters

AutoBNN has several potential benefits over other time series forecasting methods:

* **Improved accuracy:** By incorporating both temporal dependencies and the ability to handle high-dimensional data, AutoBNN can generate more accurate forecasts than traditional methods.
* **Robustness to outliers:** The model is less sensitive to outliers in the data, making it more robust to real-world scenarios where such disturbances are common.
* **Efficient handling of high-dimensional data:** Traditional time series methods can become computationally expensive as the number of features increases. AutoBNN, on the other hand, is efficient in handling high-dimensional data by using a sparse formulation that can be easily inverted.

## Context & Background

AutoBNN is a recent advancement in probabilistic time series forecasting, with the first version of the model published in the Google AI Blog in March 2024. The authors of the paper demonstrate the effectiveness of AutoBNN on a variety of datasets, including financial, economic, and meteorological data.

The paper also highlights the importance of addressing the challenges posed by non-stationarity and high-dimensional data in time series analysis. Traditional time series methods may struggle to generate accurate forecasts in these scenarios, while AutoBNN demonstrates significant improvement in terms of accuracy and robustness.

## What to Watch Next

The future of AutoBNN is promising, with the authors indicating plans to explore the use of more advanced sampling methods and the development of ensemble forecasting techniques. Additionally, they plan to investigate the application of AutoBNN to other domains, such as healthcare and finance.

---

**Source**: [Google AI Blog](http://blog.research.google/2024/03/autobnn-probabilistic-time-series.html) | Published: 2024-03-28