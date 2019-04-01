#Written by Steven Martinez
#Gather address data from a downloaded HTML file.
from bs4 import BeautifulSoup
import csv

#Open downloaded HTML file
with open ("Diamond Bar, CA.html") as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

#Create CSV to store the address information
csv_file = open('Addresses.csv', 'w')
csvwriter = csv.writer(csv_file)
count = 0

#Loop through the HTML page to gather relevant information to store into the CSV
for listing in soup.find_all('div', class_='item facility hasRating'):
	if count == 0:
		header = ["Name","Street","City","State","ZIP","URL"]
		csvwriter.writerow(header)
		count += 1
	listname = listing.h3.span.text
	address = listing.find('span', class_='street-address').text
	locality = listing.find_all('span', class_='locality')[0].text
	state = listing.find_all('span', class_='locality')[1].text
	postcode = listing.find('span', class_='postal-code').text
	url = listing.find('a', href=True)
	csvwriter.writerow([listname,address,locality,state,postcode,url['href']])