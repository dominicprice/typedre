# typedre

Typesafe regex matching for Python

## Installation

`typedre` can be installed from PyPi with `pip install typedre`, and then becomes available in your project with `import typedre`.

## Usage

`typedre` allows you to build regexes where the matching groups are converted into Python types. A simple motivating example might be something like this, which is intended to match a colour specification:

```
import re

rgb_re = re.compile(r"rgb\((\d+),(\d+),(\d+)\)")

if m := rgb_re.match("rgb(100, 50, 75)"):
    r = int(m[1])
	g = int(m[2])
	b = int(m[3])
```

Using `typedre` this example becomes

```
from typedre import re

rgb_re = re("rgb\(").int("\d+").lit(",").int("\d+").lit(",").int("\d+").lit("\)")

if m := rgb_re.match("rgb(100, 50, 75)"):
	r, g, b = m
```
