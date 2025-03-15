# MSBA Capstone: Predictive Maintenance for Tool Wear Using Bore Measurements

## Project Overview
The objective of this project is to develop a predictive data model that forecasts bore measurements for future cycles in a machining center. This will help with the predictive maintenance of tool heads, allowing for proactive management of tool wear and improving overall efficiency in the manufacturing process.

The model is designed for one toolhead but is intended to be expanded to handle multiple toolheads within the machining center. Each toolhead will have its own dataset, and the model will be dynamically trained to capture the unique trends of each toolhead.

This repository contains all necessary code, notebooks, and supporting files to build and evaluate the predictive maintenance model. The final output will be used in PowerBI to create a dashboard for monitoring toolhead conditions and predicting the need for maintenance.

## **Problem Statement**

Tool wear in a machining center can significantly impact the efficiency of manufacturing operations, leading to costly downtime and suboptimal tool performance. However, predicting when a toolhead will require maintenance is challenging due to the dynamic nature of tool wear and the limited data available, which often lacks clear patterns.

This project addresses the problem by:

- **Forecasting future bore measurements** based on historical data, which serves as an indicator of tool wear.
- **Classifying tool wear stages** (Normal, Moderate, Critical) based on the predicted changes in bore size, helping identify maintenance needs.
- **Providing a predictive maintenance dashboard** in Power BI for real-time monitoring of toolhead conditions.

By offering a data-driven approach to tool wear forecasting and maintenance scheduling, this system allows manufacturing teams to proactively manage tool life, reducing downtime and enhancing operational efficiency.

## Data Source

#### `Source_Capstone_Data.xlsx`
The dataset used in this project contains measurements of bore sizes for a single toolhead over time. This data will be used to train a model to forecast future bore sizes and classify wear stages based on those predictions.

As part of the future expansion, each toolhead in the machining center will have its own dataset. The model will adapt dynamically to these datasets to account for individual trends of each toolhead.

## Repository Structure

### /data
- **Source_Capstone_Data.xlsx**: Raw dataset containing bore measurement values for a single toolhead. This file serves as the primary input for the predictive model.
- **rfr_future_wear_predictions.xlsx**: Excel file that stores predictions of future bore measurements based on the Random Forest Regressor model.

### /code_submissions
- **submission_1_model_eval_ororke_20250301.py**: Python script used to evaluate the performance of the Random Forest model through various statistical metrics.
- **submission_2_outlier_removal_ororke_20250301.py**: Python script that implements outlier removal using the Interquartile Range (IQR) method, ensuring data quality before model training.
- **submission_3_bore_size_predictor_ororke_20250301.py**: Python script for predicting future bore sizes based on historical data and feature engineering.
- **submission_4_file_handling_ororke_20250301.py**: Python script that handles the input and output operations for the dataset, ensuring smooth data management throughout the modeling process.
- **submission_5_wear_class_logic_ororke_20250301.py**: Python script that classifies wear stages based on predicted changes in bore size, categorizing tool wear into Normal, Moderate, and Critical stages.

### /data_model_development
- **data_model_development_ororke_20250215_v1.ipynb**: Jupyter notebook documenting the early stages of machine learning model development, with an initial focus on the Random Forest Regressor model.
- **data_model_development_ororke_20250301_v2.ipynb**: Stylized Jupyter notebook presenting model development for the Random Forest Regressor, intended for integration with Power BI.
- **data_model_development_ororke_20250302_v3.ipynb**: Jupyter notebook focused on the exploration of alternative prediction models, with an emphasis on ARIMA-based forecasting.
- **data_model_development_ororke_20250315_v4.ipynb**: Stylized Jupyter notebook detailing the development and testing of the ARIMA model for time-series forecasting of bore measurements.
- **data_model_development_ororke_20250315_v5.ipynb**: Jupyter notebook documenting the refinement of the Random Forest Regressor model with enhanced feature engineering and model tuning.
- **final_data_model_ororke_20250315.ipynb**: Finalized Jupyter notebook presenting the complete model development process, including all steps from data preprocessing to model evaluation, with detailed commentary.

### /powerbi_script_development
- **model_code_combined_powerbi_ororke_20250222_v1.ipynb**: Initial Power BI model code integrating an early version of the Random Forest Regressor model, designed for predictive maintenance visualization.
- **model_code_combined_powerbi_ororke_20250301_v2.ipynb**: Refined Power BI model code incorporating updated features and results from the trained Random Forest Regressor model.
- **model_code_combined_powerbi_ororke_20250315_v3.ipynb**: Final version of the Power BI model code, utilizing the fully trained and finalized Random Forest Regressor model for dynamic tool maintenance predictions.
- **final_combined_powerbi_ororke_20250315.ipynb**: Finalized Power BI model script with comprehensive commentary on the integration and usage of the Random Forest model within Power BI for predictive maintenance.

