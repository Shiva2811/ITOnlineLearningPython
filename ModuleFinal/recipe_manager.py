import json

#Creating class recipe
class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
    
    def to_dict(self):
        return{
            'title':self.title,
            'ingredients':self.ingredients,
            'instructions':self.instructions,
        }

    @staticmethod
    def from_dict(data):
        return Recipe(data['title'],data['ingredients'],data['instructions'])

recipes = []  #A list to hold recipes in empty memory

#Add new recipe
def add_recipe():
    title = input("Enter title : ")
    ingredients = input("Enter ingredents (comma-seprated): ").split(",")
    instructions = input("Enter instrictions : ")
    new_recipe = Recipe(title,ingredients,instructions)
    recipes.append(new_recipe)
    print("Recipie added sucessfully!")

#View all recipes
def view_recipes():
    if recipes:
        for recipe in recipes:
            print(f"\nTitle: {recipe.title} \nIngredients: {', '.join(recipe.ingredients)} \nInstructions: {recipe.instructions}")
    else:
        print("No recipes available.")

#Search recipes by title or ingredients
def search_recipe(keyword):
    results = [ recipe for recipe in recipes if keyword.lower() in recipe.title.lower() or keyword.lower() in ' '.join(recipe.ingredients).lower()]
    if results:
        for recipe in results:
            print(f"\nTitle: {recipe.title} \nIngredients: {', '.join(recipe.ingredients)} \nInstructions{recipe.instructions}")
    else:
        print("No recipes found.")

#Edit recipe
def edit_recipe(title):
    recipe = next ((r for r in recipes if r.title.lower()== title.lower()),None)
    if recipe:
        recipe.title = input("Enter new title (leave blank to keep current): ") or recipe.title
        recipe.ingredients = input("Enter new ingredients (comma-separated, leave blank to keep current): ").split(", ") or recipe.ingredients
        recipe.instructions = input("Enter new instructions (leave blank to keep current): ") or recipe.instructions
        print("Recipie updated sucessfully!")
    else:
        print("Recipe not found.")

#Delete reciepe
def delete_recipe(title):
    global recipes
    recipes = [r for r in recipes if r.title.lower() != title.lower()]
    print("Recipe deleted sucessfully")


#Save recipes to file
def save_recipe_to_file(filename="ITOnlineLearning/recipes.json"):
    with open(filename,"w") as file:
        json.dump([recipe.to_dict() for recipe in recipes], file)
    print("Recipe saved to file.")

def load_recipe_from_file(filename="ITOnlineLearning/recipes.json"):
    global recipes
    try:
        with open(filename,"r") as file:
            recipes_data = json.load(file)
            recipes = [Recipe.from_dict(data) for data in recipes_data]
    except FileNotFoundError:
        print("No saved recipes found.")




#Command-Line Interface(CLI)

def main():
    load_recipe_from_file()
    # Define the options using a dictionary to map choices to functions
    options = {
        "1": add_recipe,
        "2": view_recipes,
        "3": lambda: search_recipe(input("Enter keyword to search: ")),
        "4": lambda: edit_recipe(input("Enter the title of the recipe to edit: ")),
        "5": lambda: delete_recipe(input("Enter the title of the recipe to delete: ")),
        "6": lambda: (save_recipe_to_file(), exit())
    }
    while True:
        print("\nRecipe Manager\n1. Add Recipe\n2. View All Recipes\n3. Search Recepes\n4. Edit Recipes\n5. Delete Recepies\n6. Save & Exit")
        choice = input("Choose an option: ")
        # Call the function associated with the choice, or print an error if invalid
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, please try again.")
if __name__=="__main__":
    main()