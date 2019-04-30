import xml.etree.ElementTree as ET
import json


def unmatched_bracket(text):
    """
    Returns true if there is an unmatched bracket
        this is a sentence {with a bracket } - false
        this is a sentence {with a bracket } and {this - true
    """
    for c in reversed(text):
        if c is "}":
            return False
        elif c is "{":
            return True


def parse_dump(dumpLocation, outputPath):
    """

    Still won't handle something like:
    No equal sign and the previous item ended with a bracket. Just poor data formatting.
    "| Litigants               Hughes v. Alexandria Scrap Corp."
    """

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

        # element 0 is "Infobox SCOTUS case" usually
        # however sometimes you get things like {{infobox| above       = Kansas v. Colorado
        # first split into lines
        # then merge with the most recent line that started with a |
        # this avoids considering pipes such as those in "{{ussc|525|961|1998|el=no}}"
        """
        |OralArgument=https://www.oyez.org/cases/1990-1999/1998/1998_98_377/argument/
        |Prior=Patent application 07/479,666 filed, February 13, 1990;
      Examiner's rejection affirmed by Board of Patent Appeals and Interferences, ''Ex parte Zurko, et al'', July 31, 1995 (_ USPQ 2d _, Appeal No. 94-3967);
      request for reconsideration denied, December 1, 1995;
      Board decision reversed, ''In re Zurko, et al'' 111 [[F.3d]] [https://law.justia.com/cases/federal/appellate-courts/F3/111/887/630610/ 887] ([[Fed. Cir.]] 1997);
      reheard, Board decision reversed, 142 [[F.3d]] [https://law.justia.com/cases/federal/appellate-courts/F3/142/1447/506854/ 1447] (Fed. Cir. 1998) (en banc);
      petition for writ of certiorari granted, {{ussc|525|961|1998|el=no}}
        """
        infobox_content_list = page_text[infobox_start:end_index].splitlines()

        # if there is no infobox continue
        if len(infobox_content_list) == 0:
            continue

        # need to handle the first line special
        # this could be of the forms:
        """
        {{infobox| above       = Arizona v. California
        {{Infobox SCOTUS case
        or many other variations
        """
        if len(infobox_content_list[0].split("|", 1)) == 2:
            # need to add pipe back in after the split
            # pipe is needed later on
            infobox_content_list[0] = "|" + infobox_content_list[0].split("|")[1]
        else:
            infobox_content_list = infobox_content_list[1:]

        infobox_merged_content = []
        for line in infobox_content_list:
            line = line.strip()
            if len(line) is 0:
                continue
            elif line[0] is "|":
                infobox_merged_content.append(line)
            else:
                infobox_merged_content[-1] += " " + line

        infobox = {"title": page_title}
        for entry in infobox_merged_content:
            key_data = entry.strip().split("=", 1)  # only split on first "="

            # multiple strips because it might look like
            # "    | Key = Text"
            # Need to remove up to |, remove bar, and then strip again
            key = key_data[0].lstrip()[1:].strip()  # removes "|"

            if len(key) > 0 and key[0] is "|":
                # sometimes have duplicate |'s because why would this be easy
                # eg: ||NotParticipating=Stewart and Fortas
                key = key[1:]

            data = ""

            if len(infobox) > 0 and unmatched_bracket(infobox[list(infobox.keys())[-1]]):
                infobox[list(infobox.keys())[-1]] += " " + key
                continue
                # there is no "="
                # this could be due to being part of a list
                """
                    |Holding={{Ordered list|style=text-align: left
                      | The forced extraction and analysis of a blood sample is not compelled testimony and therefore does not violate the Fifth Amendment Right against self-incrimination
                      | Intrusions into the human body require a warrant
                      | Here, the warrantless blood test was permissible under the exigent circumstances exception to prevent the destruction of alcohol in the blood stream through the body's natural metabolic processes
                  }}

                  or

                    | Holding           = {{ordered list |style=text-align: left;
                        |1=States may not prohibit citizens from contracting insurance out of state for acts performed outside the state.
                        |2=States may not prohibit citizens from contracting insurance out of state by written communication, even if the property to be insured is within the state.
                        }}

                  Note the above has "="
                """

            if len(key_data) == 2:
                data = key_data[1].strip()

            infobox[key] = data

        infoboxes.append(infobox)

    file = open(outputPath, 'w')
    file.write(json.dumps(infoboxes, ensure_ascii=False))
    file.close()

    print("Wikidump parsed and saved at " + outputPath)


parse_dump('../wiki-dump.xml', 'wiki-dump-out.js')
