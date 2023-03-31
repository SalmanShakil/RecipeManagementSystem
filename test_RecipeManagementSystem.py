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