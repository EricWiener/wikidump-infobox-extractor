from .infodump import parse_dump
import sys
import argparse
import os


# check if file exists
def file(fname):
    if not os.path.isfile(fname):
        raise argparse.ArgumentTypeError("%r is not a valid file" % (fname,))
    return fname


# create output directories
# https://stackoverflow.com/a/12517490/6942666
def output_file(fname):
    dirname = os.path.dirname(fname)
    if dirname is not "" and not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise argparse.ArgumentTypeError(
                    "An error was encountered attempting to create output file %r" % (fname,))
    return fname


def js_ext(fname):
    if not fname.lower().endswith(('.js')):
        raise argparse.ArgumentTypeError("%r is not a .js" % (fname,))
    return fname


def xml_ext(fname):
    if fname != "" and not fname.lower().endswith(('.xml')):
        raise argparse.ArgumentTypeError("%r is not a .xml file" % (fname,))
    return fname


# checks if file has .ext and exists
def js_file(fname):
    output_file(fname)
    js_ext(fname)
    return fname


def xml_file(fname):
    file(fname)
    xml_ext(fname)
    return fname


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("dump", type=xml_file, help="Full path of wiki dump")
    parser.add_argument("outputFile", type=js_file, help="Full path of output file")
    return parser.parse_args()


def main():
    args = parse_args(sys.argv[1:])
    parse_dump(args.dump, args.outputFile)


if __name__ == '__main__':
    main()
