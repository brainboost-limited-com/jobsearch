from tinydb import TinyDB

class Database:
    
    def __init__(self) -> None:
        self.db = TinyDB('bb_gt_web_automation/database/db.json')


    def get_job_boards_from_db(self):
        # Access the 'job_boards' table
        job_boards_table = self.db.table('job_boards')
        # Retrieve all records as Python dictionaries
        records = job_boards_table.all()
        return records

    def get_form_values_from_db(self):
        # Access the 'form_values' table
        form_values_table = self.db.table('form_values')
        # Retrieve all records as Python dictionaries
        records = form_values_table.all()
        return records