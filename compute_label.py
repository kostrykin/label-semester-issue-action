#!/usr/bin/env python

from datetime import date


def compute_label(year, month):
    if month < 6:
        return f'WS {year - 1}/{year}'
    else:
        return f'WS {year}/{year + 1}'


today = date.today()
year  = today.year % 2000
month = today.month

label = compute_label(year, month)
print(label)