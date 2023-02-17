from assignment1702 import show_main_mneu
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

user_correct_input = input("Do you want to delete an input? [y/n]")

def delete_item():
    if user_correct_input == 'y':
        delete_item_cat = input("Ok, great! Do you want to delete an ingredient or recipe? ")
        if delete_item_cat == "ingredient":
            delete_ingredient = input("What ingredient do you want to delete? ")
            sql_del_ing = "DELETE FROM ingredients WHERE ingredient_name = " + delete_ingredient
            mycursor.execute(sql_del_ing)
            mydb.commit()
        elif delete_ingredient == "recipe":
            delete_recipe = input("What recipe do you want to delete? ")
            sql_del_rec = "DELETE FROM ingredients WHERE recipe_name_EN = " + delete_recipe
            mycursor.execute(sql_del_rec)
            mydb.commit()
        else:
            print("Unrecognized option: " + user_correct_input + " please make another choice")
            delete_item()
    elif user_correct_input == 'n':
            print("Ok, nothing will be deleted")
    else:
        print("Unrecognized option: " + user_correct_input + " please make another choice")
        show_main_mneu()

