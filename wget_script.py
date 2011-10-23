import os
import sys

f = open('urls.txt', 'r')
urls = f.readlines()
f.close()

for i,url in enumerate(urls):
	os.system('wget -q -O tile_'+str(i)+'.jpg \''+url+'\'')


