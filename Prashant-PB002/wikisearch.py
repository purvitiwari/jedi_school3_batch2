#! /usr/bin/env python

import argparse
import sys

from wikiapi import WikiApi

def get_url(query, log_file):
  wiki = WikiApi()
  results = wiki.find(query)
  if len(results) == 0:
    sys.stderr.write("No wikipedia article found for '" + query + "'\n")
  else:
    article = wiki.get_article(results[0])
    print article.url
    with open(log_file, 'a') as f:
      f.write(article.url + "\n")

parser = argparse.ArgumentParser(
  description='Fetch link to wikipedia article for search term'
)

parser.add_argument(
  '--search',
  metavar='TERM',
  type=str,
  nargs='+',
  help="Fetch link to wikipedia article of TERM"
)

parser.add_argument(
  '--log-file',
  metavar='LOG_FILE',
  type=str,
  nargs=1,
  help="Log fetched links to LOG_FILE. By default logs to wiki.log"
)

args = parser.parse_args()

if args.search is None:
  query = raw_input("Enter search term: ")
else:
  query = " ".join(args.search)

if args.log_file is None:
  log_file = 'wiki.log'
else:
  log_file = args.log_file[0]

get_url(query, log_file)
