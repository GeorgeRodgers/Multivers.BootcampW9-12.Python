from recipes import recipes

def list_recipes():
    print('\nRecipes Available:\n')
    for recipe in recipes:
        print(recipe['name'])
  
def query_recipe():
    query_name = input("Enter the name of the recipe you want to search for: ")
    
    found_recipes = []

    for recipe in recipes:
        if query_name.lower() in recipe['name'].lower():
            found_recipes.append(recipe)
    
    if found_recipes:
        print(f"\nFound {len(found_recipes)} matching recipes:")
        for recipe in found_recipes:
            print(f"\nRecipe: {recipe['name']}\nIngredients: {', '.join(recipe['ingredients'])}\nInstructions:")
            for step, instruction in recipe['instructions'].items():
                print(f"{step}: {instruction}")
    else:
        print("No matching recipes found.")
        
def find_recipes_by_ingredients(available_ingredients):
    matching_recipes = []
    for recipe in recipes:
        if all(ingredient in recipe['ingredients'] for ingredient in available_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes
    
def main():
    print("Welcome to the Recipe Book CLI Application!")
    
    while True:
        print("\nChoose an option:")
        print("1. List recipes")
        print("2. Query recipes")
        print("3. Search by ingredients")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            list_recipes()
        elif choice == "2":
            query_recipe()
        elif choice == "3":
            available_ingredients = input("\nEnter the ingredients you have (comma-separated): ").title().split(',')
            available_ingredients = [ingredient.strip() for ingredient in available_ingredients]
            
            matching_recipes = find_recipes_by_ingredients(available_ingredients)
            
            if matching_recipes:
                print("\nYou can make the following recipes:\n")
                for recipe in matching_recipes:
                    print(recipe['name'])
            else:
                print("\nNo recipes found with the given ingredients.")
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
