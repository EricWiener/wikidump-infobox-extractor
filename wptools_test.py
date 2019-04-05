import wptools
page = wptools.page("American_Communications_Ass'n_v._Douds")
page.get_parse()
print(page.data['infobox'])
