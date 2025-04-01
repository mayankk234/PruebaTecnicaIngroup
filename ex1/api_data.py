import requests, json

def get_api_data(url: str) -> tuple[str, list[dict]]:
    """
    Fetch JSON data from a URL and convert it to a tuple containing 'users' and a list of user dictionaries.

    Args:
        url (str): The URL to fetch JSON data from

    Returns:
        tuple[str, list[dict]]: A tuple containing 'users' and a list of user dictionaries

    Raises:
        requests.RequestException: If there's an error fetching the data
        ValueError: If the response is not valid JSON
    """
    try:
        # Make HTTP GET request to the URL
        response = requests.get(url)
        # Raise an exception for bad status codes
        response.raise_for_status()
        # Parse JSON response
        data = response.json()
        # Transform the data into the required format
        users = [{
            'name': user.get('name'),
            'email': user.get('email'),
            'preferences': [int(p) for p in (user.get('preferences').split(',') if isinstance(user.get('preferences'), str) else user.get('preferences', [])) if p],
            'affiliate': user.get('affiliate') == 'true'
        } for user in data.get('users', [])]
        return ('users', users)
    except requests.RequestException as e:
        raise requests.RequestException(f"Error fetching data from {url}: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Error parsing JSON from {url}: {str(e)}")

def fetch_data_from_urls(urls: list[str]) -> list[tuple[str, list[dict]]]:
    """
    Fetch data from a list of URLs and return the results.

    Args:
        urls (list[str]): The list of URLs to fetch data from

    Returns:
        list[tuple[str, list[dict]]]: A list containing tuples of user data from each URL
    """
    results = []
    for url in urls:
        try:
            result = get_api_data(url)
            results.append(result)
        except (requests.RequestException, ValueError) as e:
            print(f"Error: {str(e)}")
    return results

# Example usage
if __name__ == "__main__":
    test_urls = [
        "https://invelonjobinterview.herokuapp.com/api/test1",
        "https://invelonjobinterview.herokuapp.com/api/test2"
    ]
    results = fetch_data_from_urls(test_urls)
    print(json.dumps(results))