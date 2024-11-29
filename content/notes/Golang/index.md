# Golang

It's mostly complete, but needs to be touched upon.

## Types

```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```

## Printing

```
import fmt

fmt.Printf("string")
fmt.Printf(variable)

%v -> value
%s -> string
%d -> int
%.2f -> float with 2 decimals
fmt.Sprintf("Hello %v", "world")
fmt.Sprintf("Hello %s", "world")
```

## Strongly typed

```
var first_name string = "Gary"
last_name := "Feng"

var age = 2.6
short_age := int(age)

//age = 24.6
//short_age = 24

const gender = "M"
```

Both are string, walrus `:=` will "infer" the type to assign the variable

## IF ELSE

```
if length1 < length2{
    asd
} else if length1 > length2{
    asd
} else {
    asd
}

if length := getLength(variable); length < 1 {
}
```

if you want to make a variable inside the scope

## Switch Case

```
func name(plan string) float64{
    switch plan{
    case "free":
        return 10.0
    case "pro":
        return 20.0
    default:
        return 30.0
    }
}
```

## blank identifier

`_` can discard a return value  
`x, _ := getXY()`  
So if a function returns 2 values like `getXY()` but we only care about the x, we can use `_` to discard the value.

## Named return

```
func getName()(first String, last String){
    //first and last are intialized with no values
    return //will return first and last if left blank
}
```

## Struct

Go doesn't have inheriance or classes, but struct's sort of allows data only inheriance

```
type car struct {
    model string
    speed int
    name string
    color string
    cost float64
}

func (myCar car) isCar() bool{
    //check if myCar is a valid car
    return true or false
}

fmt.Println(myCar.isCar())
//true or false
```

Memory layout matters

```
type stats struct {
    Reach    uint16
    NumPosts uint8
    NumLikes uint8
}
```

