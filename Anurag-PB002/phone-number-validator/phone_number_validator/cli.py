import click
import re


@click.command()
@click.option('--phone-number', '-p', prompt="Phone Number",
              help='Phone number to validate')
def main(phone_number):
    """Validates phone number"""
    if is_number_valid(phone_number):
        print('Valid')
    else:
        print('Invalid')


def is_number_valid(phone_number):
    return re.match('^(0|\\+91)?[789]\\d{9}$', phone_number) is not None
