#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import re
import datetime
now = datetime.datetime.now()
import requests
import longtermaccesstoken
import pprint as pp

access_token = longtermaccesstoken.instagram_token
latitude = str(sys.argv[1])
longitude = str(sys.argv[2])
distance = str(sys.argv[3])
#path = str(sys.argv[4])
url = requests.get('https://api.instagram.com/v1/locations/search?lat=%s&lng=%s&distance=%s&count=100&access_token=%s' % (latitude,longitude,distance,access_token))
parsed_json = url.json()
#print parsed_json    
## tell the computer where to store the csv file
#outfile_path = path + '/geolocations_%i%i%i%i%i.csv' % (now.year,now.month,now.day,now.hour,now.minute)
# open it up, the w means we will write to it
#with open(outfile_path, 'w') as csvfile:
#	writer = csv.writer(csvfile, delimiter='|')
	#create a list with headings for our columns
	#headers = ['id','cat_name','cat_id','fb_id','name','latitude','longitude']
	#write the row of headings to our CSV file
	#writer.writerow(headers)
for item in parsed_json['data']:
	print item['id']
	print item['latitude'],item['longitude']
	print item['name']
#	try:
#		print item['videos']['low_resolution']['url']
#	except KeyError:
#		image = item['images']['low_resolution']['url']
#		print '\n'.join(re.findall('\S*\.jpg',image))
#	print item['user']['username']
#	if 'created_time' in item:
#		try:
#			print item['caption']['created_time']
#		except TypeError:
#			print ''
#		row = []
#		fb_id = item['id']
#		row.append(fb_id)
#		row.append(item['category_list'][0]['name'])
#		row.append(item['category_list'][0]['id'])
#		row.append(fb_id)
#	       	name = item['name']
#       	name = unicode(name).encode('utf8')
#		row.append(name)
#		row.append(item['location']['latitude'])
#	       	row.append(item['location']['longitude'])
#		try:
#			row.append(item['location']['street'])
#		except KeyError:
#			row.append('')
#		try:
#			row.append(item['location']['city'])
#		except KeyError:
#			row.append('')
#		try:
#			row.append(item['location']['country'])
#		except KeyError:
#			row.append('')
#		row.append(item['picture']['data']['url'])
#		writer.writerow(row)
#		print row
#        	print('item written to csv')
