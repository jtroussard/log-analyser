# this is obviously going to need reformating and more work but the basics are there
# - connection
# - find/iterate confluence page table
from atlassian import Confluence
from bs4 import BeautifulSoup

# this design sucks - just done in haste to facilitate demo
def get_table_rows():
	# lots of patterns/designs available to hide/impl the credentails... hardcoded as POC/development draft
	confluence = Confluence(
	    url='https://confluence.mckesson.com:8443',
	    username='YOUR-EID-STRING',
	    password='YOUR-EID-PASSWORD')

	# get page TODO=check response
	# page_id 123905046 == ERX build issue tracker conflence page
	body = confluence.get_page_by_id(page_id=123905046, expand="body.storage").get('body').get('storage').get('value')
	# make soup
	soup = BeautifulSoup(body, 'html.parser')
	# create list representation of table TODO=find way to verify correct table was identified
	rows = soup.find("table").find("tbody").find_all("tr")

	# show results
	for row in rows:
	    print(f"* {row}\n")

def parse_table_row(row):
	# can be passed directly to route to jinja e.g. parsed_row.hash or parsed_row.description etc...
	parsed_row = {
		"row_id": "extract row id from row variable",
		"row_description": "extract row description from row variable",
		"row_stack_trace": "extract row stacktrace from row variable",
		"row_hash": "extract row hash from row variable",
	}
	return parsed_row