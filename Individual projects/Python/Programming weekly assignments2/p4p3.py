purchase_price=float(input('what is the cost before tax?:'))
#ratio 60:40
larger_percentage= (purchase_price*60/100)
smaller_percentage= (purchase_price*40/100)
print('Ratio 60:40')
print('60% of purchase price=', purchase_price*60/100)
print('40% of purchase price=', purchase_price*40/100)
print('Total cost before VAT:',larger_percentage + smaller_percentage)

print()

print('calculating tax at 13.5% of',larger_percentage)
print('calculating tax at 23% of', smaller_percentage)


higher_tax_rate= 23
HVT=(larger_percentage*13.5/100)
lower_tax_rate=13.5
LVR=(smaller_percentage*23/100)

print('higher rate of vat:',HVT)
print('lower rate of vat:',LVR)
total_vat=(HVT + LVR)
print('Total VAT=',HVT + LVR)
print('Total purchase price including VAT:',total_vat + purchase_price)
