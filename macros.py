import csv

def twitter():
	return """<a class="twitter-timeline" href="https://twitter.com/c4dm" data-widget-id="561187870955040769" data-chrome="nofooter" width="300" height="900">Tweets by @c4dm</a><script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>"""


def peoplelist(criteria=None):
	if criteria==None:
		criteria = {}
	ret = "<table width='100%' class='peoplelist'>"
	with open("input/people.tsv", "r") as fp:
		rdr = csv.DictReader(fp, delimiter='\t')
		for x in rdr:
			if any([x.get(key, '') != val for key, val in criteria.items()]):
				continue
			if x.get('url', '') != '':
				htmlname = "<a href='%s'>%s</a>" % (x['url'], x.get('name'))
			else:
				htmlname = x.get('name')
			ret += "\n   <tr><td>%s</td><td>%s</td></tr>" % (htmlname, x.get('blurb'))
	ret += "</table>"
	return ret

def publicationslist(year):
	ret = """<p>Select year: <strong>%i</strong>""" % year
	for otheryear in range(year-1, 1995, -1):
		ret += " <a href='pubs%i.html'>%i</a>" % (otheryear, otheryear)
	ret +="""
<h2>%i</h2>""" % year
	# Now load the content pre-rendered by bibtex2html
	with open("input/pubs%i_raw.html" % year, "r") as fp:
		data = ''.join(fp.readlines())
	ret += data
	return ret

def pagesourceurl():
	#return "https://github.com/c4dm/c4dmpoole/tree/master/%s" % (str(page))
        return "https://github.com/c4dm/c4dmpoole/edit/master/%s" % (str(page))


