from tinydb import TinyDB, Query
import time

# Connect to the existing TinyDB database
db = TinyDB('db.json')

# Create the 'job_boards' table
job_boards = db.table('job_boards')

# List of URLs
with open('job_boards.txt', 'r') as file:
    urls = file.read().splitlines()

# Get the current timestamp
current_timestamp = int(time.time())

# Insert URLs with the current timestamp in the 'job_boards' table
for url in urls:
    job_boards.insert({'url': url, 'last_updated': current_timestamp})

# Close the database connection
db.close()
