import os
import yaml
from pprint import pprint


TEST_FILE='lists/basic_list.yaml'

def main():
    print(os.getcwd())
    dirs = os.listdir()
    for d in dirs:
        print(d)

    with open(TEST_FILE) as f:
        #  text = f.read()

        y = yaml.load(f)
        pprint(y)
        #  print(text)
