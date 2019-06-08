import random

flag = 'ABCD'
MY_LUCKY_NUMBER = 29486316

# I need to bake special stuff!
def bake_it():
    s = 0
    for i in range(random.randint(10000,99999)):
        s = random.randint(100000000000,999999999999)
    s -= random.randint(232,24895235)
    return random.randint(100000000000,999999999999)

# Create my random mess
def rand0m_mess(food,key):
    mess = []
    mess.append(key)
    print('mess     ', mess)

    art = key
    bart = bake_it()
    cart = bake_it()
    dart = bake_it()
    print('bart     ', bart)
    print('cart     ', cart)
    print('dart     ', dart)
    print('art0     ', art)
    for i in range(len(food)-1):
        art = (art*bart+cart)%dart
        print(f'art{i+1}     ', art)
        mess.append(art)
    return mess

# Gotta prepare the food!!!
def prepare(food):
    good_food = []
    for i in range(len(food)):
        good_food.append(food[i]^MY_LUCKY_NUMBER)
    for k in range(len(good_food)):
        good_food[i] += MY_LUCKY_NUMBER
    return good_food

# Bake it!!!
def final_baking(food,key):
    baked = rand0m_mess(food,key)
    print('baked    ', baked)
    treasure = []
    for i in range(len(baked)):
        treasure.append(ord(food[i])*baked[i])
    print('treasure1', treasure)
    treasure = prepare(treasure)
    print('prepared ', treasure)
    return treasure

key = bake_it()
prepared = final_baking(flag,key)

print('-'*50)
def reverse_prepare(food):
    # reverse luck number
    food[len(food)-1] -= MY_LUCKY_NUMBER * len(food)
    # reverse XOR
    good_food = []
    for i in range(len(food)):
        good_food.append(food[i]^MY_LUCKY_NUMBER)
    return good_food

print('treasure2', reverse_prepare(prepared))
