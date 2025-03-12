import requests

# Constants
API_KEY = "5cIMwGuI2ftsaF/83xkd6w==UryyKLg1DKEWpbZn"
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animal data from the API.

    Returns: a list of animals, each represented as a dictionary.
    """
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(f"{API_URL}?name={animal_name}", headers=headers)

    if response.status_code == requests.codes.ok:
        return response.json()  # Returns a list of animals
    else:
        return None  # Handle errors in the main program
