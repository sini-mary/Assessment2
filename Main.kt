fun main() {
    val artist1 = Musician("Femi Kuti", "Nigeria", "Saxophone")
    val artist2 = Musician("Angelique Kidjo", "Benin", "Vocals")
    val artist3 = Artist("Ndeye Gueye", "Senegal")

    val musicPerformance1 = MusicPerformance("18:00", "19:30", artist1, "Afrobeat")
    val musicPerformance2 = MusicPerformance("20:00", "21:30", artist2, "World Music")
    val dancePerformance = DancePerformance("22:00", "23:30", artist3, "Traditional Senegalese Dance")

    val stage1 = Stage("Main Stage", 1000)
    stage1.addPerformance(musicPerformance1)
    stage1.addPerformance(musicPerformance2)
    stage1.addPerformance(dancePerformance)

    stage1.startPerformances()


    val product1 = Product("Shirt", 15.99, 3)
    val product2 = Product("Shoes", 4.99, 9)
    val product3 = Product("Jeans", 3.99, 55)

    val totalValue1 = product1.calculate()
    val totalValue2 = product2.calculate()
    val totalValue3 = product3.calculate()

    println("Total value of ${product1.name}: $totalValue1")
    println("Total value of ${product2.name}: $totalValue2")
    println("Total value of ${product3.name}: $totalValue3")

}
//**African Music Festival:** You're in charge of organizing a Pan-African music
//festival. Many artists from different countries, each with their own musical style
//and instruments, are scheduled to perform. You need to write a program to
//manage the festival lineup, schedule, and stage arrangements. Think about how
//you might model the `Artist`, `Performance`, and `Stage` classes, and consider
//how you might use inheritance if there are different types of performances or
//stages.

//class to manage the lineup,Artist,will have name and string,
//,musician will have , name string and instrument they will inherit from Artist

//  class pefomance will be an abstract class, and it will have an abstract function,
//class Music perfomance will have  start time, endtime and the artists, genre and inherit from the abstract class perfom
//class stage will have the capaciity.


open class Artist(val name: String, val country: String)

class Musician(name: String, country: String, val instrument: String) : Artist(name, country)

abstract class Performance(val startTime: String, val endTime: String) {
    abstract fun perform()


}

class MusicPerformance(startTime: String, endTime: String, val artist: Musician, val genre: String) : Performance(startTime, endTime) {
    override fun perform() {
        println("${artist.name} is performing $genre music from ${artist.country} on ${artist.instrument}.")
    }
}

class DancePerformance(startTime: String, endTime: String, val artist: Artist, val style: String) : Performance(startTime, endTime) {
    override fun perform() {
        println("${artist.name} is performing $style dance from ${artist.country}.")
    }
}

class Stage(val name: String, val capacity: Int) {
    private val performances: MutableList<Performance> = mutableListOf()

    fun addPerformance(performance: Performance) {
        performances.add(performance)
    }

    fun startPerformances() {
        println("Performances on $name:")
        performances.forEach { performance ->
            println("Start time: ${performance.startTime}, End time: ${performance.endTime}")
            performance.perform()
        }
    }
}

//Create a class called Product with attributes for name, price, and quantity.
//Implement a method to calculate the total value of the product (price * quantity).
//Create multiple objects of the Product class and calculate their total values.

class Product(val name: String, val price: Double, val quantity: Int) {
    fun calculate(): Double {
        return price * quantity
    }
}


