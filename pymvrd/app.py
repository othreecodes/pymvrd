#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
pyMVRD
Nigerian Motor Vehicle Registration Lookup
__author__ = 'othreecodes'
'''
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from pymvrd.errors import *

BASE_URL = 'http://www.lsmvaapvs.org'


def parse_response(response):
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        data = soup.find_all('td')
    except:
        raise InvalidPlateError

    # Cleaning the HTML tags from the string
    for i in range(0, len(data)):
        data[i] = clean_html_tags(str(data[i]))

    # Turning the list into a dict
    data_dict = dict(zip(*[iter(data)] * 2))
    return data_dict


def clean_html_tags(raw_html):
    # Clean the HTML tags from response
    clean = re.compile('<.*?>')
    clean_text = re.sub(clean, '', raw_html)
    return clean_text


class Plate:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def __str__(self):
        return str(self.raw_data)

    def __unicode__(self):
        return str(self.raw_data)

    def number(self):
        return self.raw_data['Plate Number']

    def issue_date(self):
        date = self.raw_data['Isssue Date'][0:-4]
        date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return date_object

    def vehicle_status(self):
        return self.raw_data['Vehicle Status']

    def chasis_number(self):
        return self.raw_data['Chasis Number']

    def expiry_date(self):
        date = self.raw_data['Expiry Date'][0:-4]
        date_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return date_object

    def owner_name(self):
        return self.raw_data['Owner Name']

    def model(self):
        return self.raw_data['Model']

    def color(self):
        return self.raw_data['Color']


class Mvrd:
    '''MVRD Class'''

    def __init__(self, plate_number):
        self.plate_number = plate_number

    '''Getting the raw html from www.lsmvaapvs.org'''

    def get_data(self):
        response = requests.get(BASE_URL + '/search.php', {'vpn': self.plate_number})
        data = parse_response(response=response)
        if data == {}:
            raise InvalidPlateError("The Plate number does not exist")

        pretty_data = Plate(data)
        return pretty_data
