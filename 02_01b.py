from collections import deque

def main():
    #add code here
    ordered_food = deque(maxlen=5)
    ordered_food.append("food_1")
    print(ordered_food)
    ordered_food.append("food_2")
    print(ordered_food)
    other_food = ['food_3', 'food_4', 'food_5']
    ordered_food.extend(other_food)
    print(ordered_food)
    ordered_food.append('food_6')
    print(ordered_food)
    return 

if __name__ == "__main__":
    main()