# SQL Basics

## Create table

```
CREATE TABLE table_name (
	variable_name TYPE CONSTRAINT
);
```

Types can be `NUll | INTEGER | REAL | TEXT | BLOB | BOOLEAN`
`Real` are floating int
`BLOB` are media links
Contraints can be `NOT NULL | UNIQUE | PRIMARY KEY`
`NOT NULL` Won't accept values that is NULL
`UNIQUE` Will not allow dupeplicate data in the column. Can be NULL
`PRIMARY KEY` Will automatically generate somethign if left empty. Can not be NULL

## Reference/Foreign key

Foreign key will reference to another table's primary key. This makes table relational

```
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL
);
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    CONSTRAINT fk_departments
    FOREIGN KEY (department_id)
    REFERENCES departments(id)
);
```

## Insert Data

```
INSERT INTO table (param1, param2, ...)
VALUES (arg1, arg2, ...);
```

- However, most of the time we will use a library in another programing language.

## Alter/Change data

```
ALTER TABLE table_name
	RENAME TO table_name;
	RENAME COLUMN column_name TO new_column_name;
	ADD COLUMN column_name TYPE;
	DROP COLUMN column_name TYPE;
```

## Delete Data

```
DELETE FROM table WHERE variable = x
```

# Aggregation

Single value combing serval other values

```
count
	DISTINCT (UNIQUE col)
sum (col)
min/max (col)
avg (col)
round (value, presicion)
```

`DISTINCT` Will remove duplicates
`round(value, precision)` if precision is left blank, it will round to whole number

- `round(value, 1)` will return value.1st decimal

## Query

```
SELECT what_you_want
FROM table_name
WHERE variable_name CONDITIONS
	LIKE 'name%' '%name'  '%name%'  '_ame'
	IN ('name1', 'name2', '...')
AND condition
OR condition
GROUP BY variable
HAVING condition
ORDER BY variable
LIMIT number_of_rows_you_want
```

`LIKE` is a condition
Can use with % or \_ wildcard operator:

-     `'name%''`: will check if variable starts with name
-     `'%name'`: will check if variable ends with name
-     `'%name%'`: will check if variable contains the name
-     `'_ame'`: will fill in the blank for you
      -		_oot => can be foot, boot, toot, coot
  `IN` is also a condition
- Will exactly match with the names provided
- Can also be used to do a subquery

`ORDER BY`: ASC: ascending will be default. DESC: descending
Has to come before LIMIT
`Having` : if we need to filter more after GROUP BY. Thus use after GROUP BY. Kinda like WHERE but not on raw data

## Subquery/Nested query

```
SELECT variable1
FROM table1
WHERE variable1 IN (
	SELECT variable2
	FROM table2
	WHERE table2_variable CONDITION
);
```

## IIF/Ternary/IF ELSE

```
SELECT *,
IIF (CONDITION, TRUE, FALSE) AS appended_new_column_name
FROM table;
```

# Different type of table schemas

One to One
One to Many
Many to Many tables

- Many different people can have multiple banks but they should have different bank info

```
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  username TEXT UNIQUE,
  password TEXT NOT NULL,
  is_admin BOOLEAN
);
CREATE TABLE banks (
  id INTEGER PRIMARY KEY,
  name TEXT,
  routing_number INTEGER UNIQUE
);
CREATE TABLE users_banks (
  user_id INTEGER,
  bank_id INTEGER,
  UNIQUE (user_id, bank_id)
);
```

`UNIQUE (user_id, bank_id)` is a primary key made of 2 columns

# Normalized Databases

From least to most normalized

-     1NF: 1st normal form
  -     Each row must be unique (no dupe data/primary key)
  -     Cell cannot be nested
-     2NF: 2nd normal form
  -     All columns that are not part of the primary key are dependent on the entire primary key, and not just one of the columns in the primary key
-     3NF: 3rd normal form
  -     All columns that aren't part of the primary are dependent solely on the primary key
-     BCNF: Boyce-Codd normal form
  -     A column that's part of a primary key can not be entirely dependent on a column that's not part of that primary key

ALWAYS CREATE 1NF DB's.
De-normalize DB if speed issue.

# Joins

This is like what set intersects what
`INNER JOIN | LEFT JOIN | RIGHT JOIN | FULL JOIN `

- SQLite doesn't support RIGHT and FULL JOINS but basically the same as LEFT JOIN but swap the variables around

```
SELECT columns_you_want
FROM table1
JOIN table2 ON table1.column = table2.column
```

# Performance/Indexing

`CREATE INDEX column_name_idx on table_name (column_name);`
common naming scheme: column_name_idx

- Add index to columns where there will be freq look up. Because each index = 1 binary tree. Every data insert will make a new binary tree PER INDEX resulting in slower write speeds.

## Multiple column index

`CREATE INDEX col1_col2_etc_idx ON table(col1, col2, etc);`

- If you query on first col, it'll be almost the same performance vs single index'ed columns, the more you add the more degraded the performance. Do this for only freq look up combinations.

# SQL INJECTION

- Use modern librarys to sanitize data otherwise you might pass raw strings that can ruin your db/give records to hackers.
  ie: user = asd); DROP TABLE kekw
