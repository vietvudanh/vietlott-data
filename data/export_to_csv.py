import json
import csv

# Input and output file paths
input_file = 'data/power655.jsonl'
output_file = 'power655_results.csv'

# Open the input and output files
with open(input_file, 'r') as jsonl_file, open(output_file, 'w', newline='') as csv_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    csv_writer.writerow(['Date', 'ID', 'Result', 'Page', 'Process Time'])
    
    # Read and process each line
    for line in jsonl_file:
        # Parse the JSON data
        data = json.loads(line)
        
        # Extract the relevant fields
        date = data['date']
        id = data['id']
        result = ','.join(map(str, data['result']))  # Convert list to comma-separated string
        page = data['page']
        process_time = data['process_time']
        
        # Write the data to the CSV file
        csv_writer.writerow([date, id, result, page, process_time])

print(f"Data has been exported to {output_file}")