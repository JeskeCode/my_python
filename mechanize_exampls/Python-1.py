import mechanize, urllib, urllib2

# Start Browser
br = mechanize.Browser(factory=mechanize.RobustFactory())

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6')]
br.open('http://www.tse.gov.br/spce2008DivHtml/pesquisaCandidato.jsp?sgUf=AC')
# already choose state here for now
html = br.response().read()
# print html

# Select the form
br.select_form(nr=0)  # since there is only 1 form on the site
print br.form

# get all values for states and munis
# to eventually loop over them
states = br.form.possible_items("sgUf")
munis  = br.form.possible_items("sgUe")

# Enter info in web form
br.form.set_all_readonly(False)             # make all form items changeable
#br.form['acao'] = 'Pesquisar'              # send action "pesquisar"??
br.form.set(True, states[1] , "sgUf")       # state
br.form.set(True, munis[1] , "sgUe")        # municipality
br.form.set(True, "11" , "candidatura")     # post (prefeito-11 or vereador-13)
br.form.set(True, "2" , "parcial")          # parcial 1 or 2 (choose 2)

# Submit the form  -- does not work yet
request2 = br.form.click()
#request2 = br.submit()

try:
    response2 = urllib2.urlopen(request2)
except urllib2.HTTPError, response2:
    pass
    print response2.geturl()
    print response2.info()  # headers
    print response2.read()  # body