# C

WIP

## Main

```
int main(){
	return 0;
}
```

## Variables

```
int var
float var
char var
char *var
```

## Print

```
#include <stdio.h>
printf("string goes here\n %d %s %c %f", int, char *, char, float)
```

Need \n

## Operations

```
+ // addition
- // subtraction
* // multiplication
/ // division
% // modulus (remainder)
++ // increment
-- // decrement
--
== // equal to
!= // not equal to
> // greater than
< // less than
>= // greater than or equal to
<= // less than or equal to
--
&& // logical AND
|| // logical OR
! // logical NOT
--
& // bitwise AND
| // bitwise OR
^ // bitwise XOR
~ // bitwise NOT
<< // left shift
>> // right shift
--
= // simple assignment
+= // add and assign
-= // subtract and assign
*= // multiply and assign
/= // divide and assign
%= // modulus and assign
&= // bitwise AND and assign
|= // bitwise OR and assign
^= // bitwise XOR and assign
<<= // left shift and assign
>>= // right shift and assign
--
& // address-of operator
* // dereference operator
-> // structure pointer operator
. // structure member operator
?: // ternary operator
sizeof // size operator
```

## Loops

```
while (condition){
    //do something
}
    //do something
do {
    //do something
} while (condition);
```

Do while loops are usually common in C macros. It will always run once.

## Pointers

`*` = points to a variable

& = address of variable

## Structs

```
struct Coord = {
	int x;
	int y;
	int z;
};
typedef struct Coord {
	int x;
	int y;
	int z;
} coord_t;
struct Coord new_coord = {.x = 1, .y = 2, .z = 3};
coord_t new_coord = {.x = 1, .y = 2, .z = 3};
```

## Forward declaration

If you want to have a child parent struct, you will need to declare it otherwise compiler won't like it.

```
typedef struct Employee employee_t;
typedef struct Department department_t;
typedef struct Employee {
  int id;
  char *name;
  department_t *department;
} employee_t;
typedef struct Department {
  char *name;
  employee_t *manager;
} department_t;
```

## ENUM

```
typedef enum Color {
	RED,
	ORANGE,
	YELLOW,
	GREEN,
	BLUE,
	INDIGO,
	VIOLET,
} color_t
switch (color){
	case RED:
		break;
	default:
		break;
}
```

## UNIONS

```
typedef union PacketHeader{
  struct {
    uint16_t src_port;
    uint16_t dest_port;
    uint32_t seq_num;
  } tcp_header;
  uint8_t raw[8];
} packet_header_t;
```
