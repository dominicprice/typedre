# typedre

Typesafe regex matching for Python

## Installation

`typedre` can be installed from PyPi with `pip install typedre`, and then becomes available in your project with `import typedre`.

## Usage

`typedre` allows you to build regexes where the matching groups are converted into Python types. A simple motivating example might be something like this, which is intended to match a colour specification:

```
from re import match

if m := match(r"rgb\((\d+),(\d+),(\d+)\)", "rgb(100, 50, 75)"):
    r = int(m[1])
	g = int(m[2])
	b = int(m[3])
```

Using `typedre` this example becomes

```
from typedre import match, c

rgb_re = re("rgb\(").int("\d+").lit(",").int("\d+").lit(",").int("\d+").lit("\)")

if m := match(r"rgb\((\d+),(\d+),(\d+)\)", "rgb(100, 50, 75)", c(int, int, int)):
	r, g, b = m.groups()
	# r, g, and b are already ints
	reveal_type(r) # int
	reveal_type(g) # int
	reveal_type(b) # int
```

The `c(int, int, int)` here specifies the types which the matched groups should be converted to. You can also define more complicated converters by using any function with the signature `str -> T` for some type `T`, e.g.

```
def named_number(s: str) -> int:
    names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	return names.index(s)
	
if m := match(r"I have (\d) items", "I have four items", c(named_number)):
    assert m[1] == 4 # passes
```

## Builder

You can also construct typed regexes using the chained builder class, for example

```
from typedre import new, c

pattern = new().alpha().lit(": #").hex(6).compile()
m = pattern.match("fg: #4a4a4a")
assert m is not None
assert m[1] == 0x4a4a4a

pattern = new("Name: ").str(r"[A-Z][a-z]+").compile()
m = pattern.match("Name: Joe")
assert m is not None
assert m[1] == "Joe"
```

The builder specifies the following methods:

| Method | Args | Description |
| === | === | === |
| `lit` | `pattern` | A non-capturing group |
| `str` | `pattern` | A capturing group of `str` type |
| `int` | `pattern` | A capturing group of `int` type |
| `val` | `pattern, converter` | A capturing group of type equal to the return value of `converter` |
| `float` | `allow_exp` | A capturing group for a floating point number |
| `dec` | `allow_sign` | A capturing group for a decimal integer |
| `hex` | `length` | A capturing group for a hexadecimal integer |
| `alpha` | `length` | A capturing group for a string of alpha characters |
| `alphanum` | `length` | A capturing group for a string of alphanumeric characters |
| `ws` | `required` | A non-capturing group for whitespace |
| `bool` | `true_values, false_values` | A capturing group for boolean values |

