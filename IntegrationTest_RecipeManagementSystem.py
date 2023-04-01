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
    

    def test_add_edit_recipe(self):
        management = RecipeManagementSystem.RMS()
        recipe3 = RecipeManagementSystem.Recipe("Pesto Pasta", "pasta, pesto sauce, cherry tomatoes, parmesan cheese", "1. Cook pasta. 2. Add pesto sauce. 3. Add cherry tomatoes. 4. Top with parmesan cheese.", "Italian", 4)
        management.addRecipe(recipe3)
        management.editRecipe(1, 1, "Spaghetti with Pesto")   
        captured_output = io.StringIO()
        sys.stdout = captured_output
        management.viewRecipe(1)       
        sys.stdout = sys.__stdout__
        expected_output = "\nRecipe Name: Spaghetti with Pesto\nIngredients Required: pasta, pesto sauce, cherry tomatoes, parmesan cheese\nInstructions: 1. Cook pasta. 2. Add pesto sauce. 3. Add cherry tomatoes. 4. Top with parmesan cheese.\nCategory: Italian\nRating: 4\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
    

    def test_all_features_with_wrongvalues(self):
        management = RecipeManagementSystem.RMS()
        recipe1 = RecipeManagementSystem.Recipe("Spaghetti Bolognese", "spaghetti, minced beef, canned tomatoes, onion, garlic, olive oil, salt, pepper", "1. Cook spaghetti according to package instructions. 2. In a pan, heat olive oil and sauté garlic and onion. 3. Add minced beef and cook until browned. 4. Add canned tomatoes and let simmer for 10 minutes. 5. Season with salt and pepper. 6. Serve over cooked spaghetti.", "Pasta", 4)
        management.addRecipe(recipe1)
        addedRecipe = {'id': 1, 'name': 'Spaghetti Bolognese', 'ingredients': 'spaghetti, minced beef, canned tomatoes, onion, garlic, olive oil, salt, pepper', 'instructions': '1. Cook spaghetti according to package instructions. 2. In a pan, heat olive oil and sauté garlic and onion. 3. Add minced beef and cook until browned. 4. Add canned tomatoes and let simmer for 10 minutes. 5. Season with salt and pepper. 6. Serve over cooked spaghetti.', 'category': 'Pasta', 'rating': 4}
        self.assertIn(addedRecipe, management.recipes)
        # add recipes with invalid input
        recipe2 = RecipeManagementSystem.Recipe(12345, "potatoes, carrots, onion, garlic, olive oil, salt, pepper", "1. Preheat oven to 200C. 2. Cut vegetables into bite-sized pieces. 3. Toss vegetables in olive oil and season with salt and pepper. 4. Roast for 30-40 minutes or until tender.", "Vegetarian", 3)
        management.addRecipe(recipe2)
        addedRecipe = {'id': 2, 'name': 12345, 'ingredients': 'potatoes, carrots, onion, garlic, olive oil, salt, pepper', 'instructions': '1. Preheat oven to 200C. 2. Cut vegetables into bite-sized pieces. 3. Toss vegetables in olive oil and season with salt and pepper. 4. Roast for 30-40 minutes or until tender.', 'category': 'Vegetarian', 'rating': 3}
        self.assertNotIn(addedRecipe, management.recipes)
        recipe3 = RecipeManagementSystem.Recipe("Fried Rice", 12345, "1. Cook rice according to package instructions. 2. In a pan, heat oil and sauté garlic and onion. 3. Add cooked rice and stir-fry for 2-3 minutes. 4. Add vegetables and protein of your choice. 5. Season with salt and pepper.", "Asian", 4)
        management.addRecipe(recipe3)
        recipe4 = RecipeManagementSystem.Recipe("Grilled Chicken", "chicken breasts, lemon, garlic, olive oil, salt, pepper", 12345, "Meat", 5)
        management.addRecipe(recipe4)  
        recipe5 = RecipeManagementSystem.Recipe("Caesar Salad", "romaine lettuce, croutons, Parmesan cheese, Caesar dressing", "1. Wash and chop lettuce. 2. Add croutons and Parmesan cheese. 3. Toss with Caesar dressing.", 12345, 4)
        management.addRecipe(recipe5)     
        recipe6 = RecipeManagementSystem.Recipe("Chocolate Cake", "flour, sugar, cocoa powder, baking soda, baking powder, salt, eggs, milk, oil, vanilla extract, hot water", "1. Preheat oven to 350F. 2. Mix dry ingredients in a bowl. 3. Add wet ingredients and mix until smooth. 4. Grease a cake pan and pour in batter. 5. Bake for 30-35 minutes. 6. Let cool before frosting with your choice of frosting.", "Dessert", "five stars")
        management.addRecipe(recipe6)
        # view a recipe that does not exist
        management.viewRecipe(10)
        # view a recipe that exists
        management.viewRecipe(1)
        # delete a recipe that does not exist
        management.deleteRecipe(10)
        # delete a recipe that exists
        management.deleteRecipe(1)
        # edit a recipe that does not exist
        management.editRecipe(10, 1, "Spaghetti Carbonara")

if __name__ == '__main__':
    unittest.main()