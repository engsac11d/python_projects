# operators = evaluate a multiple conditins (or , and , not)
temp = 20
its_sunny = True
if temp >= 28 and its_sunny:
    print ("It iS HOT OUTSIDE 🥵")
    print ("its sunny 🌞")
elif temp <= 0 and its_sunny:
    print("its cold outside 🥶")
    print("its very cold ❄️")
elif temp > 28 and temp < 0 and its_sunny :
    print("its warm outside 😊" )
    print("its sunny ☀️")
elif temp >= 28 and not its_sunny:
    print ("It iS HOT OUTSIDE 🥵")
    print ("its sunny 🌞")
elif temp <= 0 and not its_sunny:
    print("its cold outside 🥶")
    print("its very cold ❄️")
    


