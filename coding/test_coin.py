#coding=utf-8
import urllib
import urllib2
import json

url_latestblock = 'https://blockchain.info/zh-cn/latestblock'
url_transaction = 'https://blockchain.info/zh-cn/rawtx/'
def send(url):
	#data = urllib.urlencode(values)
	response = urllib2.Request(url)#vlaues
	request = urllib2.urlopen(response)
	return request.read()

def out_latesblock(json):
	print 'json_latesblock keys:',json.keys()
	print 'json_latesblock hash',json['hash']
	print 'json_latesblock height',json['height']

json_latesblock = json.loads(send(url_latestblock))
out_latesblock(json_latesblock)

in_sum=0
out_sum=0
sum_num=0
for tx_index in json_latesblock['txIndexes'] :
	sum_num=1+sum_num
print 'sum of transaction:',sum_num

for tx_index in json_latesblock['txIndexes'] :
	json_transaction=json.loads(send(url_transaction+str(tx_index)))
	inputs=json_transaction['vin_sz']
	out=json_transaction['vout_sz']
	in_sum+=inputs
	out_sum+=out
	print 'tx_index: ',tx_index ,'  inputs: ',inputs,'  out: ',out,'  all:',in_sum,'/',out_sum

print 'sum of inputs are : ',in_sum
print 'sum of out are :',out_sum