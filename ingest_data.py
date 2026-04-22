import pandas as pd

# 1. Load the dataset with the correct encoding
try:
    df = pd.read_csv("cleaned_recipes.csv", encoding='latin-1')
    print("Step 1: File loaded successfully!")
except Exception as e:
    print(f"Error loading file: {e}")

# 2. Check the column names
print("Your columns are:", df.columns.tolist())

# 3. Create the Search String
# IMPORTANT: Change 'RecipeName', 'Ingredients', and 'Instructions' 
# to match the exact names printed above.
def prepare_text(row):
    # Example: If your column is 'title' instead of 'RecipeName', change it here
    return f"Recipe: {row.iloc[0]}. Ingredients: {row.iloc[1]}. Instructions: {row.iloc[2]}"

df['search_text'] = df.apply(prepare_text, axis=1)

print(f"Successfully prepared {len(df)} recipes for the AI.")
print("\nPreview of first search string:")
print(df['search_text'].iloc[0])