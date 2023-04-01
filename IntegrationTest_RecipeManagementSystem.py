import unittest
from unittest.mock import patch
import io, sys, os, json
import RecipeManagementSystem 

class TestRMSIntegration(unittest.TestCase):
    def test_add_view_recipe(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("Chicken Curry", "chicken, curry paste, coconut milk, vegetables", "1. Heat oil in a pot. 2. Add curry paste and fry for 1 minute. 3. Add chicken and fry until browned. 4. Add coconut milk and simmer for 20 minutes. 5. Add vegetables and simmer for another 10 minutes.", "Curry", 4)
        management.addRecipe(recipe1)
        captured_output = io.StringIO()          
        sys.stdout = captured_output             
        management.viewRecipe(1)                   
        sys.stdout = sys.__stdout__              
        expected_output = "\nRecipe Name: Chicken Curry\nIngredients Required: chicken, curry paste, coconut milk, vegetables\nInstructions: 1. Heat oil in a pot. 2. Add curry paste and fry for 1 minute. 3. Add chicken and fry until browned. 4. Add coconut milk and simmer for 20 minutes. 5. Add vegetables and simmer for another 10 minutes.\nCategory: Curry\nRating: 4\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
    

    def test_add_delete_recipe(self):
        management = RecipeManagementSystem.RMS()
        recipe2 = RecipeManagementSystem.Recipe("Lasagna", "pasta, meat, tomato sauce, cheese", "1. Cook pasta. 2. Brown meat. 3. Add tomato sauce. 4. Layer pasta, meat sauce, and cheese. 5. Bake in oven for 30 minutes.", "Italian", 5)
        management.addRecipe(recipe2)
        management.deleteRecipe(1)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        management.viewRecipe(1)
        sys.stdout = sys.__stdout__
        expected_output = "No recipes available to view\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()