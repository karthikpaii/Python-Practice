import pandas as pd
# File paths
input_file = "anual_report"     # Replace with your input file
output_file = "cleaned_output_file.csv" # Output file

chunk_size = 500  # Number of rows per chunk
first_chunk = True  # To control header writing

# Read the file in chunks
for chunk in pd.read_csv(input_file, chunksize=chunk_size):
    
     # Remove duplicate rows in the chunk
     cleaned_chunk = chunk.drop_duplicates()
    
     # Write cleaned data to output file
     if first_chunk:
         cleaned_chunk.to_csv(output_file, index=False, mode='w')
         first_chunk = False
     else:
        cleaned_chunk.to_csv(output_file, index=False, mode='a', header=False)

print("File processed successfully. Duplicates removed.")
