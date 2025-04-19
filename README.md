# Steam Wishlist Cleanup

This Python script allows you to compare your Steam wishlist with the libraries of your friends or family members. It identifies games that are both in your wishlist and in the libraries of the specified Steam accounts.

https://steamcommunity.com/dev
https://steamwebapi.azurewebsites.net/

## Features
- Fetches your Steam wishlist using the Steam Web API.
- Fetches the libraries of your friends or family members using their Steam IDs.
- Compares your wishlist with the combined libraries of the specified accounts.
- Outputs a list of games that are present in both your wishlist and the specified libraries.

## Prerequisites
- Python 3.x installed on your system.
- A Steam API key. You can get one from [Steam's API Key page](https://steamcommunity.com/dev/apikey).

## Project Structure

```
steam-wishlist-cleanup
├── src
│   ├── main.py          # Entry point of the application
│   ├── steam_api.py     # Functions to interact with the Steam API
│   ├── utils.py         # Utility functions for comparison
│   └── __init__.py      # Marks the directory as a Python package
├── requirements.txt      # Lists project dependencies
├── .gitignore            # Specifies files to ignore in Git
└── README.md             # Project documentation
```

## Installation
1. Clone this repository or download the source code.
2. Install the required Python dependencies:
   ```bash
   pip install requests
   ```

## Usage

1. Open `src/main.py` and set your Steam user ID and the Steam IDs of your friends or family members.
2. Run the script:
   ```
   python src/main.py
   ```
3. The script will fetch your wishlist and the libraries of the specified accounts, then display any games that are present in both lists.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.