import unittest
import RecipeManagementSystem

class TestRMS(unittest.TestCase):
    def test_addRecipe(self):      
        management = RecipeManagementSystem.RMS()    
        recipe = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        management.addRecipe(recipe)
        addedRecipe = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        self.assertIn(addedRecipe, management.recipes)
    

    def test_viewRecipe(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        recipe2 = RecipeManagementSystem.Recipe("pizza", "chicken, ranch sauce, mushrooms", "bake for 30 minutes", "main", 5)         
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)
        management.viewRecipe(2)
        self.assertEqual([management.recipes[0]['id'],management.recipes[0]['name']],[1,'soup'])
        self.assertEqual([management.recipes[1]['id'],management.recipes[1]['name']],[2,'pizza'])
    

    def test_deleteRecipe(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        recipe2 = RecipeManagementSystem.Recipe("pizza", "chicken, ranch sauce, mushrooms", "bake for 30 minutes", "main", 5)         
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)
        management.deleteRecipe(1)
        addedRecipe = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        self.assertNotIn(addedRecipe, management.recipes)
    

    def test_editRecipe(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        recipe2 = RecipeManagementSystem.Recipe("pizza", "chicken, ranch sauce, mushrooms", "bake for 30 minutes", "main", 5)         
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)
        management.editRecipe(2,1,"Pasta")
        management.editRecipe(1,1,"Tomato Soup")
        addedRecipe = {'id': 2, 'name': 'Pasta', 'ingredients': 'chicken, ranch sauce, mushrooms', 'instructions': 'bake for 30 minutes', 'category': 'main', 'rating': 5}
        addedRecipe1 = {'id': 1, 'name': 'Tomato Soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        self.assertIn(addedRecipe, management.recipes)
        self.assertIn(addedRecipe1, management.recipes)
    

    def test_exportRecipe(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        recipe2 = RecipeManagementSystem.Recipe("pizza", "chicken, ranch sauce, mushrooms", "bake for 30 minutes", "main", 5)         
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)
        management.exportRecipe("SOUP AND PIZZA")
    

    def test_importRecipe(self):
        management = RecipeManagementSystem.RMS()
        management.importRecipe("SOUP AND PIZZA")
        addedRecipe = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        addedRecipe1 = {'id': 2, 'name': 'pizza', 'ingredients': 'chicken, ranch sauce, mushrooms', 'instructions': 'bake for 30 minutes', 'category': 'main', 'rating': 5}
        self.assertIn(addedRecipe, management.recipes)
        self.assertIn(addedRecipe1, management.recipes)
    

    def test_addRecipe_1(self):      
        management = RecipeManagementSystem.RMS()    
        recipe = RecipeManagementSystem.Recipe("", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        recipe1 = RecipeManagementSystem.Recipe(-1, "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        management.addRecipe(recipe)
        management.addRecipe(recipe1)
        addedRecipe = {'id': 1, 'name': '', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        addedRecipe1 = {'id': 1, 'name': -1, 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        self.assertNotIn(addedRecipe, management.recipes)
        self.assertNotIn(addedRecipe1, management.recipes)
    

    def test_addRecipe_2(self):
        management = RecipeManagementSystem.RMS()    
        recipe1 = RecipeManagementSystem.Recipe("soup", "", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        management.addRecipe(recipe1)
        addedRecipe1 = {'id': 1, 'name': 'soup', 'ingredients': '', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        self.assertNotIn(addedRecipe1, management.recipes)
    

    def test_addRecipe_3(self):
        management = RecipeManagementSystem.RMS()    
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "", "appetizer", 5)
        management.addRecipe(recipe1)
        addedRecipe1 = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': '', 'category': 'appetizer', 'rating': 5}
        self.assertNotIn(addedRecipe1, management.recipes)
    

    def test_addRecipe_4(self):
        management = RecipeManagementSystem.RMS()    
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", 23, 5)
        recipe2 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "", 5)
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)
        addedRecipe1 = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 23, 'rating': 5}
        addedRecipe2 = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': '', 'rating': 5}
        self.assertNotIn(addedRecipe1, management.recipes)
        self.assertNotIn(addedRecipe2, management.recipes)
    

    def test_addRecipe_5(self):
        management = RecipeManagementSystem.RMS()    
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", "good")
        recipe2 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", "")
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)
        addedRecipe1 = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': '', 'category': 'appetizer', 'rating': 'good'}
        addedRecipe2 = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': '', 'category': 'appetizer', 'rating': ''}
        self.assertNotIn(addedRecipe1, management.recipes)
        self.assertNotIn(addedRecipe2, management.recipes)
    

    def test_viewRecipe_1(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        recipe2 = RecipeManagementSystem.Recipe("pizza", "chicken, ranch sauce, mushrooms", "bake for 30 minutes", "main", 5)         
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)       
        management.viewRecipe(3)
    

    def test_deleteRecipe_1(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        recipe2 = RecipeManagementSystem.Recipe("pizza", "chicken, ranch sauce, mushrooms", "bake for 30 minutes", "main", 5)         
        management.addRecipe(recipe1)
        management.addRecipe(recipe2)
        management.deleteRecipe(3)