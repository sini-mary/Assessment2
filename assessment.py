# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.


# sudo code 
#  App that records the stories
# in a database (story_table) with fields:
# method  Prints the title and content of the story
# Translates the story into the target language

class Story:
    def __init__(self, storytitle, details, length, age_group):
        self.storytitle =storytitle
        self.details = details
        self.length = length
        self.age_group = age_group
    
    def get_summary(self):
    
        return f"Title: {self.storytitle}\nLength: {self.length}\nAge Group: {self.age_group}"

    def get_content(self):
        return self.content


class StoryTeller:
    def __init__(self, name, language):
        self.name = name
        self.language = language
    
    def tell_story(self, story):
        print(f"{self.name} is telling a story in {self.language}:")
        print(story.get_content())


class Translator(StoryTeller):
    def __init__(self, name, language, target_language):
        super().__init__(name, language)
        self.target_language = target_language
    
    def translate_story(self, story):
        print(f"{self.name} is translating the story from {self.language} to {self.target_language}:")
        translated_content = Translator(story.get_content(), self.language, self.target_language)
        translated_story = Story(story.title, translated_content, story.length, story.age_group)
        print(translated_story.get_content())

        
    
# # 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# main class is class recipe ,   which has , name of the food, country, preparation time, cooking method and nutritional
# info
#methods are display recipes


class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_method, nutritional_info):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info
    
    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Country: {self.country}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"Preparation Time: {self.preparation_time}")
        print(f"Cooking Method: {self.cooking_method}")
        print(f"Nutritional Information: {self.nutritional_info}")


class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info,spice_level):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.spice_level = spice_level

    def display_recipe(self):
        super().display_recipe()
        print(f"Spice Level: {self.spice_level}")


class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, injera_required):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.injera_required = injera_required

    def display_recipe(self):
        super().display_recipe()
        print(f"Injera Required: {self.injera_required}")


class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, jollof_rice):
        super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method, nutritional_info)
        self.jollof_rice = jollof_rice

    def display_recipe(self):
        super().display_recipe()
        print(f"Jollof Rice: {self.jollof_rice}")


moroccan_recipe = MoroccanRecipe("Potatoes", ["Chicken", "Tomatoes", "Onions", "Spices"],
                                 "2 hours", "Braising", "Calories: 400", "Medium")


ethiopian_recipe = EthiopianRecipe("Hinjera", ["Chicken", "Berbere spice blend", 
                                               "Onions", "Garlic", "Ginger"], "2 hours", "Stewing", "Calories: 450", True)


nigerian = NigerianRecipe("Fried rice", ["Rice", "Tomatoes", "Pepper", "Onions",
                                                "Chicken"], "1 hour", "Simmering", "Calories: 500",
                                 True)
nigerian.display_recipe()

# // **Wildlife Preservation:** You're a wildlife conservationist working on a
# // program to track different species in a national park. Each species has its own
# // characteristics and behaviors, such as its diet, typical lifespan, migration
# // patterns, etc. Some species might be predators, others prey. You'll need to

# // create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# // these classes might relate to each other through inheritance.
# main class is class species 
class Species :
    def __init__( self,name, diet, lifespan) :
      self.name = name
      self.diet = diet
      self.lifespan = lifespan
    
  
  
class Predator (Species ):
    def __init__( self,name, diet, lifespan, huntingMethod) :
      pass
      self.huntingMethod = huntingMethod
    
  
    def hunt(self) :
      print (f"{self.name} is hunting using{self.huntingMethod}")
    
  
  
class Prey  (Species) :
    def __init__(self,name, diet, lifespan, habitat) :
      pass
      self.habitat = habitat
    
  
    def escape(self) :
      print(f"{self.name} is escaping from predators.")
    
  
  
 
cheetah =  Predator("Lion", "Carnivore", 15, "Stalking and ambushing")
cheetah.hunt()
  
zebra =  Prey("Zebra", "Herbivore", 20, "Grasslands")
zebra.escape()
# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
#  attributes are name age and grades, 
# implement a condition that checks in the students has passes or not
# create two instances of this class
# call their functions

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(str(grade) for grade in self.grades)}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60



student1 = Student("John Smith", 18, [80, 75, 90, 85, 95])
student2 = Student("Jane Doe", 19, [70, 65, 80, 75, 55])
student3 = Student("Adam Johnson", 20, [])

student1.display_student_info()
print(f"Avg Grade: {student1.calculate_average_grade()}")
print(f" Status: {'Passed' if student1.has_passed() else 'Failed'}")



student2.display_student_info()
print(f"Average Grade: {student2.calculate_average_grade()}")
print(f"Pass Status: {'Passed' if student2.has_passed() else 'Failed'}")


