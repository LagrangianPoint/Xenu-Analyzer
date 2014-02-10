#!/usr/bin/python

import sys
import re

print " * * This script is for extracting data from Xenu * * "

if sys.argv == 1:
	print " ERROR: no input file given"
	print "Usage: \t ./xenu-analyzer.py input.html"
	sys.exit(1)

strFile = sys.argv[1]

fh = open(strFile, 'r')
strRaw = fh.read()
fh.close()

def getValidUrlForSearchEngine(strRaw):
	listSection = re.findall('List of valid URLs you can submit to a search engine:</h2>\s*<pre>(.*?)</pre>', strRaw, re.DOTALL|re.MULTILINE )
	strSection = listSection[0]
	listUrls =  re.findall('<a href="([^"]+)" TARGET=_blank>', strSection, re.DOTALL|re.MULTILINE )
	return listUrls
	
	

## Gets the root url
def getRootUrl(strRaw):
	listResults = re.findall('<h2>Root URL: <a href="([^"]+)">[^<]+</a>', strRaw, re.DOTALL|re.MULTILINE )
	return listResults[0]

def listToFile(listData, strFile):
	fh = open(strFile, 'w')
	strOut = "\n".join(listData)
	fh.write(strOut )
	fh.close()

def getBrokenLinks(strRaw):
	listSection = re.findall('Broken links, ordered by link:</h2>\s*<pre>(.*?)</pre>', strRaw, re.DOTALL|re.MULTILINE )
	strSection = listSection[0]
	listUrls =  re.findall('[^\t]<a href="([^"]+)" TARGET=_blank>[^<]+</a>', strSection, re.DOTALL )
	return listUrls

def getRedirectedUrls(strRaw):
	listSection = re.findall('List of redirected URLs</h2>\s*<pre>(.*?)</pre>', strRaw, re.DOTALL|re.MULTILINE )
	strSection = listSection[0]
	listUrls =  re.findall('^<a href="([^"]+)" TARGET=_blank>[^<]+</a>', strSection, re.DOTALL|re.MULTILINE )
	return listUrls



strRootUrl = getRootUrl(strRaw)
print "Root URL: %s " % (strRootUrl)

listValidForSearch = getValidUrlForSearchEngine(strRaw)
listToFile(listValidForSearch, "valid_urls_for_searchengines.txt")

listBrokenLinks = getBrokenLinks(strRaw)
listToFile(listBrokenLinks, "broken_links.txt")

listRedirectedUrls = getRedirectedUrls(strRaw)
listToFile(listRedirectedUrls, "redirected_urls.txt")


