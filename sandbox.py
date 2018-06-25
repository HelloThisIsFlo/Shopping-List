import os
import yaml
from pprint import pprint

TEST_FILE='basic_list.yaml'

def main():
    dirs = os.listdir()
    for d in dirs:
        print(d)

    with open(TEST_FILE) as f:
        #  text = f.read()

        y = yaml.load(f)
        pprint(y)
        #  print(text)