![b7604073197af25f77e411a6daf35aed.png](:/afb8eaeab1de470f8eee0074ca9f77b4)  
Notice how it's 16 then 8 then 8. if the memory is 8 then 16 then 8. It will add padding which will waste memory space.  
![f7fb5aa446ab886a231c2fda12441add.png](:/f777faa76179486486b181d2b8f64d9c)  
[reflect package](https://pkg.go.dev/reflect) can help debug [memory layout](https://go101.org/article/memory-layout.html)

`empty := struct{}{}`  
this is an empty struct.

```
type emptyStruct struct{}
empty := emptyStruct{}
```

this is a named empty struct.  
They are used as unary values. Both of these take 0 bytes.  
Example of a function for a structure.

```
func (myUser User) SendMessage (message string, messageLength int) (string, bool) {
    if messageLength <= myUser.Membership.MessageCharLimit {
        return message, true
    }
    return "", false
}
```

Send message is the method for User struct. It takes in message and messageLength as the parameter and returns a string and boolean. An example of using this method is

```
Bob := User{
	//stuff
}
Bob.SendMessage("Hello World", 11)
```

\> > RE ORGANIZE THIS < <

## Interface

A collection of method signatures.

```
map[string]any
```

# Variadic

```
import package

func sum(nums ...int) int{
	sum := 0
	for i := 0; i < len(nums); i++{
		sum += nums[i]
	}
	return sum
}
```

Notice the `...` before int. It takes an abirtary number of final arguments.

```
// func make([]T, len, cap) []T
mySlice := make([]int, 5, 10)
```

# Append

```
i := make([]int, 3, 8)
fmt.Println("len of i:", len(i))
// len of i: 3
fmt.Println("cap of i:", cap(i))
// cap of i: 8
fmt.Println("appending 4 to j from i")
// appending 4 to j from i
j := append(i, 4)
fmt.Println("j:", j)
// j: [0 0 0 4]
fmt.Println("addr of j:", &j[0])
// addr of j: 0x454000
fmt.Println("appending 5 to g from i")
// appending 5 to g from i
g := append(i, 5)
fmt.Println("addr of g:", &g[0])
// addr of g: 0x454000
fmt.Println("i:", i)
// i: [0 0 0]
fmt.Println("j:", j)
// j: [0 0 0 5]
fmt.Println("g:", g)
// g: [0 0 0 5]
```

# Slices (Arrays)

`var myInts[10]`
slice of size 10
`primes := [6]int{1,2,3,4,5,6}`
slices
`primes[1:4]`

# Loops

`for i := 0; i < len(something); i++{
}`

`for i, ele := range slice{
}`

# Maps

to make a map in go, need to use make method
`dict := make(map[string]int)`
this is a map of key string to int value.

# Pointers

Uses `*` and `&`

# Channels

Channel creation
`ch <- make(chan int, len(size))`
Sending to channel
`ch <- 5`
Receiving from channel
`x := <-ch`
Close channel
`close(ch)` / `defer close(ch)`
Check if closed
`if value, ok := <-ch; !ok{
	fmt.Println("ch closed")
}`
if sending data to closed channel. It will panic. Reciving from closed channel will result in 0.
Type safety
Read only`func name(chan <-chan string)`
Write only `func name(chan chan<- string`
Select statement

```
select{
case:
default:
}
```

Code snippet

```
import "time"

func processMessages(messages []string) []string {
	ch := make(chan string, len(messages))
	for _, message := range messages{
		go func(msg string){
			ch <- process(msg)
		}(message)
	}
	processedMsgs := make([]string, len(messages))
	for i := 0; i < len(messages); i++{
		processedMsgs[i] = <-ch
	}
	return processedMsgs
}

func process(message string) string {
	time.Sleep(1 * time.Second)
	return message + "-processed"
}
```

# Mutexes

# Generics

```
func last[T any](s []T) T {
	if len(s) == 0 {
		var zero T
		return zero
	}
	return s[len(s)-1]
}
```

T is the generic variable name. any allows it to be a generic
in order for there to be a 0 generic.

## Constraints

If you want only certain generics/types then you can make an interface

```
type numbers interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64 |
        ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
        ~float32 | ~float64 |
}

func doMath[T numbers](vals []T) T {
	//do something and return a T type
}
```

# Enum

# HTTPS

## JSON

```
type Item struct{
	Id 					string `json:"id"`
	Name			 string `json:"name"`
	ItemLevel int		 `json:"item_level"`
}


func getJSONtoGoStruct(url string) ([]Item, error){
	res, res_err := http.Get(url)
	defer res.Body.Close() //to prevent mem issue
	var items []Items


	decoder := json.NewDecoder(res.Body)
	err := decoder.Decode(&items)
------------------------------------OR----------------------------------------
	data []byte, err := io.ReadAll(res.Body)
	json.Unmarshal(data, &items)

	return items
}
```

Makes a GET request and turns the result into a Go struct

`data, err := json.Marshal(items)`
Turns a go struct into a `[]bytes`

## CRUD

```
func createPostReq(url, apiKey string, user User)(User, err){
	jsonData, err := json.Marshal(data)
	//err  check

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	//err check

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("X-API-Key", apiKey)

	client := &http.Client{}
	res, err := client.Do(req)
	//err check

	defer res.Body.Close()

	var newUser User
	decoder := json.NewDecoder(res.Body)
	err = decoder.Decode(&newUser)
	//err check

	return data, nil
}
```

`http:NewRequest("GET/POST/PUT/DELETE", url, nil/bytes.NewBuffer(jsonData))`

```
brew install postgresql@16
brew services start postgresql
/opt/homebrew/opt/postgresql@16/bin/psql --version
echo 'export PATH="/opt/homebrew/opt/postgresql@16/bin:$PATH"' >> ~/.zshrc
psql --version

brew services start postgresql@16
psql postgres
CREATE DATABASE gator;
\c gator
SELECT version();
```
