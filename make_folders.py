import os

# Define the list of folders
folders = ["banking_account", "internet", "phone_expenses", "loan_account", "council_rate", "insurance", "legal", "misc"]

# Create a function to create folders
def create_folders(parent_folder, folder_names):
    for folder_name in folder_names:
        folder_path = os.path.join(parent_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

# Define the base directory where the folders will be created
base_directory = "."

# Create folders for the next 10 years
for year in range(2023, 2033):  # Change the range according to the current year
    year_folder = os.path.join(base_directory, f"{str(year-1)}-{str(year)}")
    os.makedirs(year_folder, exist_ok=True)
    
    nz_taxes_folder = os.path.join(year_folder, "nz_taxes")
    os.makedirs(nz_taxes_folder, exist_ok=True)
    
    create_folders(nz_taxes_folder, folders)

print("Folders created successfully.")
