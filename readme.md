# Python Threading Example: Countdown Timers

This project is a simple demonstration of Python multithreading using the threading module.  
It creates multiple countdown timers that run in parallel, simulating concurrent tasks.

# installation
`bash`

python -m venv .venv

.venv\Scripts\activate

and you should import:
```python
import threading
import time
```

## Purpose

To show how you can:
- Create and start multiple threads
- Pass arguments to thread functions
- Use thread.join() to wait for threads to finish
- Observe interleaved (mixed) output due to parallel execution

---

## How to Run ?

1. Save the script as thread.py
2. Run it using:

`bash`
python thread.py

### Output Example

Because threads run in parallel, the printed output will be interleaved.
Each thread prints its name and countdown step every second.

Thread A → 5

Thread B → 3

Thread C → 7

Thread B → 2

Thread A → 4

...

Thread C finished!
 All threads completed.

---
### What is thread.join()?

thread.start() → Starts a new thread.

thread.join() → Tells Python: “Wait here until this thread finishes.”


This ensures that the main program doesn't exit before all threads complete their tasks.
