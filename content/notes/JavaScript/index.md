# JavaScript

A popular language that I don't really care about.

## Basics

Typing Convention: camelCase

Printing: `console.log('string');`
To print/interpolate a variable use `'${variable}'` NOTICE THE \`

Commenting: `//text` OR multiple lines `/* text */`
Variable Declaration:
`let variable = content`
`var` is similar to `let` but only in block scope. legacy code. Don't use `var`.
**Mutable: can reassign variable**
`const variable = content`
**Immutable: Cannot reassign variable**
Length: `variable.length`
All number types are just `number`
Null: `null`

## Logical Operators

And: `&&`
Or: `||`
Not: `!`
Loose Equal: `==` This will compare value `5 == '5' => true`
Strict Equal: `===` This will compare value AND type `5 === '5' => false`

# If/Else/

```js
if (condition) {

} else if {

} else {

}
```

**Ternary**
Combines if else into 1 line
`let variable_name = condition ? True : False`

## Switch/Match Case

```js
def matchThis(word) ={
	switch(word){
		case 'hello':
			//do something
			break
		case 'world':
		case '!!!!':
			//do something
			break
		default:
			console.log(word)
	}
}

```

If you don't break in a case, it will "fall through". So if the word matches case 2, it will go to case 3 and then exit out.

## Functions

```js
function variable(parameter) {
  stuff;
  return result;
}
```

Can't return more than 1 result at a time unlike python
Functions can be used as '**callback**'. Meaning you can do
`functionName1(functionName2)`
Most of the time, you shouldn't nee to use a callback function. Keep it simple.
Usually API/librarys are the one that needs this.
Fat arrow/arrow function

```js
const add = (x, y) => {
  return x + y;
};
```

Needs to be declared as a variable.
Can be more intuitive object scoping.

## Scope

## Arrays

Don't need to be the same type in an array
`const list = []`
`.push()` to put something to the back of the list
`.length`
`.concat()` or "spread" syntax: `[...arrayVariable, 2,3,4]` to combine 2 arrays

- `[...array1, ...array2]`

`.includes('word')`
`.slice(indexStart, indexEnd)`

## For loops

`for (init; condition; post)`
This will print from 0 - 99
`break` will break out of a loop
`continue` can break out of single iter early
`for (let element of array)`

## Objects

```js
const person = {
  name: {
    first: context,
    last: context,
  },
  age: number,
};
```

To access the first name. `person.name.first`
if you don't know how to access something or if it's not there. `person.name?.first`
Will check if there's a name variable. This helps to not throw an error if you reach into it wrong.
Object Method

```js
const person = {
	name: {
		first: context,
		last: context
	},
	age: number
	getfirstname(){
		return this.name.first
	}
	older(){
		this.age++
	}
}
```

`console.log(person.getfirstname())`
Methods can mutate the objects. `person.older()` will increment age by 1.
Can use string as keys
`person.name['first']` this helps finding stuff more dynamic. we can use this to be an input

## Error

```js
try {
	stuff
} catch (err) {
	stuff
} finally {
 stuff that will always run
}
```

`finally` is rarely used b/c if you wanted to run something just put it after the try catch block. Use if you want to do something dangerous with error object.

```js
function (){
	does something
	throw new Error('string')
}
```

When someone calls a function and the function doesn't work. It should throw an error at the user.
`Error` is an object.
Two properties: `name` and `properties`
`message`

## Runtime Environment

There are many different runtime environments.
Originally it used to be on the browser only.
Now Node.js, Deno.js, Bun can all run js.
Node Version Manager allows you to have different versions of Node. Easy to manage based on projects that require different version/update version.
