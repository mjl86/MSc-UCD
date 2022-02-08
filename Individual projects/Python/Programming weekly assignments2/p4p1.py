euro_Aud_rate= float(1.63)
euro_USD_rate= float(1.17)

print('sell rate of Aud:', euro_Aud_rate)

print()

print('sell rate of USD:', euro_USD_rate)

print()
print('Converting Euro to Australian Dollars')

amount_to_exchange=float(input('Enter how much would you like to exchange:'))

print('conversion is:', amount_to_exchange*euro_Aud_rate)

print()

print('Converting Euro to American Dollars')
amount_to_exchange=int(input('Enter how much would you like to exchange:'))

print('conversion is:', amount_to_exchange*euro_USD_rate)
