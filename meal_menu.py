from bs4 import BeautifulSoup
import requests

class DailyMeal():
    def __init__(self):
        self.meal_options = {
            "Breakfast": "https://www.jamieoliver.com/recipes/category/course/breakfast/",
            "Healpthy soups": "https://www.jamieoliver.com/recipes/category/course/healthy-soup-recipes/",
            "Pasta": "https://www.jamieoliver.com/recipes/pasta-recipes/",
            "Chicken": "https://www.jamieoliver.com/recipes/chicken-recipes/",
            "Vegetables": "https://www.jamieoliver.com/recipes/vegetables-recipes/",
            "Fish": "https://www.jamieoliver.com/recipes/fish-recipes/",
            "Beef": "https://www.jamieoliver.com/recipes/beef-recipes/",
            "Eggs": "https://www.jamieoliver.com/recipes/eggs-recipes/",
            "Salads": "https://www.jamieoliver.com/search/?s=Salads",
            "Desserts": "https://www.jamieoliver.com/recipes/category/course/desserts/"
        }
        self.meal = 0
        self.recipe_title = 0
        self.selected_recipe = 0

    def choose_meal(self):
        print('Choose one of the following options:')
        index = 0
        for i in self.meal_options:
            print(index, ')', i)
            index += 1
        num = input('Enter number:')
        self.meal = list(self.meal_options.keys())[int(num)]

    def download_titles(self):
        url=self.meal_options[self.meal]
        req=requests.get(url)
        content=req.text
        if(content):
            self.recipe_title=BeautifulSoup(content, 'html.parser')
            self.recipe_title=self.recipe_title.findAll("div",class_="recipe-title")

    def show_options(self):
        self.download_titles()
        index = 0
        for i in self.recipe_title: 
            print(index, ') ', i.text)
            index += 1

    def choose_recipe(self):
        self.show_options()
        num = input('Enter number:')
        self.selected_recipe = list(self.recipe_title.keys())[int(num)]

    def exec(self):
        self.choose_meal()
        self.show_options()

def main():
    daily_meal = DailyMeal()
    daily_meal.exec()


if __name__ == "__main__":
    main()
