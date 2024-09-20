# Weathher_advice.py
#Prompt the user to input the current weather
weather = input("what's the weather like today? (sunny/rainy/cold): ").lower()
#Provide clothing recommendations based on the weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
    else:
        print("sorry, I don't have recommendation for this weather.")
