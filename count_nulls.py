import argparse
from pathlib import Path

import pandas as pd


def main() -> None:
    default_csv = Path(__file__).parent / "data" / "creditcard_2023_processed.csv"

    parser = argparse.ArgumentParser(description="Count null values in each CSV column.")
    parser.add_argument(
        "csv_path",
        nargs="?",
        type=Path,
        default=default_csv,
        help=f"CSV file to inspect (default: {default_csv})",
    )
    args = parser.parse_args()

    dataframe = pd.read_csv(args.csv_path)
    print(dataframe.isna().sum().to_string())


if __name__ == "__main__":
    main()
