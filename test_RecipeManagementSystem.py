import unittest
import RecipeManagementSystem

class TestRMS(unittest.TestCase):
    def test_addRecipe(self):      
        management = RecipeManagementSystem.RMS()    
        recipe = RecipeManagementSystem.Recipe("soup", "tomato, tomato paste, water, spices", "boil all ingredients together and leave for 30 minutes", "appetizer", 5)
        management.addRecipe(recipe)
        addedRecipe = {'id': 1, 'name': 'soup', 'ingredients': 'tomato, tomato paste, water, spices', 'instructions': 'boil all ingredients together and leave for 30 minutes', 'category': 'appetizer', 'rating': 5}
        self.assertIn(addedRecipe, management.recipes)