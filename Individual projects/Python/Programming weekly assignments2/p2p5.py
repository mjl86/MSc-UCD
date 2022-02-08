
animals= 'herd of elephants'
seg= animals[0:4]
print('Segement is:', seg)

animals= 'herd of elephants'
seg= animals[1:1]
print('Segement is:', seg)
# result is blank

animals= 'herd of elephants'
seg= animals[8:5]
print('Segement is:', seg)
#x can't be bigger than y as it is read sequentially and that would mean back to front

animals= 'herd of elephants'
seg= animals[:6]
print('Segement is:', seg)
#When x is omitted the range it print from the start of the string to the designated number.

animals= 'herd of elephants'
seg= animals[3:]
print('Segement is:', seg)
#when y is omitted it prints from the value of x to the end of the string.

animals= 'herd of elephants'
seg= animals[:]
print('Segement is:', seg)
#When both x and y are omitted it gives you the full range of the string

animals= 'herd of elephants'
seg= animals[-9:-1]
print('Segement is:', seg)

animals= 'herd of elephants'
seg= animals[-15:-1]
print('Segement is:', seg)
#You can also have negative values for x and y
