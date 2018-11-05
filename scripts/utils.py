import re

def dequote(s: str):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def get_time_from_filename(filename: str):
    regex = r'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
    return re.findall(regex, filename)[0]

def get_show_name(title: str):
    if "BlockChannel" in title:
        return 'BlockChannel'
    elif 'On-Ramping' in title:
        return 'On-Ramping with Dee'
    elif 'Announcements' in title:
        return 'TBP Announcements'
    elif 'NABP' in title:
        return 'Not Another Bitcoin Podcast'
    elif 'Ether Review' in title:
        return "The Ether Review"
    elif 'Buy or Sell' in title:
        return "Buy or Sell, What the Hell"
    elif 'An Ethereum' in title:
        return "An Ethereum Podcast"
    elif 'Crypto Until Infinity' in title:
        return 'Crypto Until Infinity'
    else:
        return 'The Bitcoin Podcast'