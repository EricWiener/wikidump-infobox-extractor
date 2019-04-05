# https://en.wikipedia.org/wiki/2000_term_opinions_of_the_Supreme_Court_of_the_United_States
from bs4 import BeautifulSoup
import wikipedia

# get html representation of page given title
html_doc = (wikipedia.WikipediaPage(title='Cooper_v._Pate')).html()

# convert html string to BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# find infobox
infobox = soup.find("table", class_="infobox")


# find the justices involved
opinions_rows = infobox.find("tr", string="Justices").next_siblings

# find all rows after the case opinions header
opinions_rows = infobox.find("tr", string="Case opinions").next_siblings

# loop through the rows
opinions = []
for opinion_row in opinions_rows:
    if "style" in str(opinion_row.contents[0]):

        try:
            # if it is a per curiam decision
            # in a try block in case it is not a per curiam decision and
            # the contents[] chain would fail
            if opinion_row.contents[0].contents[0].contents[0].string == "Per curiam":
                opinions.append({"opinion": "per curiam"})
                continue
        except:
            # if the row has a style attribute and not per curiam, this is
            # the start of the next header. All opinions have been gathered
            break

    opinion_type = opinion_row.contents[0].string
    opinion_members = opinion_row.contents[1].string.replace(" joined by", "").split(",")
    opinion_author = opinion_members[0]
    opinion_joined = [member.strip() for member in opinion_members[1:]]
    opinions.append({"opinion": opinion_type, "author": opinion_author, "joinedBy": opinion_joined})
    # print(opinion_row.prettify())

for opinion in opinions:
    print(opinion)
