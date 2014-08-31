from mechanize import ParseResponse, urlopen, urljoin

uri = "http://bookblog.net"

response = urlopen(urljoin(uri, "/gender/genie.php"))
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]

#print form

form['text'] = 'cheese'
form['genre'] = ['fiction']

print urlopen(form.click()).read()