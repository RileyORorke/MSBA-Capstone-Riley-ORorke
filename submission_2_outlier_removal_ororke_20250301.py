# Outlier Removal Using Interquartile Range (IQR)
q1 = df["C.[DataValue]"].quantile(0.25)
q3 = df["C.[DataValue]"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

df = df[(df["C.[DataValue]"] >= lower_bound) & (df["C.[DataValue]"] <= upper_bound)]
df = df.reset_index(drop=True)

