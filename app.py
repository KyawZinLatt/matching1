import pandas as pd
from fuzzywuzzy import process

# Load your data
mimu_town_data = pd.read_excel('Mimu Town Level.xlsx')
not_match_data = pd.read_excel('not match data.xlsx')

# Stripping the suffix "Town" from the "Town_Name_Eng" column in the "Mimu Town Level.xlsx" file
mimu_town_data['Town_Name_Eng'] = mimu_town_data['Town_Name_Eng'].str.replace(' Town', '', regex=False)

# Function to perform fuzzy matching
def get_matches(query, choices, limit=3):
    return process.extract(query, choices, limit=limit)

# Applying fuzzy matching
# Assuming we are matching 'Town_Name_Eng' from mimu_town_data with 'Town' from not_match_data
results = []
for town in mimu_town_data['Town_Name_Eng']:
    matches = get_matches(town, not_match_data['Town'])
    results.append((town, matches))

# Convert the results to a DataFrame for better visualization and analysis
results_df = pd.DataFrame(results, columns=['Town_Name_Eng', 'Matches'])

# Saving the results to a new Excel file
results_df.to_excel('fuzzy_matching_results.xlsx', index=False)

print("Fuzzy matching completed and results saved to 'fuzzy_matching_results.xlsx'")
