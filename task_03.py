#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" a program to calculate the lifetime compound interest of a loan.
"""

# from fractions import Fraction
from decimal import Decimal
# import locale

LOANERNAME = raw_input('What is your First and last name?\n')

PRINCIPAL = raw_input('What is the principal of the loan?\n')

LOANTREM = raw_input('how long is this being borrowed?\n')

PRE_QUALIFIED = raw_input('Are you pre-qualified Yes or No?\n')

PRE_QUALIFIED = PRE_QUALIFIED[:1].lower()
P = float(PRINCIPAL)
T = float(LOANTREM)

N = 12   # interest is compounded monthly ( so n = 12 in our above equation ).

if P >= 1000000 and PRE_QUALIFIED == 'y':

    if 16 <= T <= 20:

        R = float(2.62/100)

    elif 1 <= T <= 15:

        R = float(2.05/100)

    else:

        R = 0


elif 200000 <= P <= 999999 and PRE_QUALIFIED == 'y':

    if 21 <= T <= 30:

        R = float(4.66/100)

    elif 16 <= T <= 20:

        R = float(3.27/100)

    elif 1 <= T <= 15:

        R = float(3.02/100)

    else:

        R = 0

elif 200000 <= P <= 999999 and PRE_QUALIFIED == 'n':

    if 16 <= T <= 20:

        R = float(4.08/100)

    elif 1 <= T <= 15:

        R = float(3.98/100)

    else:

        R = 0

elif 0 <= P <= 199999 and PRE_QUALIFIED == 'y':

    if 21 <= T <= 30:

        R = float(5.77/100)

    elif 16 <= T <= 20:

        R = float(4.04/100)

    elif 1 <= T <= 15:

        R = float(3.63/100)

    else:

        R = 0

elif 0 <= P <= 199999 and PRE_QUALIFIED == 'n':

    if 21 <= T <= 30:

        R = float(6.39/100)

    elif 16 <= T <= 20:

        R = float(4.98/100)

    elif 1 <= T <= 15:

        R = float(4.65/100)

    else:

        R = 0

if R == 0:

    TOTAL = None

else:

    A = Decimal(P*(1 + (R/N))**(T*N))
    TOTAL = (round(A, 2))
    TOTAL = '$'+'{0:,}'.format(TOTAL)

print '\n\n'
# print ('Loan Report for: {0}\n').format(NAME)
# print('-'*80)
PRINCIPAL = '$'+'{0:,}'.format(P)
LOANTREMS = LOANTREM + 'yrs'
# print ('{0:>20}''{1:>20}').format('Principal:',PRINCIPAL)
# print ('{0:>20}''{1:>20}').format('Duration:',LOANTREMS)
# print('{0:>20}''{1:>20}').format('Pre-qualified?:',PRE_QUALIFIED)

# print('\n')
# print ('{0:>20}''{1:>20}').format('Total:',TOTAL)

REPORT = ('Loan Report for: {}\n{}\n{:>20}{:>20}\n{:>20}{:>20}\n'
          '{:>20}{:>20}\n\n{:>20}{:>20}').format(LOANERNAME, '-'*80,
                                                 'Principal:',
                                                 PRINCIPAL, 'Duration:',
                                                 LOANTREMS,
                                                 'Pre-qualified?:',
                                                 PRE_QUALIFIED,
                                                 'Total:', TOTAL)
print REPORT
