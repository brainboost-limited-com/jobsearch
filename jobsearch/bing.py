import requests
import json

from bb_gt_web_automation.Database import Database
from bb_gt_web_automation.EmailClient import EmailClient
from bb_gt_web_automation.Website import Website







# Initialize the Chrome driver


# update_job_boards()
db = Database()
job_boards_from_db = db.get_job_boards_from_db()

email = EmailClient()
print(email.check_email())


# Iterate over the links returned in the search results and print them
for each_job_board_from_db in job_boards_from_db:
    link = each_job_board_from_db['url']
    print("Checking is_signed_up" + link)
    if not each_job_board_from_db['signed_up']:
        web_site = Website(each_job_board_from_db['url'])
        web_site.sign_up()
        






