#!/usr/bin/python3
# Author:	Torsten Spickhofen

import sys
import datetime
import json
from urllib.request import urlopen, urlretrieve


lang = 'de-De' 
idx = '0' 
picDir = '/home/hawkril/Bilder/Bing/'


def fetch_json():
	js_url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=' + idx + '&n=1&mkt=' + lang
	js_socket = urlopen(js_url)
	return json.loads(js_socket.read().decode('utf-8'))

def fetch_wallpaper(pic, data):
	picpath = picDir + pic
	picurl = 'http://www.bing.com' + data['images'][0]['url']
	urlretrieve(picurl, picpath)


def fetch_descrition(pic, data):
	copyright = data['images'][0]['copyright']
	split = copyright.partition('(')
	des_string = pic + ' - ' + split[0] +'\n'
	des_file = picDir + 'descriptions.txt'
	with open(des_file, "a") as f:
		f.write(des_string)
		f.close()

def main():
	json = fetch_json()
	date = datetime.datetime.now() + datetime.timedelta(days=-(int(idx)))
	picname = date.strftime('bing_%d-%m-%Y') + '.jpg'

	fetch_wallpaper(picname, json)
	fetch_descrition(picname, json)

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc > 1:
		idx = sys.argv[1]
	main()
