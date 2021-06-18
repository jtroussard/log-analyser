from atlassian import Confluence
from bs4 import BeautifulSoup

confluence = Confluence(
    url='https://confluence.mckesson.com:8443',
    username='e6737e6',
    password='fck!this5stupiD')

# get page TODO=check response
body = confluence.get_page_by_id(page_id=123905046, expand="body.storage").get('body').get('storage').get('value')
# make soup
soup = BeautifulSoup(body, 'html.parser')
# create list representation of table TODO=verify table id='issues' or whatever
rows = soup.find("table").find("tbody").find_all("tr")

results = {}
for row in rows:
    # if row hash matches update GUI status column with link to solution
    # if row hash does not match update GUI status column with link to create jira ticket, and add row to confluence table
    print(f"* {row}\n")