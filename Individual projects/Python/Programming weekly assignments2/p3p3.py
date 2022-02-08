print('purchase price= 192105.40')
purchase_price=float(192105.40)
#ratio 60:40
larger_percentage= (purchase_price*60/100)
smaller_percentage= (purchase_price*40/100)
print('Ratio 60:40')
print('60% of purcahse price=', purchase_price*60/100)
print('40% of purchase price=', purchase_price*40/100)

print()

print('calculating tax at 13.5% of',larger_percentage)
print('calculating tax at 23% of', smaller_percentage)


higher_tax_rate= 23
lower_tax_rate=13.5

print('total tax=',(larger_percentage*13.5/100)+(smaller_percentage*23/100))
total_tax=(33234.2342)
print('total including all tax:',total_tax+purchase_price)
