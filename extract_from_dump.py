import re
import sys
import argparse
import os
import xml.etree.ElementTree as ET
import json


def parse_dump(dumpLocation, outputPath):
    tree = ET.parse(dumpLocation)
    root = tree.getroot()
    ns = 'http://www.mediawiki.org/xml/export-0.10/'

    infoboxes = []

    # https://stackoverflow.com/a/36415473/6942666
    for page in root.findall('{%s}page' % ns):
        page_title = page.find('{%s}title' % ns).text
        page_text = page.find('{%s}revision' % ns).find('{%s}text' % ns).text

        # location of opening initial bracket
        # case insensitive
        infobox_start = page_text.find("nfobox") - 1
        if infobox_start is -1:
            print("No infobox")
            break

        bracket_count = 0
        end_index = infobox_start
        for i in range(infobox_start, len(page_text)):
            char = page_text[i]
            if char is "}":
                bracket_count -= 1
            elif char is "{":
                bracket_count += 1

            if bracket_count is -2:
                # reached end of info box
                end_index = i - 1
                break

        infobox_content_list = page_text[infobox_start:end_index].splitlines()[1:]

        infobox = {"title": page_title}
        for entry in infobox_content_list:
            key_data = entry.strip()[1:].split("=")
            key = key_data[0].strip()
            data = ""
            if len(key_data) == 2:
                data = key_data[1].strip()
            infobox[key] = data

        infoboxes.append(infobox)

    file = open(outputPath, 'w')
    file.write(json.dumps(infoboxes, ensure_ascii=False))
    file.close()

    print("Wikidump parsed and saved at " + outputPath)

# check if file exists


def file(fname):
    if not os.path.isfile(fname):
        raise argparse.ArgumentTypeError("%r is not a valid file" % (fname,))
    return fname


# create output directories
# https://stackoverflow.com/a/12517490/6942666
def output_file(fname):
    if not os.path.exists(os.path.dirname(fname)):
        try:
            os.makedirs(os.path.dirname(fname))
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


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    parse_dump(args.dump, args.outputFile)
