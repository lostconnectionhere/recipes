import mysql.connector

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
        return
    elif user_choice == 1:
        list_recipes()
    elif user_choice == 2:
        recipe_id = int(input("Recipe ID: "))
        get_recipe(recipe_id)
    elif user_choice == 3:
        update_recipe()
    elif user_choice == 4:
        delete_recipe()
    else:
        print("Unrecognized option, %d please make another choice" % (user_choice))
    show_recipe_menu()

    

def list_recipes(): 
    print("\n<<< Your results are")
    mycursor.execute("SELECT recipe_id, recipe_name_EN, recipe_name_KU, total_time, directions, author FROM recipes")
    result_rec = mycursor.fetchall()

    for recipe in result_rec: 
        print("""\n\
              id = [%d] 
              English name = %s 
              Kurdish name = %s 
              Total time = %s 
              Directions = %s 
              Author = %s""" % recipe)
    
    print (">>> DONE")

def get_recipe(recipe_id):
    print("Fetching recipe " + str(recipe_id))


def update_recipe():
    rec_update = input("Which recipe do you want to change? ")
    old_row_input = input("Pick a column: [recipe_id, recipe_name_EN, recipe_name_KU, total_time, directions, author]: ")
    new_row_input = input("Sure, to what do you want to update it to? ")
    sql_update_rec = "UPDATE recipes SET " + old_row_input +  " = '" + new_row_input + "' WHERE recipe_id =" + rec_update
    mycursor.execute(sql_update_rec)
    mydb.commit()

def delete_recipe():
    user_correct_input = input("Do you want to delete a recipe? [y/n]")
    if user_correct_input == "y":
        delete_rec_id = str(input("Ok, great! What recipe do you want to delete? Give ID number "))
        sql_del_rec = "DELETE FROM recipes WHERE recipe_id = " + delete_rec_id
        mycursor.execute(sql_del_rec)
        mydb.commit()
        
        if (mycursor.rowcount == 0):
            print("Nothing to be deleted")
        elif (mycursor.rowcount == 1):
            print ("Successfully deleted recipe")
        elif (mycursor.rowcount > 1):
            print ("Something bad happened.. deleted %d rows" % (mycursor.rowcount))
    elif user_correct_input == "n":
        print("Ok, nothing will be deleted")
    else: 
        print("Unrecognized option, please make another choice")
        delete_recipe()
