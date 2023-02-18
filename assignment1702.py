import mysql.connector
from recipe import show_recipe_menu # list_recipes, get_recipe
from ingredient import show_ingredient_menu # list_ingredients, get_ingredient, update_ingredient, delete_ingredient

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()


def show_main_menu(): 
    # show main menu
    print("\n\n*********************")
    print("[Main Menu]")
    print("[0] Exit")
    print("[1] Recipe Menu")
    print("[2] Ingredient Menu")
    print("*********************")

    user_choice = int(input("Make a choice: "))

    if user_choice == 0:
        print("Goodbye")
    elif user_choice == 1:
        show_recipe_menu()
    elif user_choice == 2:
        show_ingredient_menu()
    else:
        print("Unrecognized option: " + user_choice + " please make another choice")

    show_main_menu()


# Start of script
show_main_menu()