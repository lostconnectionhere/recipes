
# Prepare 

## Database creation
Create a `create_db.py` that creates all the necessary tables and databases.

## Content creation
Create a `seed_db.py` that creates at least 5 dummy entries in the database.

## Reset
Create a `reset.py` that drops all tables from the database and re-executes create_db.py and seed_db.py

# Assignment 1

The idea is to create a traversable menu in the terminal.
It should offer FULL CRUD operations for both recipes and ingredients.

```sh
[ Main Menu ]
[0]: Exit
[1]: Recipes Menu
[2]: Ingredients Menu

```

```sh
[ Recipes Menu ]
[0]: Back to Main Menu
[1]: List recipes # all recipes, summary of only [ID, TITLE]
[2]: Get recipe # a single recipe, more detailed
[3]: Add recipe
[4]: Update recipe
[5]: Delete recipe
```

```sh
> list recipes
The recipes that you have are: 
[ID]: [TITLE]
[ID]: [TITLE]
[ID]: [TITLE]
[ID]: [TITLE]

...Should be back in the recipes menu after chosing 1.
```

```sh
> get recipe 1
The recipe for [TITLE] is
[Ingredient]
[Ingredient]
[Ingredient]
[Ingredient]
[Ingredient]
[Ingredient]

...Should be back in the recipes menu after chosing 2.
```

