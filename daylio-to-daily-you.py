import sys
import os
import datetime
import argparse
import csv
import json

# Configure this to match your Daylio mood names
mood_mapping = {
        'rad': 2,
        'good': 1,
        'meh': 0,
        'bad': -1,
        'awful': -2,
    }

# Command-line args
parser = argparse.ArgumentParser(description='Convert Daylio entries to Daily You.')

parser.add_argument('csv', type=str, help='Input CSV file')
parser.add_argument('--images', help='Folder of images to import.')

args = parser.parse_args()
csv_file_path = args.csv
import_image_folder = args.images

# Check if CSV file exists
if not os.path.isfile(csv_file_path):
    print(f'Error: file {csv_file_path} does not exist')
    sys.exit(1)

# Open the CSV
csv_file = open(csv_file_path, 'r', encoding="utf-8-sig")
csv_reader = csv.DictReader(csv_file)

json_array = []

# Convert CSV into JSON array
for row in csv_reader:
    time_created = datetime.datetime.strptime(row['full_date'], '%Y-%m-%d').isoformat()
    time_modified = datetime.datetime.now().isoformat()

    # Handle images
    if import_image_folder:
        entry_date = datetime.datetime.strptime(row['full_date'], '%Y-%m-%d')
        
        image_paths = []

        # Check if image folder exists
        if not os.path.exists(import_image_folder):
            print(f'Error: folder {import_image_folder} does not exist')
            sys.exit(1)
        
        # Search for images for the current day
        for file_name in os.listdir(import_image_folder):
            if file_name.startswith(f'photo_{entry_date.year}_{str(entry_date.month).zfill(2)}_{str(entry_date.day).zfill(2)}'):
                image_paths.append(os.path.join(import_image_folder, file_name))

        if len(image_paths) > 0:
            image_path = image_paths[0]
            
            # Assume there will be an image file named after the date
            entry_date = datetime.datetime.strptime(row['full_date'], '%Y-%m-%d')

            # Rename the image to the expected format
            new_img_name = 'daily_you_' + str(entry_date.month) + '_' + str(entry_date.day) + '_' + str(entry_date.year) + '.jpg'
            new_path = os.path.join('output', new_img_name)
            os.makedirs('output', exist_ok=True)
            with open(image_path, 'rb') as source_file, open(new_path, 'wb') as dest_file:
                dest_file.write(source_file.read())
            
            img_path = new_img_name
        else:
            img_path = None
    else:
        img_path = None
    mood = row['mood']
    text = row['note']
    
    # Add to json
    json_entry = {
        'timeCreated': time_created,
        'timeModified': time_modified,
        'imgPath': img_path,
        'mood': mood_mapping.get(mood, 0),
        'text': text
    }
    
    json_array.append(json_entry)

# Save the JSON
output_file_path = 'output/daily_you_logs.json'
os.makedirs('output', exist_ok=True)
with open(output_file_path, 'w') as json_file:
    json.dump(json_array, json_file, indent=2)
