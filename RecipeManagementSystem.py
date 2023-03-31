import sys,json
class Recipe:
    def __init__(self,name,ingredients,instructions,category,rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.rating = rating

class RMS:
    def __init__(self):
        self.recipes = []
        
        
    def addRecipe(self,recipe):
        ids = len(self.recipes)+1
        for i in self.recipes:
            if (i['id']==ids) or (i['id']>ids):
                ids = i['id']+1
        if (type(recipe.name)==int) or (recipe.name==""):
            print("Error: Enter a string input for recipe name")
            return
        if (recipe.ingredients=="") or (type(recipe.ingredients)==int):
            print("Error: Enter ingredients for recipe")
            return
        if (recipe.instructions=="") or (type(recipe.instructions)==int):
            print("Error: Enter instructions for recipe")
            return
        if (type(recipe.category)==int) or (recipe.category==""):
            print("Error: Enter a string input for recipe category")
            return
        if (type(recipe.rating)==str) or (recipe.rating==""):
            print("Error: Enter a int input for recipe rating")
            return
        dict_rec = {'id':ids, 'name':recipe.name,'ingredients':recipe.ingredients,'instructions':recipe.instructions,'category':recipe.category,'rating':recipe.rating}
        for x in self.recipes:
            if x['name'] == recipe.name:
                print("\nRecipe already exists")
                return
        check = len(self.recipes)
        self.recipes.append(dict_rec)
        if len(self.recipes)>check:
            print("\nRecipe Added")


    def viewRecipe(self):
        return
            

    def deleteRecipe(self):
        return


    def editRecipe(self):
        return


    def exportRecipe(self):
        return


    def importRecipe(self):
        return


    def askUserOptions(self):
        return
           
            
    def exitRecipe(self):
        return
