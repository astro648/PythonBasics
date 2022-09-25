import csv

with open('1wklaunchwrite.csv', mode='w') as csv_file:
    fieldnames = ['Spacecraft', 'Rocket', 'Company', 'Date of Launch']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Spacecraft': 'NROL-91', 'Rocket': 'Delta IV Heavy', 'Company': 'United Launch Alliance',
                     'Date of Launch': '24-Sep-22'})
    writer.writerow({'Spacecraft': 'Starlink Group 4-35', 'Rocket': 'Falcon 9 Block 5', 'Company': 'SpaceX',
                     'Date of Launch': '24-Sep-22'})
    
