import time  # Import time for rate limiting
from steam_api import get_wishlist, get_library, get_game_name  # Import get_game_name
from utils import compare_lists, save_results_to_file  # Import save_results_to_file from utils

# Hardcoded values (set to None or empty if you want to prompt the user)
HARDCODED_API_KEY = None
HARDCODED_USER_ID = None
HARDCODED_FAMILY_IDS = None

# Time to wait between API requests (in seconds)
DELAY_BETWEEN_REQUESTS = 5

def main():
    # Use hardcoded values or prompt the user if they are not set
    api_key = HARDCODED_API_KEY or input("Enter your Steam API Dev key: ")
    user_id = HARDCODED_USER_ID or input("Enter your Steam User ID: ")
    family_ids = HARDCODED_FAMILY_IDS.split(',') if HARDCODED_FAMILY_IDS else input(
        "Enter the Steam IDs of users in your Steam Family(comma-separated): "
    ).split(',')

    wishlist = get_wishlist(api_key, user_id)
    
    # Add a delay between each API request
    time.sleep(DELAY_BETWEEN_REQUESTS)

    family_libraries = []
    for steam_id in family_ids:
        family_libraries.extend(get_library(api_key, [steam_id]))
        # Add a delay between each API request
        time.sleep(DELAY_BETWEEN_REQUESTS)

    # Find common games
    common_games = compare_lists(wishlist, family_libraries)

    # Append game names to the list of common games
    common_games_with_names = []
    for app_id in common_games:
        game_name = get_game_name(api_key, app_id)
        common_games_with_names.append(f"{app_id} - {game_name}")
        # Add a delay between each API request
        time.sleep(DELAY_BETWEEN_REQUESTS)

    # Prepare results for output
    results = []
    if common_games_with_names:
        results.append("Games in both your wishlist and available via family library:")
        results.extend(common_games_with_names)
    else:
        results.append("No common games found in your wishlist and any family library.")

    # Print results to the screen
    for line in results:
        print(line)

    # Save results to a file
    save_results_to_file(results)

if __name__ == "__main__":
    main()