### Other Files
- **three_ps_ororke.txt**: Weekly log file documenting the project's progress, problems encountered, and plans for the following week, in addition to the number of hours spent working on the Capstone project.

### Git Configuration
- **.gitignore**: A configuration file specifying which files and directories should be ignored by Git to prevent unnecessary or sensitive files from being tracked.
- **.git/**: The hidden directory that stores all Git configuration, logs, refs, and objects related to version control and the history of the repository.

## File Naming Conventions

- **Submission Files**: Files ending in `submission_X.py` correspond to specific tasks as part of the capstone submission. These include model evaluation, outlier removal, feature engineering, and wear classification.
- **Model Development Files**: Notebooks prefixed with `data_model_development_ororke` represent various stages of model development, including experiments and refinements.
- **Power BI Files**: Files in the `powerbi_script_development` directory contain scripts for integrating the predictive model into Power BI, where the model will be used to create an interactive dashboard.

## **Feature Engineering & Model Development**

### **Data Integration & Processing**
- **Feature Engineering**: The data is processed to create meaningful features for the Random Forest Regressor (RFR) model. Key feature types include:
  - **Lag Features**: Lag-based variables capture previous values of bore measurements to predict future cycles.
  - **Rolling Statistics**: Rolling means and standard deviations are computed over varying window sizes to capture local trends in the bore measurements.
  - **Differencing Features**: These features calculate the rate of change in bore measurements over different lags to understand the measurement shifts.
  - **Distance to Tolerance Limits**: This feature calculates the distance between the current bore size and predefined tolerance limits, providing insights into tool wear.
  
- **Feature Normalization**: All features are scaled to ensure that each input to the model has a consistent range, improving the performance and stability of the Random Forest Regressor.
  
- **Data Preprocessing**: Missing or invalid data points are handled using techniques like imputation or exclusion, and outliers are removed through the Interquartile Range (IQR) method to ensure high-quality data for training the model.

### **Predictive Modeling**
- **Random Forest Regressor**: The core model used for forecasting future bore measurements and tool wear stages. The Random Forest Regressor was chosen due to its ability to handle complex, non-linear relationships and feature interactions in time-series data.
  
- **Core Features of the Dataset**:  
  The features used to train the model are critical in predicting the bore size and wear. Below are key features:
  
  | **Column Name**             | **Description**                                                                                           |
  |-----------------------------|-----------------------------------------------------------------------------------------------------------|
  | **C.[DataValue]**            | Current bore size measurement (target variable).                                                         |
  | **DataValue_Lag3**           | Bore size measurement lagged by 3 cycles.                                                                 |
  | **DataValue_Lag5**           | Bore size measurement lagged by 5 cycles.                                                                 |
  | **Rolling_Mean_3**           | 3-cycle rolling mean of the bore size.                                                                     |
  | **Rolling_Std_3**            | 3-cycle rolling standard deviation of the bore size.                                                      |
  | **Rolling_Mean_5**           | 5-cycle rolling mean of the bore size.                                                                     |
  | **Rolling_Std_5**            | 5-cycle rolling standard deviation of the bore size.                                                      |
  | **Distance_to_MinValue**     | Distance to the minimum acceptable bore size (tolerance limit).                                           |
  | **Distance_to_MaxValue**     | Distance to the maximum acceptable bore size (tolerance limit).                                           |
  | **Target_NextCycle**         | Future bore size measurement (target variable for prediction).                                            |
  
### **Model Development Process**
- The model development begins with exploratory data analysis (EDA) to understand the data distribution and relationships.
- **Random Forest Regressor** was then trained using the engineered features, with parameters such as the number of trees (`n_estimators=200`), maximum depth (`max_depth=10`), and minimum samples per leaf (`min_samples_leaf=5`) to ensure robustness and prevent overfitting.
- The model's hyperparameters were tuned through experimentation to find the optimal configuration, and performance was evaluated using metrics like MAE (Mean Absolute Error) and R² score.

## **Model Deployment**

### **Data Pipeline & Automation**

1. **Data Extraction**:
   - The dataset is extracted and cleaned from an Excel file, followed by feature engineering, which prepares the data for the Random Forest model.

2. **Data Processing**:
   - The processed data is stored in an Excel file and used for further analysis in the Power BI dashboard, where real-time predictions are displayed.

3. **Model Execution**:
   - The **Random Forest Regressor** model is applied to predict future bore sizes based on the current and historical data. The model is updated periodically as more data becomes available.

4. **Dashboard Integration**:
   - The final trained model is integrated into Power BI using a stylized Power BI script that feeds the model's predictions into interactive dashboards for real-time monitoring and decision-making.


## **Analysis & Insights**

### **Visualization Dashboards**

- **Wear Stage Classification**: The predictive model generates bore size predictions for each tool in the machining center, and these predictions are visualized as wear classifications in a Power BI dashboard. The wear stage classification is a critical part of the dashboard, displaying the predicted wear stages for each tool based on the calculated changes in bore size. These stages are categorized as **Normal**, **Moderate**, and **Critical**, with thresholds set according to the predicted bore size change. 

    - **Normal Wear**: Indicating minimal change in bore size, suggesting that the tool is operating within acceptable wear limits.
    - **Moderate Wear**: Suggesting that wear is becoming noticeable, and maintenance or monitoring is recommended.
    - **Critical Wear**: Highlighting significant wear or damage that may compromise the tool’s performance and indicates an immediate need for maintenance.

    These stages are visually represented with color coding on the dashboard, enabling users to quickly assess the status of tools in the machining center. This classification helps prioritize which tools need immediate attention, contributing to proactive maintenance management.

## **Limitations & Challenges**

### **Data Constraints**
- **Limited Features**: The dataset primarily consists of bore measurement values and timestamps, with very few additional inherent features available for predictive modeling. As a result, the model relies heavily on engineered features, such as lag values and rolling statistics, to make predictions. While these features help, their reliance can limit the model’s ability to generalize and capture more complex patterns in the data, which may hinder performance on more diverse datasets.

- **Noise in the Data**: The data is noisy, which complicates the detection of meaningful patterns. Despite feature engineering efforts to address this, the raw data itself lacks clear trends or relationships. This noise posed challenges when fitting models like ARIMA, which performed poorly due to the static nature and lack of inherent patterns in the dataset.

### **Model Limitations**
- **Non-linearity of Bore Measurements**: While the Random Forest Regressor has provided reasonable predictive performance, the model may not fully account for the non-linear nature of bore measurement changes. Future work could explore more advanced models that can better capture these non-linear patterns, such as LSTM networks or other deep learning approaches, to improve prediction accuracy over time.

- **Feature Engineering**: Given the lack of inherent features in the data, significant reliance was placed on feature engineering to enable model development. While this strategy was effective, it may not fully capture the system's complexities.

## **Future Enhancements**

### **Expanding to Multiple Toolheads**:
- The model has already been developed and tested on data from a single toolhead, and it has been successfully implemented in Power BI for multiple toolheads within a machining center. The model is designed to be easily expanded to handle data from other machining centers as well. Each toolhead will have its own dynamic model that captures specific wear patterns unique to it, providing more accurate and personalized maintenance insights for each toolhead.

### **Improved Model Accuracy**:
- While the model has shown promising results, it has faced challenges due to the limited features in the data and the static nature of the dataset. Future improvements will focus on exploring advanced time-series forecasting models, such as LSTM (Long Short-Term Memory) networks, which could better handle non-linear trends and improve long-term wear prediction. These models would help address the limitations of feature engineering by capturing more complex relationships in the data and improving model accuracy.

### **Real-time Dashboard Updates**:
- To enhance predictive maintenance capabilities further, integrating live data streams from the machining center into the Power BI dashboard could enable real-time updates. This would allow for continuous monitoring of tool wear and maintenance needs, facilitating proactive interventions based on the most up-to-date data and enabling a more dynamic maintenance strategy.

## **Conclusion**
This project demonstrates the development of a predictive maintenance system for toolheads using bore measurements to forecast tool wear. The primary goal is to enhance operational efficiency in a machining center by predicting tool maintenance needs and optimizing tool usage. The model has been successfully implemented in Power BI, where it has been applied to data from multiple toolheads within a single machining center, and it is ready for expansion to other machining centers with similar toolhead datasets.

While the dataset used for the model had limited features and contained significant noise, the system has proven effective in predicting tool wear. Moving forward, the model will be extended to capture more diverse tool wear patterns across different machining centers. Further accuracy improvements will be pursued by experimenting with advanced time-series forecasting models, such as LSTM networks, and integrating real-time data streams for continuous updates.

By enabling proactive maintenance decisions, this system will help reduce downtime and optimize tool usage, contributing to the overall efficiency of machining operations across multiple centers.


