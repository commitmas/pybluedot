import configparser
import os

def create_config(path):
    """
    Create pybluedot config file
    """
    config = configparser.ConfigParser()
    config.add_section('Global')
    config.set('Global', 'API_KEY', input('Enter your NASA API Key:'))
    config.add_section('Patent')
    config.set('Patent', 'URL', 'https://api.nasa.gov/patents/content')
    config.add_section('APOD')
    config.set('APOD', 'URL', 'https://api.nasa.gov/planetary/apod')
    config.add_section('NEO')
    config.set('NEO', 'URL', 'https://api.nasa.gov/neo/rest/v1')
    config.add_section('EPIC')
    config.set('EPIC', 'URL', 'https://api.nasa.gov/EPIC/api')
    config.add_section('IMAGERY')
    config.set('IMAGERY', 'URL', 'https://api.nasa.gov/planetary/earth/imagery')
    config.add_section('ASSETS')
    config.set('ASSETS', 'URL', 'https://api.nasa.gov/planetary/earth/assets')
    config.add_section('IMAGES')
    config.set('IMAGES', 'URL', 'https://images-api.nasa.gov')
    config.add_section('ROVERS')
    config.set('ROVERS', 'URL', 'https://api.nasa.gov/mars-photos/api/v1/rovers')
    config.add_section('SOUNDS')
    config.set('SOUNDS', 'URL', 'https://api.nasa.gov/planetary/sounds')
    config.add_section('TECHPORT')
    config.set('TECHPORT', 'URL', 'https://api.nasa.gov/planetary/sounds')

    with open(path, 'w') as config_file:
        config.write(config_file)

def get_config(path):
    """
    Return config object.
    """
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    return config

if __name__ == '__main__':
    path = 'pybluedotconf.py'
    get_config(path)


