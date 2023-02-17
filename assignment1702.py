import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "mydb_test"
)

mycursor = mydb.cursor()

def showMainMenu(): 
    # show main menu
    print("\n\n*********************")
    print("[Main Menu]")
    print("[0] Exit")
    print("[1] Recipe Menu")
    print("[2] Ingredient Menu")
    print("*********************")

    userChoice = int(input("Make a choice: "))

    if userChoice == 0:
        print("Goodbye")
    elif userChoice == 1:
        showRecipeMenu()
    elif userChoice == 2:
        showIngredientMenu()
    else:
        print("Unrecognized option: " + userChoice + " please make another choice")
        showMainMenu()

def showRecipeMenu(): 
    print("\n\*********************")
    print("[RECIPE MENU]")
    print("[0] Back to Main Menu")
    print("[1] List recipes")
    print("[2] Get recipes")
    print("*********************")

    userChoice = int(input("Make a choice: "))

    if userChoice == 0:
        showMainMenu()
    elif userChoice == 1:
        listRecipes()
        showRecipeMenu()
    elif userChoice == 2:
        recipeId = int(input("Recipe ID: "))
        getRecipe(recipeId)
    else:
        print("Unrecognized option: " + userChoice + " please make another choice")
        showRecipeMenu()

    showMainMenu()

def listRecipes(): 
    print("\n<<< Your results are")
    mycursor.execute("SELECT recipe_id, recipe_name_EN FROM recipes")
    result_rec = mycursor.fetchall()

    for recipe in result_rec: 
        print("[%d] %s" % recipe)
    
    print (">>> DONE")

def getRecipe(recipeId):
    print("Fetching recipe " + str(recipeId))

def showIngredientMenu():
    print("\n[INGREDIENT MENU]")
    print("\n<<< Your results are")
    mycursor.execute("SELECT ingredient_id, ingredient_name FROM ingredients")
    result_ing = mycursor.fetchall()

    for ingredient in result_ing: 
        print("[%d] %s" % ingredient)
    
    print (">>> DONE")

showMainMenu()