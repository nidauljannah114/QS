# shoplist = ['apple', 'mango', 'carrot', 'banana']

# print('I have', len(shoplist), 'items to purchase.')

# print('These items are:', end=' ')
# for item in shoplist:
#     print(item, end=' ')

# print('\nI also have to buy rice.')
# shoplist.append('rice')
# print('My shopping list is now', shoplist)

# print('I will sort my list now')
# shoplist.sort()
# print('Sorted shopping list is', shoplist)

# print('The first item I will buy is', shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print('I bought the', olditem)
# print('My shopping list is now', shoplist)

# zoo = ('python', 'elephant', 'penguin')
# print('Number of animals in the zoo is', len(zoo))

# new_zoo = 'monkey', 'camel', zoo    
# print('Number of cages in the new zoo is', len(new_zoo))
# print('All animals in new zoo are', new_zoo)
# print('Animals brought from old zoo are', new_zoo[2])
# print('Last animal brought from old zoo is', new_zoo[2][2])
# print('Number of animals in the new zoo is',
#       len(new_zoo)-1+len(new_zoo[2]))

# ab = {
#     'Swaroop': 'swaroop@swaroopch.com',
#     'Larry': 'larry@wall.org',
#     'Matsumoto': 'matz@ruby-lang.org',
#     'Spammer': 'spammer@hotmail.com'
# }

# print("Swaroop's address is", ab['Swaroop'])


# del ab['Spammer']

# print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

# for name, address in ab.items():
#     print('Contact {} at {}'.format(name, address))


# ab['Guido'] = 'guido@python.org'

# if 'Guido' in ab:
#     print("\nGuido's address is", ab['Guido'])

# shoplist = ['apple', 'mango', 'carrot', 'banana']
# name = 'swaroop'

# # Indexing or 'Subscription' operation #
# print('Item 0 is', shoplist[0])
# print('Item 1 is', shoplist[1])
# print('Item 2 is', shoplist[2])
# print('Item 3 is', shoplist[3])
# print('Item -1 is', shoplist[-1])
# print('Item -2 is', shoplist[-2])
# print('Character 0 is', name[0])

# # Slicing on a list #
# print('Item 1 to 3 is', shoplist[1:3])
# print('Item 2 to end is', shoplist[2:])
# print('Item 1 to -1 is', shoplist[1:-1])
# print('Item start to end is', shoplist[:])

# # Slicing on a string #
# print('characters 1 to 3 is', name[1:3])
# print('characters 2 to end is', name[2:])
# print('characters 1 to -1 is', name[1:-1])
# print('characters start to end is', name[:])

# shoplist = ['apple', 'mango', 'carrot', 'banana']
# print(shoplist[::1])
# print(shoplist[::2])
# print(shoplist[::3])
# print(shoplist[::-1])

# bri = set(['brazil', 'russia', 'india'])
# print('india' in bri)
# print('usa' in bri)
# bric = bri.copy()
# bric.add('china')
# print(bric.issuperset(bri))
# bri.remove('russia')
# print(bri & bric) # OR bri.intersection(bric)

# print('Simple Assignment')
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# # mylist is just another name pointing to the same object!
# mylist = shoplist

# # I purchased the first item, so I remove it from the list
# del shoplist[0]

# print('shoplist is', shoplist)
# print('mylist is', mylist)
# # Notice that both shoplist and mylist both print
# # the same list without the 'apple' confirming that
# # they point to the same object

# print('Copy by making a full slice')
# # Make a copy by doing a full slice
# mylist = shoplist[:]
# # Remove first item
# del mylist[0]

# print('shoplist is', shoplist)
# print('mylist is', mylist)
# # Notice that now the two lists are different

# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))