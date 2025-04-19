import os
from datetime import datetime

def compare_lists(wishlist, library):
    return list(set(wishlist) & set(library))

def save_results_to_file(results):
    """
    Saves the results to a timestamped text file in the output folder.

    :param results: The results to save (list of strings).
    """
    # Determine the parent directory of the src folder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_folder = os.path.join(base_dir, "output")

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_folder, f"results_{timestamp}.txt")

    # Convert all items in the results list to strings
    results = [str(item) for item in results]

    # Write the results to the file
    with open(filename, "w") as file:
        file.write("\n".join(results))

    print(f"Results saved to {filename}")