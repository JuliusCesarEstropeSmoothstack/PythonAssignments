import logging
import phonenumbers
import email_validator
import re
import pandas as pd

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='pandasProcessingLog.log')


# Renames columns if they exist
def replace_headers(df: pd.DataFrame):
    c1 = 'Agent Writing Contract Start Date (Carrier appointment start date)'
    c2 = 'Agent Writing Contract Start Date'
    c3 = 'Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)'
    c4 = 'Agent Writing Contract Status'

    df.rename({c1: c2, c3:c4}, axis=1, inplace=True)


def validate_phone_numbers(df: pd.DataFrame):
    logging.info('Validating Phone Numbers...')

    for phone_number in df['Agency Phone Number']:
        try:
            ph_numobj = phonenumbers.parse(phone_number, 'US')

            if not phonenumbers.is_valid_number(ph_numobj):
                logging.warning(f"Invalid Phone Number in Agency Phone Number: '{phone_number}'")

        except phonenumbers.phonenumberutil.NumberParseException:
            logging.warning(f"Non-Number in Agency Phone Number: '{phone_number}'")

    for phone_number in df['Agent Phone Number']:
        try:
            ph_numobj = phonenumbers.parse(phone_number, 'US')

            if not phonenumbers.is_valid_number(ph_numobj):
                logging.warning(f"Invalid Phone Number in Agent Phone Number: '{phone_number}'")

        except phonenumbers.phonenumberutil.NumberParseException:
            logging.warning(f"Non-Number in Agent Phone Number: '{phone_number}'")

    logging.info('Completed Validating Phone Numbers')


# Validate that state is valid
# Solution from: https://stackoverflow.com/questions/2313032/regex-for-state-abbreviations-python
def validate_state(df: pd.DataFrame):
    logging.info('Validating States...')

    states = ['IA', 'KS', 'UT', 'VA', 'NC', 'NE', 'SD', 'AL', 'ID', 'FM', 'DE', 'AK', 'CT', 'PR', 'NM', 'MS', 'PW',
              'CO', 'NJ', 'FL', 'MN', 'VI', 'NV', 'AZ', 'WI', 'ND', 'PA', 'OK', 'KY', 'RI', 'NH', 'MO', 'ME', 'VT',
              'GA', 'GU', 'AS', 'NY', 'CA', 'HI', 'IL', 'TN', 'MA', 'OH', 'MD', 'MI', 'WY', 'WA', 'OR', 'MH', 'SC',
              'IN', 'LA', 'MP', 'DC', 'MT', 'AR', 'WV', 'TX']
    regex = re.compile(r'\b(' + '|'.join(states) + r')\b', re.IGNORECASE)

    for state in df['Agency State']:
        if not re.match(regex, state):
            logging.warning(f"Invalid State:\n{df[df['Agency State'] == state]}")

    for state in df['Agent State']:
        if not re.match(regex, state):
            logging.warning(f"Invalid State:\n{df[df['Agent State'] == state]}")

    logging.info('Completed Validating States')


# Validate that email is valid
def validate_email(df: pd.DataFrame):
    logging.info('Validating Emails...')
    for email in df['Agent Email Address']:
        try:
            if not email_validator.validate_email(email):
                logging.warning(f"Invalid Email: {email}")
        except email_validator.EmailSyntaxError:
            logging.warning(f"Invalid Syntax for Email: {email}")

    logging.info('Completed Validating Emails')


# Performs all processing of the agent dataframe
def process_agent_dataframe(df: pd.DataFrame):
    logging.info('Processing dataframe information...')
    replace_headers(df)
    validate_phone_numbers(df)
    validate_state(df)
    validate_email(df)
