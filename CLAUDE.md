# Claude Code Context

## Project Overview

This is a simple Python project that demonstrates a hello world function with best practices including type hints, proper documentation, and comprehensive testing.

## Project Structure

```
claudecode-test/
├── main.py           # Main module containing hello_world function
├── test_main.py      # Unit tests for main.py
├── README.md         # User-facing documentation
└── CLAUDE.md         # This file - project context for Claude Code
```

## Key Components

### main.py
- `hello_world(name: str = "World") -> None`: Main function that prints a greeting
- `main() -> None`: Entry point for the script
- Uses type hints for better IDE support and code clarity
- Includes comprehensive docstrings with examples

### test_main.py
- Contains comprehensive test suite for the hello_world function
- Tests default behavior and custom name functionality

## Development Guidelines

### Code Style
- Use type hints for all function parameters and return values
- Write comprehensive docstrings following Google style guide
- Include examples in docstrings using `>>>` format
- Keep functions simple and focused

### Testing
- Write tests for all new functionality
- Test both default behavior and edge cases
- Use descriptive test names

### Python Version
- Target: Python 3.6+
- Uses only standard library (no external dependencies)

## Common Tasks

### Running the program
```bash
python3 main.py
```

### Testing
```bash
python3 -m pytest test_main.py
```

### Type checking
```bash
mypy main.py
```

## Conventions

- Use f-strings for string formatting
- Default values for optional parameters
- Return `None` for functions that print output
- Follow PEP 8 style guidelines
- Use meaningful variable names
