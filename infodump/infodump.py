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
