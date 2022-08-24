# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# i = 5

# def f(arg=i):
#     print(arg)

# i = 6
# f()

# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def f(a, L=None):
#     if L is None:
#          L = []
#          L.append(a)
#          return L

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# def cheeseshop(kind, *arguments, **keywords):
#      print("-- Do you have any", kind, "?")
#      print("-- I'm sorry, we're all out of", kind)
#      for arg in arguments:
#         print(arg)
#         print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#             shopkeeper="Michael Palin",
#              client="John Cleese",
#              sketch="Cheese Shop Sketch")
            
# print(concat("earth", "mars", "venus"))

# def concat(*args, sep="/"):
#     return sep.join(args)

# print(concat("earth", "mars", "venus"))
# print(concat("earth", "mars", "venus", sep="."))

# print(list(range(3, 6)))

# args = [3, 6]
# print(list(range(*args)))

#  def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# print(f(0))
# print(f(1))

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# def my_function():
#     """Do nothing, but document it.
    
#     No, really, it doesn't do anything.
#      """
    
#     pass
# print(my_function.__doc__)

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))
