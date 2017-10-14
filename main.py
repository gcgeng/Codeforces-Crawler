pages = []
with open('list') as f:
    lines = f.readlines()
    for line in lines:
        pages.append(line.rstrip())
import urllib
import urllib2 as ur
from urllib2 import Request, urlopen
f = open('output.html', 'a')
for page in pages:
    url = 'https://vjudge.net/problem/CodeForces-'+page
    content=ur.urlopen(url).read()
    pos = content.find('src="/problem/description')
    pos2 = content.find('width', pos)
    content = content[pos+5:pos2]
    haha = 'https://vjudge.net'+content
    pos = haha.find('"');
    haha = haha[:pos]
    co = ur.urlopen(haha).read()
    f.write(co)
