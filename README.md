# TimeUtils
> Helper functions for working with time.

TimeUtils is a collection of helper functions to work with time

## Installation
Clone the project inside your working directory.
You can install the package locally by running pip at the root level.
```sh
pip install /path/to/root/level
```
## Usage examples
Time conversion functions.
```py

from TimeUtils.utils import now_iso8601
from TimeUtils.utils import str2stamp
from TimeUtils.utils import stamp2str


# print current UTC time.
print('Current UTC: ', now_iso8601())

# convert time string
DATE = '2022-10-14 08:00:00'
converted = str2stamp(DATE)
print('Time string to timestamp: ', DATE, ' -> ', converted)

# converting back
print('Converting back: ', stamp2str(converted))


```

## Meta
Alessandro Visintin - alevise.public@gmail.com

Find me: [Twitter](https://twitter.com/analog_cs) [Medium](https://medium.com/@analog_cs)

Distributed under the MIT license. See ``LICENSE.txt``.
