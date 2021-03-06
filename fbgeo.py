import sys
import json
import csv
import datetime
now = datetime.datetime.now()
import urllib2
from urllib2 import HTTPError, URLError
import longtermaccesstoken
access_token = longtermaccesstoken.access_token
latitude = str(sys.argv[1])
longitude = str(sys.argv[2])
distance = str(sys.argv[3])
path = str(sys.argv[4])
url = urllib2.Request('https://graph.facebook.com/search?limit=1000&type=place&center=%s,%s&distance=%s&fields=name,category,category_list,likes,location,picture&access_token=%s' % (latitude,longitude,distance,access_token))
parsed_json = json.load(urllib2.urlopen(url))
## tell the computer where to store the csv file
outfile_path = path + '/geolocations_%i%i%i%i%i.csv' % (now.year,now.month,now.day,now.hour,now.minute)
#for item in parsed_json['data']:
#	name = item['name']
#	name = unicode(name).encode('utf8')
#	print(item['category'])
#	print(item['category_list'][0]['id'])
#	print(item['category_list'][0]['name'])
#	print(item['id'])
#	print(name)
#	print(item['location']['latitude'])
#	print(item['location']['longitude']) 
#	print('--')
# open it up, the w means we will write to it
writer = csv.writer(open(outfile_path, 'w'))
#create a list with headings for our columns
headers = ['id','cat_name','cat_id','fb_id','name','latitude','longitude']
#write the row of headings to our CSV file
writer.writerow(headers)
for item in parsed_json['data']:
	row = []
	fb_id = item['id']
	row.append(fb_id)
	row.append(item['category_list'][0]['name'])
	row.append(item['category_list'][0]['id'])
	row.append(fb_id)
        name = item['name']
        name = unicode(name).encode('utf8')
	row.append(name)
	row.append(item['location']['latitude'])
        row.append(item['location']['longitude'])
	writer.writerow(row)
	print row
        print('item written to csv')
