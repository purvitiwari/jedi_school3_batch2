import click
import urllib2
import json
import pprint

@click.command()
@click.argument('search_term')
def validate(search_term):
    jsonres = urllib2.urlopen("http://apilayer.net/api/validate?access_key=5897967950821a17fbff92b7cc531bb9&number="+ search_term + "&format=1").read()
    jsonres = json.loads(jsonres)

    if jsonres["valid"] == True :
    	pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(jsonres)
    else :
    	print ("Invalid number or does not exist in my directory")
    	pp = pprint.PrettyPrinter(indent=4)
    	pp.pprint(jsonres)
