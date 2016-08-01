#! /usr/bin/env python

import argparse
import phonenumbers
import sys

def cli_mode(phone_number, country):
  if not phone_number.startswith('+') and country is None:
    sys.stderr.write('error: country code required if not present in phone number\n')
  else:
    validate_number(phone_number, country)

def interactive_mode():
  phone_number = raw_input("Enter phone number to validate: ")
  if not phone_number.startswith("+"):
    country = raw_input("Enter the two character country code for this phone number: ")
  else:
    country = None
  validate_number(phone_number, country)

def validate_number(phone_number, country):
  try:
    num = phonenumbers.parse(phone_number, country)
    if phonenumbers.is_valid_number(num):
      print "This phone number is valid."
    else:
      print "This phone number is invalid."
  except phonenumbers.phonenumberutil.NumberParseException:
    print "This phone number is invalid."


parser = argparse.ArgumentParser(
  description='Check if a phone number is valid'
)

parser.add_argument(
  '--phone-number',
  metavar='NUMBER',
  type=str,
  nargs='+',
  help="Phone number to be validated. Defaults to interactive mode if NUMBER not present"
)

parser.add_argument(
  '--country',
  metavar='COUNTRY',
  type=str,
  nargs=1,
  help="Two character country code. Not required if included in phone number"
)

args = parser.parse_args()

if args.phone_number is None:
  phone_number = None
else:
  phone_number =  "".join(args.phone_number)

if args.country is None:
  country = None
else:
  country =  args.country[0]

if phone_number is None:
  interactive_mode()
else:
  cli_mode(phone_number, country)
