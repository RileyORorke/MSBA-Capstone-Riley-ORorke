from pathlib import Path

output_file_path = Path(
    r"G:\College\University of Montana\Semester 4\Capstone"
    r"\MSBA-Capstone-Riley-ORorke\data\future_wear_predictions.xlsx"
)

final_predictions.to_excel(output_file_path, index=False, engine="openpyxl")

print(f"Predictions successfully saved to: {output_file_path}")
