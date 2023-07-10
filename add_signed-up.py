from tinydb import TinyDB, Query

# Path to the database file
db_path = "bb_gt_web_automation/database/db.json"

# Create a TinyDB instance and open the database
db = TinyDB(db_path)

# Access the "job_boards" collection/table
job_boards = db.table("job_boards")

# Define the field to be added
new_field = "signed_up"

# Update all documents in the collection with the new field and value
job_boards.update({new_field: False})

# Close the database
db.close()
