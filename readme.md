# Threading Experiment in Python

This project is a practice script demonstrating multithreading in Python using the built-in threading module.

It attempts to launch multiple threads under specific limits, simulating basic control over concurrent execution.



# installation
`bash`

python -m venv .venv

.venv\Scripts\activate

and you should import:
```python
import threading
import time
```
## What It Does

- Defines two functions: test1 (single print and sleep) and test2 (looped print and sleep).
- Tries to run:
  - test1 threads only if 2 or fewer with name "test1" are running
  - test2 threads only if 3 or fewer with name "test2" are running
- Each thread prints its assigned value and sleeps for a short, random time.
- The script stops after i = 9.
- The code attempts to control how many threads of each type are running simultaneously.

- Thread names are used to count active threads using threading.enumerate().
---


## How to Run

1. Save the script as test.py
2. Run it via terminal:

`bash`
python test.py