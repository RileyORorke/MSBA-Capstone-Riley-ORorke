def predict_future_bores(model, df, feature_columns, future_cycles=10):
    """
    Predicts bore sizes for future cycles using the trained model.

    Parameters:
    - model: Trained regression model
    - df (pd.DataFrame): DataFrame containing past bore data
    - feature_columns (list): List of feature column names
    - future_cycles (int): Number of future cycles to predict

    Returns:
    - pd.DataFrame: DataFrame containing future cycle predictions
    """
    future_df = pd.DataFrame()
    future_df["cycle_count"] = range(df["cycle_count"].max() + 1, df["cycle_count"].max() + 1 + future_cycles)
    
    last_known_values = df.iloc[-1][feature_columns].to_dict()
    predicted_bores = []

    for cycle in future_df["cycle_count"]:
        new_row = last_known_values.copy()
        new_row["cycle_count"] = cycle

        for lag in [1, 2, 3, 5]:
            new_row[f"data_value_lag{lag}"] = predicted_bores[-lag] if len(predicted_bores) >= lag else last_known_values["C.[DataValue]"]

        new_X = pd.DataFrame([new_row])[feature_columns]
        predicted_bore = model.predict(new_X)[0]
        predicted_bores.append(predicted_bore)

        future_df.loc[future_df["cycle_count"] == cycle, "predicted_bore_size"] = predicted_bore
    
    return future_df

