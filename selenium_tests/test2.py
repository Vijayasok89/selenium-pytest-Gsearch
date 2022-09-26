import configparser
import os
config = configparser.ConfigParser()
config.read('env_config.ini')
print(config.sections())
gecko_path = config.get('driver','geckodriver_path')
print(os.path.join(os.path.dirname(__file__),config.get('driver','geckodriver_path')))