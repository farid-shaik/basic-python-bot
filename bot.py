"""
This is a program for a recipe chatbot which tells what are the ingredients required for a recipie.
1. the bot will start with a greeting and self intro and ask for name of the person
2. The bot will greet and welcome the person.
3. the bot asks the person what kind of recipie he wanted to make.
4. bot gives the list of ingredients required for making that recipie.
"""



from datetime import datetime

def greet_and_introduce():
    # bot will greet and introduce what task it will do
    greet = "hello user!\n I am your cooking guide. I will tell list of ingredients are required for some of delicious and yummy recipies i know\n Can you please tell me your name?"
    print(greet)
greet_and_introduce()



# bot asks name of the user
name = input("enter your name: " )
def ask_name():
    # says hello to the user
    print("Hello ", name)
ask_name()


# bot wish the user according to the time
def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour >= 12 and current_time.hour < 17 :
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour >= 17 and current_time.hour <= 22 :
        timeofday_greeting = "Good Evening"
    elif current_time.hour >22 :
        timeofday_greeting = "Hi, Thats Late"
    print(timeofday_greeting)
get_timeofday_greeting()



def show_menu():
    print("select the recipie you are going to prepare")
    print("1. veg Burger")
    print("2. Cheese Pizza")
    print("3. Egg  Noodles")
    print("4. Veg Pasta")
    print("5.  Doughnuts")
    print("6. exit")
    print("......................")
    try:
        return int(input("Enter your choice [1-6]:  "))
    except:
        print("only enter choice from 1, 2, 3, 4 and 5")
        return 0
choice = show_menu()
    
while choice!=6:
    # gives the list of ingredients required for making veg Burger
    if choice == 1:
        print("1 sliced onion\n"
        "4 slices cheese slices\n"
        "1 teaspoon powdered garam masala powder\n"
        "2 teaspoon refined oil\n"
        "1/2 gm ginger paste\n"
        "4 halved burger buns\n"
        "2 tablespoon tomato ketchup\n"
        "1/2 teaspoon garlic paste\n"
        "1 sliced tomato\n"
        "2 teaspoon powdered red chilli\n"
        "2 pinch powdered salt\n"
        "3 tablespoon breadcrumbs\n"
        "1 teaspoon lemon juice\n"
        "3 tablespoon butter\n"
        "1 handful chopped coriander leaves\n"
        "4 leaves lettuce loose-leaf\n"
        "1/2 peeled,sliced cucumber\n"
        "2 chopped onion\n"
        "1/2 cup shelled peas\n"
        "2 mashed,boiled,peeled potato\n"
        "2 chopped carrot\n"
        "1/2 cup corn\n")

    elif choice == 2:
        print("2 readymade pizza base\n"
        "1 1/2 tablespoon tomato ketchup\n"
        "1 pinch powdered black pepper\n"
        "150 gm shredded mozzarella\n"
        "1/2 teaspoon powdered salt\n"
        "100 gm chopped onion\n"
        "70 gm chopped capsicum ( green pepper)\n"
        "100 gm chopped tomato\n"
        "50 gm sliced mushroom\n")

    elif choice == 3:
        print("250 gm parboiled fresh noodles\n"
        "1 cup chopped,grated cabbage\n"
        "1 cup sliced onion\n"
        "2 teaspoon powdered black pepper\n"
        "1 cup sunflower oil\n"
        "3 teaspoon garlic paste\n"
        "1 cup finely chopped bean\n"
        "3 egg\n"
        "1 cup grated carrot\n"
        "7 sliced green chilli\n"
        "salt as required\n"
        "3 teaspoon ginger paste\n"
        "1 teaspoon ajinomoto\n"
        "2 tablespoon soy sauce\n"
        "1 handfuls chopped coriander leaves\n")

    elif choice == 4:
        # gives the list of ingredients required for making pasta
        print("250 gm pasta macaroni\n"
        "1 teaspoon garlic\n"
        "1 onion\n"
        "1 carrot\n"
        "1 teaspoon chilli flakes\n"
        "red chilli powder as required\n"
        "1 tablespoon tomato ketchup\n"
        "1 tablespoon red chilli sauce\n"
        "1 teaspoon ginger\n"
        "2 tomato\n"
        "1 capsicum (green pepper)\n"
        "1 green chillies\n"
        "salt as required\n"
        "1/2 teaspoon garam masala powder\n"
        "1 1/2 teaspoon soy sauce\n"
        "1/2 teaspoon oregano\n")

    elif choice == 5:
        print("=> 2 cup refined oil\n"
        "=> 4 teaspoon caster sugar\n"
        "=> 2 teaspoon baking powder\n"
        "=> 1 cup powdered sugar\n"
        "=> 2 cup milk\n"
        "=> 250 gm all purpose flour\n"
        "=> 2 tablespoon butter\n"
        "=> 7 gm dry yeast\n")
    elif choice == 6:
        exit()
    else:
        print("I dont understand that")
    choice = show_menu()


