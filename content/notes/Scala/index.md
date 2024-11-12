# Scala

These notes are incomplete because it was mostly for a project. This lanaguage is pretty aesticially pleasing.

## Basics

```
import scala.io.StdIn.readLine

println("Hello World")
val firstname: String = readLine()
val lastname: String = readLine()
println(s"Name: $firstname $lastname")
println(s"do math via {2+2} = 4")
```

## Types

```
Int | Long | Short | Double | Float
BigInt | BigDecimal
String
Byte
```

## OOP

```
trait Speaker:
	def speak(): String

class Dog(name: String) extends Speaker:
	def speak(): String = "Woof!"
```
