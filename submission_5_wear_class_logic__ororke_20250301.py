def classify_wear(change):
    """
    Classifies wear severity based on bore size change.

    Parameters:
    - change (float): Difference in bore size between cycles.

    Returns:
    - str: Wear classification label.
    """
    if change < 0.001:
        return "Normal Wear"
    elif 0.001 <= change < 0.005:
        return "Moderate Wear"
    return "Critical Wear"

# Assign wear labels
future_df["predicted_wear_stage"] = future_df["bore_size_change"].apply(classify_wear)
