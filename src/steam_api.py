import requests

# Centralized base URL for Steam API
STEAM_API_BASE_URL = "https://api.steampowered.com"

def get_wishlist(api_key, steam_id):
    """
    Fetches the wishlist of a user from the Steam API.

    :param api_key: The user's Steam API key.
    :param steam_id: The user's Steam ID.
    :return: A list of app IDs in the user's wishlist.
    """
    url = f"{STEAM_API_BASE_URL}/IWishlistService/GetWishlist/v1"
    params = {
        "key": api_key,
        "steamid": steam_id,
        "format": "json"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # Extract app IDs from the response
        wishlist = [item['appid'] for item in data.get('response', {}).get('items', [])]
        return wishlist
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wishlist: {e}")
        return []

def get_library(api_key, steam_id):
    """
    Fetches the library of a user from the Steam API.

    :param api_key: The user's Steam API key.
    :param steam_id: The user's Steam ID.
    :return: A list of dictionaries with app details in the user's library.
    """
    url = f"{STEAM_API_BASE_URL}/IPlayerService/GetOwnedGames/v0001/"
    params = {
        "key": api_key,
        "steamid": steam_id,
        "format": "json"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # Extract app IDs from the response
        library = [item['appid'] for item in data.get('response', {}).get('games', [])]
        return library
    except requests.exceptions.RequestException as e:
        print(f"Error fetching library for Steam ID {steam_id}: {e}")
        return []

def get_game_name(api_key, app_id):
    """
    Fetches the game name for a given app ID using the Steam API.

    :param api_key: The user's Steam API key.
    :param app_id: The app ID of the game.
    :return: The name of the game, or the app ID if the name cannot be fetched.
    """
    url = f"{STEAM_API_BASE_URL}/ISteamUserStats/GetSchemaForGame/v2/"
    params = {
        "key": api_key,
        "appid": app_id,
        "format": "json"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("game", {}).get("gameName", str(app_id))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game name for app ID {app_id}: {e}")
        return str(app_id)