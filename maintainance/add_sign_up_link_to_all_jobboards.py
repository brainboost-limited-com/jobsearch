from tinydb import TinyDB, Query
from jobsearch.bb_gt_web_automation.DuckDuckGo import DuckDuckGo




db = TinyDB('jobsearch/bb_gt_web_automation/database/db.json')
job_board_table = db.table('job_boards')
JobBoard = Query()

for each_job_board in JobBoard:    
    search_engine = DuckDuckGo()
    site_name = [JobBoard.split('https://')[1] if JobBoard.include('https://') else JobBoard.split('http://')[1]]
    signup_link = search_engine.search(site_name + ' create account')[0]
    job_board_table.update({'sign_up_link': signup_link}, JobBoard)

# You can also set the value of the 'sign_up_link' field to a specific value for each job board
#job_board_table.update({'sign_up_link': 'https://example.com/signup'}, JobBoard.name == 'Example Job Board')
