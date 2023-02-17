import mysql.connector
from assignment1702 import show_main_menu 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

def show_recipe_menu(): 
    print("\n\*********************")
    print("[RECIPE MENU]")
    print("[0] Back to Main Menu")
    print("[1] List recipes") 
    print("[2] Get recipes")
    print("[3] Update recipe")
    print("[4] Delete recipe")
    print("*********************")

    user_choice = int(input("Make a choice: "))

    if user_choice == 0:
        show_main_menu()
    elif user_choice == 1:
        list_recipes()
        show_recipe_menu()
    elif user_choice == 2:
        recipe_id = int(input("Recipe ID: "))
        get_recipe(recipe_id)
    else:
        print("Unrecognized option: " + user_choice + " please make another choice")
        show_recipe_menu()

    show_main_menu()

def list_recipes(): 
    print("\n<<< Your results are")
    mycursor.execute("SELECT recipe_id, recipe_name_EN FROM recipes")
    result_rec = mycursor.fetchall()

    for recipe in result_rec: 
        print("[%d] %s" % recipe)
    
    print (">>> DONE")

def get_recipe(recipe_id):
    print("Fetching recipe " + str(recipe_id))


def update_recipe():
    old_rec_id = input("Which recipe name do you want to update? Give ID number ")
    new_rec_name = input("Sure, to what recipe name do you want to update it to? ")
    sql_update_rec = "UPDATE recipes SET recipe_name_EN =" + new_rec_name + "WHERE recipe_id =" + old_rec_id
    mycursor.execute(sql_update_rec)
    mydb.commit()

def delete_recipe():
    user_correct_input = input("Do you want to delete a recipe? [y/n]")
    if user_correct_input == "y":
            delete_rec_id = input("Ok, great! What recipe do you want to delete? Give ID number ")
            sql_del_rec = "DELETE FROM recipes WHERE recipe_id = " + delete_rec_id
            mycursor.execute(sql_del_rec)
            mydb.commit()
    elif user_correct_input == "n":
        print("Ok, nothing will be deleted")
    else: 
        print("Unrecognized option: " + user_correct_input + " please make another choice")
        delete_recipe()
