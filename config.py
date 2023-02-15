import yaml
from yaml.loader import SafeLoader


def get():
    with open('./config.yaml') as config:
        data = yaml.load(config, Loader=SafeLoader)
    return data

