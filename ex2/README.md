# Thread Concurrency Demo

This module demonstrates thread synchronization and ordered message printing using Python's threading module.

## Features

- Implements thread synchronization using locks
- Ensures ordered message printing across multiple threads
- Demonstrates proper thread management and coordination
- Uses a custom OrderedPrinter class for message synchronization

## Project Structure

```
ex2/
├── concurrency.py   # Main module with thread concurrency implementation
└── README.md        # Documentation
```

## Requirements

- Python 3.x
- No external dependencies required (uses standard library only)

## Implementation Details

### OrderedPrinter Class

Manages synchronized printing across multiple threads:

- Uses threading.Lock for synchronization
- Maintains order of thread execution
- Prevents race conditions in output

### concurrency_with_coffee() Function

Demonstrates thread coordination with a coffee-themed conversation:

- Creates 5 threads with ordered messages
- Ensures messages are printed in the correct sequence
- Provides a fun example of thread synchronization

## Usage

```python
from concurrency import concurrency_with_coffee

concurrency_with_coffee()
```

## Expected Output

```
- I'm tired, Bob! Do you know that our bodies are made of coffee? -Try drinking it! - You're right!
```

## Key Concepts

- Thread Synchronization
- Lock Mechanism
- Race Condition Prevention
- Ordered Execution
- Thread Management