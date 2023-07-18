food = [
    "5 Литров воды",
    "3 Сухпойка",
    "Швецарский нож"
]
while len(food) < 10:
    questions = input("что вы ещё хотите взять?)")
   
    
    if questions in food:
        print("У вас уже это есть:(")
    else:
        food.append(questions)
        print(food)
