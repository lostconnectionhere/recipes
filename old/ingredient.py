import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()
def show_ingredient_menu():
    print("\n\*********************")
    print("[INGREDIENT MENU]")
    print("[0] Back to Main Menu")
    print("[1] List ingredients") 
    print("[2] Get ingredients")
    print("[3] Update ingredients")
    print("[4] Delete ingredients")
    print("*********************")

    user_choice = int(input("Make a choice: "))

    if user_choice == 0:
        return
    elif user_choice == 1:
        list_ingredients()
    elif user_choice == 2:
        ingredient_id = int(input("Recipe ID: "))
        get_ingredient(ingredient_id)
    elif user_choice == 3:
        update_ingredient()
    elif user_choice == 4:
        delete_ingredient()
    else:
        print("Unrecognized option: " + user_choice + " please make another choice")
        show_ingredient_menu()
    show_ingredient_menu()

def list_ingredients(): 
    print("\n<<< Your results are")
    mycursor.execute("SELECT ingredient_id, ingredient_name FROM ingredients")
    result_ing = mycursor.fetchall()
    for ingredient in result_ing:
        print(ingredient)

def get_ingredient(ingredient_id):
    print("Fetching ingredient " + str(ingredient_id)) 
    print (">>> DONE")

def update_ingredient():
    old_ing_id = input("Which ingredient do you want to update? ")
    new_ing_name = input("Sure, to what ingredient do you want to update it to? ")
    sql_update_ing = "UPDATE ingredients SET ingredient_name =" + new_ing_name + "WHERE ingredient_id =" + old_ing_id
    mycursor.execute(sql_update_ing)
    mydb.commit()

def delete_ingredient():
    user_correct_input = input("Do you want to delete an ingredient? [y/n]")
    if user_correct_input == "y":
            delete_ing_id = input("Ok, great! What ingredient do you want to delete? ")
            sql_del_ing = "DELETE FROM ingredients WHERE ingredient_id = " + delete_ing_id
            mycursor.execute(sql_del_ing)
            mydb.commit()
    elif user_correct_input == "n":
        print("Ok, nothing will be deleted")
    else: 
        print("Unrecognized option: " + user_correct_input + " please make another choice")
        delete_ingredient()
        
    delete_ingredient()

    