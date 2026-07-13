import pandas as pd


def profile_csv(file_path):
    """
    Analyse a CSV file and return basic profiling metrics.
    """

    df = pd.read_csv(file_path)

    metrics = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }

    return metrics