#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using ternary expression to build a simple alarm clock with snooze function
"""

# Ask the user what day

DAYOFWEEK = raw_input('What day of the week is it?:\n')

ALAMTIME = raw_input('What time is it? enter time in 4-digit 24 hours format'
                     '(eg,0605):\n')

# while(len(ALAMTIME)!=4):
# raw_input('wrong time format, enter time again: ')

DAYOFWEEK = DAYOFWEEK[:3].lower()

"""if sat' or 'sun' or the user-submitted time is less-than 600, set SNOOZE to
True,otherwise set it to False
"""

SNOOZESET = (DAYOFWEEK == 'sat' or DAYOFWEEK == 'sun' or ALAMTIME < '0600')

SNOOZE = True if(SNOOZESET)else False


if SNOOZE is False:
    ALARM = 'Beep! '
    print ALARM*5
