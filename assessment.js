class Story{
    constructor(storytitle, details, name, age_group,period){
        this.storytitle=storytitle;
        this.details=details;
        this.name=name;
        this.age_group=age_group;
        this.period=period
    }
    getSummary(this){
        return `Title is ${this.storytitle} length is ${this.period} the age group of this story is ${self.age_group}`

    }
    getContent(this){
     return `Content is ${this.details}`
}}

class StoryTeller{
    constructor(name, language){
        this.name=name
        this.language=language
    }
    tellStory(this,story){
        return `${this.name}  narrates ${story} in ${this.language}`

    }
    


}
class Translator extends StoryTeller{
    constructor(names , language, target_language){
        this.names=names;
        this.language=language;
        this.target_language=target_language;
    }
    translate(this,story){
       return `This ${this.name} translates ${story} to ${target_language}`

}}
// # # 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// # The app needs to handle recipes from different African countries, each with its
// # unique ingredients, preparation time, cooking method, and nutritional
// # information. Consider creating a `Recipe` class, and think about how you might
// # create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// # `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// # methods.


class Recipe{
    constructor(name, country, ingredients, preparation_time, cooking_method,nutritional_info )
    {
        this.name=name
        this.country=country
        this.ingredients=ingredients
        this.preparation_time=preparation_time
        this.cooking_method=cooking_method
        this.nutritional_info=nutritional_info
    }

     display_recipe(this){
           return(`Recipe: ${this.name}`
         `Country: ${this.country}, 
        Ingredients  ${this.ingredients},
        
        Preparation Time: ${this.preparation_time}
        Cooking Method: ${this.cooking_method},
        Nutritional Information: ${this.nutritional_info}`)

}}
console.log(display_recipe);

// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.

// main class is class species with, name diet and lifespan,and no method. the pther class is 
// class predator which inherits from the main class species 



class Species {
    constructor(name, diet, lifespan) {
      this.name = name;
      this.diet = diet;
      this.lifespan = lifespan;
    }
  }
  
  class Predator extends Species {
    constructor(name, diet, lifespan, huntingMethod) {
      super(name, diet, lifespan);
      this.huntingMethod = huntingMethod;
    }
  
    hunt() {
      console.log(`${this.name} is hunting using ${this.huntingMethod}.`);
    }
  }
  
  class Prey extends Species {
    constructor(name, diet, lifespan, habitat) {
      super(name, diet, lifespan);
      this.habitat = habitat;
    }
  
    escape() {
      console.log(`${this.name} is escaping from predators.`);
    }
  }
  
 
  const lion = new Predator("Lion", "Carnivore", 15, "Stalking and ambushing");
  lion.hunt();
  
  const zebra = new Prey("Zebra", "Herbivore", 20, "Grasslands");
  zebra.escape();

//   # Implement a class called Student with attributes for name, age, and grades (a
//     # list of integers). Include methods to calculate the average grade, display the
//     # student information, and determine if the student has passed (average grade >=
//     # 60). Create objects for the Student class and demonstrate the usage of these
//     # methods.
//     #  attributes are name age and grades, 
//     # implement a condition that checks in the students has passes or not
//     # create two instances of this class
//     # call their functions

class Student{
    constructor( name, age, grades){
        this.name = name;
        this.age = age;
        this.grades = grades;
    }
    calculate_average_grade(this){
        if(!this.grades){
            return 0
        }
            
         else{
    return ` ${this.grades} ${this.grades}`
            }
       display_student_info(this){
        console.log(`Name: ${self.name}
        "Age: ${self.age}",
        "Grades: ${', '.join({grade} =={grade} ==this.grades)}`)
       }
    has_passed(this){
        average_grade = self.calculate_average_grade()
        return average_grade >= 60
    }
    }

        student1 = new Student("John Smith", 18, [80, 75, 90, 85, 95])
student2 = Student("Jane Doe", 19, [70, 65, 80, 75, 55])
student3 = Student("Adam Johnson", 20, [])
Student.display_student_info()



  