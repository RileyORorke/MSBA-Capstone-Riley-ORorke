def evaluate_model_performance(model, X, y):
    """
    Evaluate the trained model using common regression metrics.

    Parameters:
    - model: Trained regression model
    - X (pd.DataFrame): Feature set
    - y (pd.Series): True target values

    Returns:
    - None (prints evaluation metrics and displays a scatter plot)
    """
    y_predicted = model.predict(X)

    mae = mean_absolute_error(y, y_predicted)
    mse = mean_squared_error(y, y_predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_predicted)

    print("\nModel Evaluation Metrics:")
    print(f"- Mean Absolute Error (MAE): {mae:.4f}")
    print(f"- Mean Squared Error (MSE): {mse:.4f}")
    print(f"- Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"- R-squared (R²): {r2:.4f}")
