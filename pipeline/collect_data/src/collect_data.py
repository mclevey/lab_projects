import os
import yaml
import pandas as pd
import logging
logfile = __file__.split('/')[-1].replace('.py', '.log')
logging.basicConfig(filename=logfile, 
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(funcName)s:%(message)s')


def load_config(config_path: str ='../input/config.yaml'):
    with open(config_path, 'rb') as file:
        params = yaml.safe_load(file)
    return params

config = load_config()

with open('../output/test.md', 'w') as f:
    for r in config['subreddits']:
        f.write(f'{r}\n')

logging.debug(config['subreddits'])
logging.debug(config['sample_n_conversations'])
