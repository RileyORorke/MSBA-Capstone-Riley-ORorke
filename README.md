# MSBA Capstone: Predictive Maintenance for Tool Wear Using Bore Measurements

## Project Overview
This repository contains the implementation of a predictive maintenance model designed to forecast tool wear in machining centers based on bore measurement trends. The goal of this project is to transition from reactive maintenance, where tools are replaced only after exceeding tolerance limits, to a predictive approach that leverages machine learning and time series analysis to forecast wear trends before failures occur.

By analyzing historical bore measurements, this model provides early alerts for excessive wear, helping manufacturers reduce downtime, optimize tool lifespan, and improve machining precision. The project integrates a Random Forest Regressor for predictive modeling and is deployed within a Power BI dashboard for real-time monitoring.

## Key Features
* Forecasts bore measurements for the next 10 cycles using machine learning.  
*  Classifies wear states based on predicted bore measurement changes (Normal, Moderate, or Critical Wear).  
*  Identifies gradual wear trends to optimize tool replacement schedules.  
*  Reduces unplanned downtime by enabling proactive maintenance.  
*  Integrated into Power BI for real-time visualization of tool health.  

## Data & Preprocessing
The dataset consists of bore measurements recorded over machining cycles, including:  
  
* Timestamps for each bore measurement.  
* Bore diameter readings as a proxy for tool wear.  
* Min/Max bore tolerances from operator instructions.  
* Cycle count to track tool usage over time.  

## Data Cleaning & Feature Engineering
* Removed outliers using tolerance-based filtering and IQR analysis.  
* Generated lag features (previous bore measurements) to model wear progression.  
* Computed rolling statistics (mean & standard deviation) to capture long-term trends.  
* Standardized cycle count as a proxy for tool degradation.  

## Power BI Integration  
The model is deployed in Power BI, where bore measurement forecasts and wear classifications are visualized in real-time.  

* Data cards display tool wear states for each machining center.  
* Predictive alerts notify maintenance teams of potential tool failures.  
* Trend analysis charts track bore size progression over cycles.  