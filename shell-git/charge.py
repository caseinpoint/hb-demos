import os
CREDIT_CARD = os.environ['CREDIT_CARD']

def charge_card(amt, card):
    print(f'Charging ${amt} to {card}')

charge_card(100, CREDIT_CARD)
