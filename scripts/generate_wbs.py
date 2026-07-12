from pathlib import Path
import pandas as pd

# Locate the project root
project_root = Path(__file__).resolve().parent.parent

input_file = project_root / "data" / "wbs_template.csv"
output_folder = project_root / "output"
output_file = output_folder / "WBS.xlsx"


def load_wbs_data(file_path):
    """
    Load the WBS template CSV into a pandas DataFrame.

    Parameters:
        file_path (Path): Path to the WBS template CSV file.

    Returns:
        pandas.DataFrame: DataFrame
    """
    if not file_path.exists():
        raise FileNotFoundError(f"WBS template not found: {file_path}")
    df = pd.read_csv(file_path)
    return df


def validate_wbs_columns(df):
    """
    Validate that the required columns exist in the DataFrame.

    Parameters:
        df (pandas.DataFrame): WBS DataFrame.

    Raises:
        ValueError: If any required columns are missing.
    """
    required_columns = [
        "WBS_Code",
        "Parent_WBS",
        "WBS_Description",
        "Project_Phase",
        "Discipline",
        "Control_Account"
    ]
    missing_columns = [
        column for column in required_columns if column not in df.columns]
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )


def export_to_excel(df, output_folder, output_file):
    """
    Export the WBS DataFrame to an Excel file.

    Parameters:
        df (pandas.DataFrame): WBS DataFrame.
        output_folder (Path): Folder to save the output Excel file.
        output_file (Path): Full path to the output Excel file.
    """

    # Create the output folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    # Export the DataFrame to Excel
    df.to_excel(output_file, index=False)

    print(f"WBS exported  successfully to Excel:\n{output_file}")


if __name__ == "__main__":
    # Load the WBS data
    df = load_wbs_data(input_file)

    # Validate the columns
    validate_wbs_columns(df)

    # Export to Excel
    export_to_excel(df, output_folder, output_file)
