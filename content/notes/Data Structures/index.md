# Data Structures

## Stack

Last In First Out (LIFO)

push: add item to top of stack
pop: remove and return item from top of stack
peek: return item from top of stack
size: return the len of the stack

## Queue

First in First Out (FIFO)

push: add to tail of queue
pop: remove and return the oldest item (head)
peek: return the item in front of queue
size: return the len of the queue

## Linked List

Have a self.head and optionally a self.tail.
self.head.next refers to next node
if 1 node then self.head and self.tail is the same.

## Graph

Preorder traversal

- Append val to list
- Recusively go down left
- Recursively go down right
- return list

Postorder traversal

- recursively go down left
- recursively go down right
- append val to list
- return list

Inorder

- recursively go down left
- append val to list
- recurisvely go down right
- return list

## Trie

A dictionary made of nested objects. Can help find words

```
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
	"w": {
		"o": {
			"r":{
				"l":{
					"d":{
						"*": True
					}
				}
			}
			"w":{
				"*": True
			}
		}
	}
}
```

Can be used for autofills
