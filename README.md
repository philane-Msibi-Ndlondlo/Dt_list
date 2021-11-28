# Dt List

A data type enforce on a list in Python

NB: WIP

Create a list with only ints in it

# Example 1: List with Ints
``` python
from dt_list import Dt_list

    my_list = Dt_list('int', [1,2,4,4,5,6])
    my_list.add(2)
    my_list.add(23)
    print(my_list)

```

# Example 2: List with Strings
``` python
from dt_list import Dt_list

    my_list2 = Dt_list('str', [])
    my_list2.add(2) # Raise Error of 2 is not type of str, instead add '2'
    my_list2.add("string")

    print(my_list2)
    
```

# Example 3: Remove Item at index
``` python
from dt_list import Dt_list

    my_list = Dt_list('int', [1,2,4,4,5,6])
    my_list.remove_at(0) # Result: [2,4,4,5,6]
    my_list.add(23)
    print(my_list)

```

# Example 4: Get Length of dt list
``` python
from dt_list import Dt_list

    my_list = Dt_list('int', [1,2,4,4,5,6])
    my_list.add(23)
    print(my_list.length) # Result: 7

`
