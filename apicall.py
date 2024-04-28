import csv
import requests

# Function to call the API
def call_api(id):
    url = f'https://jsonplaceholder.typicode.com/todos/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Read IDs from the CSV file
updated_rows = []
with open('/Users/irshadvali/Desktop/input.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        id = row['id']
        # Call the API
        api_data = call_api(id)
        if api_data:
            # Process the API response
            # For example, if the response has a 'title' field:
            title = api_data.get('title', 'N/A')
            # Update the row with the API data
            row['title'] = title
        updated_rows.append(row)

# Write the updated data back to the CSV file
with open('/Users/irshadvali/Desktop/output.csv', mode='w', newline='') as csv_file:
    fieldnames = ['id', 'title']  # Add more fields as needed
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    # Write the updated rows
    for row in updated_rows:
        writer.writerow(row)
