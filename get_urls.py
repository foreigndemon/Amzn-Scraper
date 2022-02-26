# using this get_urls.py I have extracted all
# 1000 urls which are needed to be scraped

import csv
import pprint

urls = []
with open("Amazon_Scraping.csv",'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        urls.append(f"https://www.amazon.{row[3]}/dp/{row[2]}")

# count = 0
# for item in urls:
#     if item[-1].lower() != 'x':
#         count += 1
#         print(item)
# print(count)
# pprint.pprint(urls)
print(len(urls))