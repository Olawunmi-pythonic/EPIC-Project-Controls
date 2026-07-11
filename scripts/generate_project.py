"""
Project: EPIC Project Controls Data Generator

Author: Balogun Olawunmi
Description: 
Generate the Project_Master.xlsx file for the
120MMSCFD Gas Processing Facility Project.
"""

from pathlib import Path
import pandas as pd

PROJECT = {
    "Project_ID": "GPF001",
    "Project_Name": "120MMSCFD Gas Processing Facility",
    "Client": "Shell Petroleum Development Company",
    "EPC_Contractor": "Saipem Nigeria Limited",
    "Location": "Bonny Island, Rivers State, Nigeria",
    "Contract_Type": "EPIC",
    "Start_Date": "2026-01-01",
    "Finish_Date": "2027-12-31",
    "Budget_USD": 200000000,
    "Project_Manager": "Engr. Olawunmi Balogun",

}

project_df = pd.DataFrame([PROJECT])

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

project_df.to_excel(OUTPUT_DIR / "Project_Master.xlsx", index=False)

print("Project_Master.xlsx file generated successfully in the output folder.")
