# Hello World

A simple Python project that demonstrates a hello world function with type hints and proper documentation.

## Installation

### Prerequisites
- Python 3.6 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/chaoweimt/claudecode-test.git
cd claudecode-test
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Run the script:
```bash
python3 main.py
```

Expected output:
```
Hello, World!
```

### Use as a module:
```python
from main import hello_world

# Default greeting
hello_world()  # Output: Hello, World!

# Custom greeting
hello_world("Alice")  # Output: Hello, Alice!
```

## Features

- Type hints for better IDE support
- Customizable greeting name
- Comprehensive docstrings
- Clean, documented code

## Development

### Running tests
```bash
# Run the main script
python3 main.py

# Test with custom name
python3 -c "from main import hello_world; hello_world('YourName')"
```

### Type checking (optional)
```bash
pip install mypy
mypy main.py
```

## License

MIT License
