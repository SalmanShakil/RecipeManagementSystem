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


    def viewRecipe(self,name):
        if len(self.recipes)==0:
            print("No recipes available to view")
            return
        x = False
        if type(name) != int:
            print("Error: Provide an int input as id to view recipe")
        for rec in self.recipes:
            if rec['id']==name:
                print("\nRecipe Name: "+rec['name'])
                print("Ingredients Required: "+rec['ingredients'])
                print("Instructions: "+rec['instructions'])
                print("Category: "+rec['category'])
                print("Rating: "+str(rec['rating']))
                x = True
        if x == False:
            print("Recipe not found")
            

    def deleteRecipe(self,name):
        x = False
        if type(name)!=int or name=="":
            print("Error: Provide an int input as id to delete recipe")
            return
        for rec in self.recipes:
            if rec['id']==name:
                self.recipes.remove(rec)
                print("\nRecipe Removed")
                x = True
            elif name == 0:
                return
        if x == False:
            print("Unable to delete, Recipe does not exist!")


    def editRecipe(self,name,ch,new_data):
        if type(name)!=int or name=="":
            print("Error: Provide an int input as id to edit recipe")
            return
        if type(ch)!=int or (ch>6 and ch<1):
            print("Error: Provide an int input between 1-6 as field id to edit recipe")
            return  
        for rec in self.recipes:
            if rec['id']==name:
                if ch==1:
                    if type(new_data)==int or (new_data=="") or (new_data.lstrip('-').isdigit()==True):
                        print("Error: Provide a valid recipe name")
                        return
                    rec['name']=new_data
                    print("Updated recipe "+rec['name'])
                elif ch==2:
                    if type(new_data)==int or (new_data=="") or (new_data.lstrip('-').isdigit()==True):
                        print("Error: Provide valid ingredients for recipe")
                        return
                    rec['ingredients']=new_data
                    print("Ingredients updated for "+rec['name'])
                elif ch==3:
                    if type(new_data)==int or (new_data=="") or (new_data.lstrip('-').isdigit()==True):
                        print("Error: Provide valid instructions for recipe")
                        return
                    rec['instructions']=new_data
                    print("Instructions updated for "+rec['name'])
                elif ch==4:
                    if type(new_data)==int or (new_data=="") or (new_data.lstrip('-').isdigit()==True):
                        print("Error: Provide valid category for recipe")
                        return
                    rec['category']=new_data
                    print("Category updated for "+rec['name'])
                elif ch==5:
                    if type(new_data)==str or (new_data=="") or new_data.startswith("-"):
                        print("Error: Provide int input for rating")
                        return
                    rec['rating']=new_data
                    print("Rating updated for "+rec['name'])
                else:
                    print("Select one of the fields available.")


    def exportRecipe(self,name):
        if len(self.recipes)==0:
            print("There are no recipes to export!")
            return
        jsonString = json.dumps(self.recipes)
        n = name+".json"
        jsonFile = open(n,"w")
        jsonFile.write(jsonString)
        jsonFile.close()
        print("\nRecipes Exported")


    def importRecipe(self,name):
        n = name+".json"
        fileObject = open(n, "r")
        jsonContent = fileObject.read()
        fileObject.close()
        aList = json.loads(jsonContent)
        self.recipes = aList
        print("\nRecipes Imported")


    def askUserOptions(self):
        print("What would you like to do?\n  1. Add a new recipe\n  2. Display a recipe\n  3. Delete an existing recipe\n  4. Edit an existing recipe\n  5. Export available recipes\n  6. Import new recipes\n  7. Exit\n")   
        while True:
            choice = input("Enter your choice: ")
            if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                break
            else:
                print("Enter a response from the available choices! ")
        while int(choice) != -1:
            if int(choice) == 1:
                while True:
                    name = input("Enter recipe name: ")
                    if not name.isnumeric() and name!="" and (name.lstrip('-').isdigit()==False):
                        break
                    else:
                        print("Enter a valid recipe name! ")
                while True:
                    ingredients = input("Enter ingredients required: ")
                    if ingredients !="" and (ingredients.lstrip('-').isdigit()==False) and not ingredients.isnumeric():
                        break
                    else:
                        print("Enter ingredients! ")
                while True:
                    instructions = input("Enter instructions for the recipe: ")
                    if instructions !="" and (instructions.lstrip('-').isdigit()==False) and not instructions.isnumeric():
                        break
                    else:
                        print("Enter instructions! ")
                while True:
                    category = input("Enter category: ")
                    if category !="" and (category.lstrip('-').isdigit()==False) and not category.isnumeric():
                        break
                    else:
                        print("Enter a valid category! ")                     
                while True:
                    rating = input("Provide ratings for the recipe: ")
                    if rating !="" and not rating.isalpha() and not rating.startswith("-"):
                        break
                    else:
                        print("Enter a valid rating! ")                
                rec = Recipe(name,ingredients,instructions,category,int(rating))     
                self.addRecipe(rec)
                while True:
                    choice = input("Enter your choice: ")
                    if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                        break
                    else:
                        print("Enter a response from the available choices! ")            
            if int(choice) == 2:
                print("\nAvailable recipes: ")
                for i in self.recipes:
                    print(str(i['id'])+". "+str(i['name']))
                while True:
                    name = input("\nEnter recipe id to view: ")
                    x = False
                    if len(self.recipes)==0:
                        x = True
                    for i in self.recipes:
                        if name==str(i['id']):
                            x = True
                    if not name.isalpha() and (x==True):   
                            break
                    else:
                        print("\nEnter an id from the available options! ")
                self.viewRecipe(int(name))
                while True:
                    choice = input("Enter your choice: ")
                    if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                        break
                    else:
                        print("Enter a response from the available choices! ")
            if int(choice) == 3:
                print("\nAvailable recipes: ")
                for i in self.recipes:
                    print(str(i['id'])+". "+str(i['name']))
                while True:
                    name = input("\nEnter recipe id to delete or enter 0 to exit: ")
                    x = False
                    for i in self.recipes:
                        if name==str(i['id']):
                            x = True
                    if not name.isalpha() and (x==True or name=='0'):
                        break
                    else:
                        print("\nEnter an id from the available options or enter 0 to exit! ")      
                self.deleteRecipe(int(name))
                while True:
                    choice = input("Enter your choice: ")
                    if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                        break
                    else:
                        print("Enter a response from the available choices! ")
            if int(choice) == 4:
                print("\nAvailable recipes: ")
                for i in self.recipes:
                    print(str(i['id'])+". "+str(i['name']))
                while True:
                    name = input("\nEnter recipe name to edit: ")
                    x = False
                    for i in self.recipes:
                        if name==str(i['id']):
                            x = True
                    if not name.isalpha() and (x==True):
                        break
                    else:
                        print("\nEnter an id from the available options! ")              
                print("Available fields to edit:\n  1. name\n  2. ingredients\n  3. instructions\n  4. category\n  5. rating\n  6. exit\n")
                while True:
                    ch = input("Enter field number to edit: ")
                    if not ch.isalpha() and (int(ch)>=1 and int(ch)<=6):
                        break
                    else:
                        print("\nEnter a choice between 1-6! ")
                        print("Available fields to edit:\n  1. name\n  2. ingredients\n  3. instructions\n  4. category\n  5. rating\n  6. exit\n")
                if ch!='6':
                    new_data = input("Enter info to edit: ")
                    self.editRecipe(int(name),int(ch),new_data)
                    while True:
                        choice = input("Enter your choice: ")
                        if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                            break
                        else:
                            print("Enter a response from the available choices! ")
                else:
                    while True:
                        choice = input("Enter your choice: ")
                        if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                            break
                        else:
                            print("Enter a response from the available choices! ")
            if int(choice) == 5:
                name = input("\nEnter file name to be saved as: ")
                self.exportRecipe(name)
                while True:
                    choice = input("Enter your choice: ")
                    if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                        break
                    else:
                        print("Enter a response from the available choices! ")
            if int(choice) == 6:
                name = input("\nEnter file name to import recipes: ")
                self.importRecipe(name)
                while True:
                    choice = input("Enter your choice: ")
                    if not choice.isalpha() and choice!="" and (int(choice)>=1 and int(choice)<=7):
                        break
                    else:
                        print("Enter a response from the available choices! ")
            if int(choice) == 7:
                self.exitRecipe()
           
            
    def exitRecipe(self):
        sys.exit(0)

r = RMS()
#r.askUserOptions()