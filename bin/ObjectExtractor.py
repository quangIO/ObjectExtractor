#!/usr/bin/env python
from object_extractor import Extractor
import sys
import os

def main():
    print(os.getcwd() + '\\' + sys.argv[1])
    return Extractor.extract(os.getcwd() + '\\' + sys.argv[1])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ObjectExtractor filename.png')
        sys.exit(1)
    print(str(main()) + ' objects found')