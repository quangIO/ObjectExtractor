#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser

from object_extractor import Extractor, FRONTALFACE_DEFAULT


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', dest='image_path', help='filename.png', required=True)
    parser.add_argument('-s', '--size', nargs='?', dest='size', help='Size of face images (default None, no rescale '
                                                                     'at all)', default=None)
    parser.add_argument('-x', '--scale', nargs='?', dest='scale_factor', help='Specifying how much the image size is '
                                                                              'reduced at each image scale (default '
                                                                              '1.1)',
                        type=float, default=1.1)
    parser.add_argument('--min_neighbors', nargs='?', dest='min_neighbors', help='Specifying how many neighbors each '
                                                                                 'candidate rectangle should have to '
                                                                                 'retain it (default 5).', default=5,
                        type=int)
    parser.add_argument('-o', '--output', nargs='?', dest='output_directory', help='Directory where to save output',
                        default=os.getcwd())
    parser.add_argument('--min_size', nargs='?', dest='min_size', help='Minimum possible object size. Objects smaller '
                                                                       'than that are ignored (default (50,50)).',
                        default=(50, 50))
    parser.add_argument('--cascade_file', nargs='?', dest='cascade_file', default=FRONTALFACE_DEFAULT)
    parser.add_argument('--output_prefix', nargs='?', dest='output_prefix', default=None)
    parser.add_argument('--start_count', nargs='?', dest='start_count', help='Specifying the starting of the number '
                                                                             'put into output names (default 0)',
                        default=0, type=int)

    arguments = vars(parser.parse_args())
    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)
    return Extractor.extract(**arguments)


if __name__ == '__main__':
    print('Found ' + str(main()) + ' object(s)')
