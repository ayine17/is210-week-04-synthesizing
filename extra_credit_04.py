#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" extra credut 4"""

# NAME = raw_input('Enter Customer Name\n')
CREDITLIMIT = raw_input(" what is customer credit limit ")
CREDITLIMIT = int(CREDITLIMIT)


def credit_limit(limit):
    """fuction that determine customer credit levels:PLATINUM,GOLD and SILVER
    arg:
        CREDITLIMIT(int): credit limit entered by the user

    Return: return string credit levels:PLATINUM,GOLD and SILVER

    example:
        >>> credit_limit(CREDITLIMIT)
        'GOLD'
        >>> credit_limit(56000)
        'PLATINUM'
        >>> credit_limit(456)
        'SILVER'
    """

    if CREDITLIMIT > 50000:
        level = 'PLATINUM'
    elif 50000 >= CREDITLIMIT >= 10000:
        level = 'GOLD'

    else:
        level = 'SILVER'
    return level

    print 'Custome {} is {} card holder'.format(NAME, level)
