#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" a program to pick 3 color for a redesigning: BASE color, an ACCENT color,
and a HIGHLIGHT color. To help you pick, you'll build a decision tree where you
select each of your three colors one-at-a-time from the selections below.
"""


BASE = raw_input('Which \"BASE" color, \"Seattle Gray" or \"Manatee"?:\n')

if BASE == 'Seattle Gray':

    ACCENT = raw_input('Which \"ACCENT" color, \"Ceramic Glaze" or'
                       '\"Cumulus Nimbus"?:\n')
elif BASE == 'Manatee':

    ACCENT = raw_input('Which \"ACCENT" color, \"Platinum Mist" or'
                       '\"Spartan Sage"?:\n')

else:

    print 'wrong color choice'

if ACCENT == 'Ceramic Glaze':

    HIGHLIGHT = raw_input('Which \"HIGHLIGHT" color,\"Basically White" or'
                          '\"White":\n')

elif ACCENT == 'Cumulus Nimbus':

    HIGHLIGHT = raw_input('Which \"HIGHTLIGHT" color, \"Off-White" or'
                          '\"Paper White":\n')

elif ACCENT == 'Platinum Mist':

    HIGHLIGHT = raw_input('Which \"HIGHTLIGHT" color, \"Bone White" or'
                          '\"Just White":\n')

elif ACCENT == 'Spartan Sage':

    HIGHLIGHT = raw_input('Which highlight color, \"Fractal White" or'
                          '\"Not White":\n')

else:
    print 'wrong color choice'

if HIGHLIGHT != 'Fractal White' or HIGHLIGHT != 'Not White':
    if HIGHLIGHT != 'Just White' or HIGHLIGHT != 'Bone White':
        if HIGHLIGHT != 'Off-White' or HIGHLIGHT != 'Paper White':
            if HIGHLIGHT != 'Basically White' or HIGHLIGHT != 'White':
                print 'Sorry, wrong color choice'
else:

    print 'Your selected colors are, {0},{1}, and {2}.'.format(BASE, ACCENT,
                                                               HIGHLIGHT)
