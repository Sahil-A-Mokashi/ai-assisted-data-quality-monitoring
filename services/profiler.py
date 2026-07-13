import pandas as pd


def profile_csv(file_path):

    df = pd.read_csv(file_path)

    total_rows = len(df)

    total_columns = len(df.columns)

    missing_values = int(df.isnull().sum().sum())

    duplicate_rows = int(df.duplicated().sum())

    total_cells = total_rows * total_columns

    null_percentage = (
        (missing_values / total_cells) * 100
        if total_cells > 0
        else 0
    )

    completeness_score = round(100 - null_percentage, 2)

    consistency_score = round(
        ((total_rows - duplicate_rows) / total_rows) * 100,
        2
    ) if total_rows > 0 else 100

    return {
        "total_rows": total_rows,
        "total_columns": total_columns,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "null_percentage": round(null_percentage, 2),
        "completeness_score": completeness_score,
        "consistency_score": consistency_score
    }