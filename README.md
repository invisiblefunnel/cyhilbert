# cyhilbert

A cythonized version of that one hilbert function you keep copy-pasting. See the original implementation of [Hilbert curves in O(log(n)) time](http://threadlocalmutex.com/?p=126).

```python
from cyhilbert import hilbert, DIMS, BITS_PER_DIM, MAX

DIMS #=> 2
BITS_PER_DIM #=> 16
MAX #=> 65535

hilbert(0, 0) #=> 0
hilbert(1, 0) #=> 1
hilbert(1, 1) #=> 2
hilbert(0, 1) #=> 3
hilbert(0, 2) #=> 4
hilbert(0, 3) #=> 5
hilbert(1, 3) #=> 6
hilbert(1, 2) #=> 7
```
