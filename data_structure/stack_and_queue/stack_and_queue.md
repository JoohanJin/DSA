# Stack and Queue
***

## Stack
- LIFO (last-in first-out) ordering
- the most recent item added to the stack is the first item to be removed.

#### Operations
- pop(): remove the top item from the stack
- push(item): add an item to the top of the stack
- peek(): return the top of the stack
- isEmpty(): return true iff the stack is empty

- Does not offer constant-time access to the ith item.
- Constant add and remove.
    - since it does not require shifting elements around
***

## Queue
- FIFO (first-in first-out) orderderng
- items are removed from the data strucutre in the same order that they are added

#### Operations
- add(item): add an item to the end of teh list
- remove(): remove the first item in the list
- peek(): return the top of the queue
- isEmpty(): 