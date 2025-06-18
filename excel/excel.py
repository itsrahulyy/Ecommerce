import pandas as pd
import os

# === CONFIGURATION ===
input_file = 'C:/python/E-commerce_page/ASSIGNMENT/excel/invite_today.csv'        # Your input CSV file name
output_folder = 'C:/python/E-commerce_page/ASSIGNMENT/excel/sheets'    # Folder to store batch files
batch_size = 50000                   # Change this to your desired batch size

# === LOAD CSV ===
df = pd.read_csv(input_file)

# === CREATE OUTPUT FOLDER IF NOT EXISTS ===
os.makedirs(output_folder, exist_ok=True)

# === SPLIT INTO BATCHES ===
total_rows = len(df)
num_batches = (total_rows + batch_size - 1) // batch_size  # ceiling division

for i in range(num_batches):
    start_row = i * batch_size
    end_row = min((i + 1) * batch_size, total_rows)
    batch_df = df.iloc[start_row:end_row]
    
    output_file = os.path.join(output_folder, f'batch_{i + 1}.csv')
    batch_df.to_csv(output_file, index=False)

    print(f'Batch {i + 1} saved: {output_file}')

print(f'\n✅ Done! {num_batches} batches created in "{output_folder}" folder.')
