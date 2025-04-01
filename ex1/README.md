# API Data Fetching Module

This module provides functionality to fetch and transform user data from multiple API endpoints.

## Features

- Fetches JSON data from specified URLs
- Transforms user data into a standardized format
- Handles errors gracefully
- Supports multiple URL processing

## Project Structure

```
ex1/
├── api_data.py      # Main module with API fetching functionality
└── README.md        # Documentation
```

## Requirements

- Python 3.x
- requests library

Install dependencies:
```bash
pip install requests
```

## Usage

```python
from api_data import fetch_data_from_urls

urls = [
    "https://invelonjobinterview.herokuapp.com/api/test1",
    "https://invelonjobinterview.herokuapp.com/api/test2"
]

results = fetch_data_from_urls(urls)
print(json.dumps(results))
```

## Function Documentation

### get_api_data(url: str) -> tuple[str, list[dict]]

Fetches and transforms data from a single URL.

**Parameters:**
- `url` (str): The URL to fetch JSON data from

**Returns:**
- tuple[str, list[dict]]: A tuple containing 'users' and a list of user dictionaries

### fetch_data_from_urls(urls: list[str]) -> list[tuple[str, list[dict]]]

Fetches data from multiple URLs.

**Parameters:**
- `urls` (list[str]): List of URLs to fetch data from

**Returns:**
- list[tuple[str, list[dict]]]: List of tuples containing user data from each URL

## Data Format

The transformed user data follows this structure:
```python
{
    'name': str,
    'email': str,
    'preferences': list[int],
    'affiliate': bool
}
```

## Error Handling

The module handles two types of errors:
- `requests.RequestException`: For network-related errors
- `ValueError`: For JSON parsing errors