import json
import uvicorn
from codingchallenge_qa_service.app_main import create_app


def load_config(file_path):
    """
    Load the JSON configuration file.

    Args:
        file_path (str): Path to the JSON configuration file.

    Returns:
        dict: Configuration settings loaded from the JSON file.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        json.JSONDecodeError: If the configuration file has invalid JSON format.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise e


def main():
    """
    Main entry point of the application.
    """
    config_file_path = 'config/app_config.json'
    config = load_config(config_file_path)
    uvicorn.run(app=create_app(), **config)


if __name__ == '__main__':
    main()
