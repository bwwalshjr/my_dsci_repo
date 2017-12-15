import requests
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

#loads all the html information, after making sure the javascript elements are evaluated
def build_soup():
	url = 'http://www.champion.gg/statistics/'
	
	browser = webdriver.Firefox()
	browser.get(url)
	innerHTML = browser.execute_script("return document.body.innerHTML")
	browser.quit()

	soup = BeautifulSoup(innerHTML, 'html.parser')

	return soup
	
#finds the table body and selects it
def build_table(soup):
	table = soup.find('tbody')
	return table

#finds the header and selects it
def build_header(soup):
	header = soup.find('thead')
	return header
	
#creates the column headers
def add_header_list(header, collection):
	header_list = []
	header_row = header.find('tr')
	for cell in header_row.findAll('td'):
		item = cell.get_text(strip=True).encode("utf-8")
		header_list.append(item)
	collection.append(header_list)
	return collection
	
#adds the data for each row
def add_champion_rows(table, collection):
	for row in table.findAll('tr'):
		row_list = []
		for cell in row.findAll('td'):
			data = cell.get_text(strip=True).encode("utf-8")
			row_list.append(data)
		collection.append(row_list)
	return collection
	
#writes the data to a csv file
def write_to_csv(collection):
	with open("./data/champion_data2.csv", "w") as f:
		writer = csv.writer(f)
		for row in collection:
			writer.writerow(row)
			
soup = build_soup()
header = build_header(soup)
table = build_table(soup)

collection = []

collection = add_header_list(header, collection)

collection = add_champion_rows(table, collection)

write_to_csv(collection)

