from Bio.KEGG import REST

# Create the search query and get the ID
search = REST.kegg_find("pathway", "bacterial+secretion").read()
pathway_ID = search.split()[0][5:]

# Get the orthology ID
orthology_ID = pathway_ID.replace("map", "ko")

# Call the details
details = REST.kegg_get(orthology_ID).read()

indicator = False
line_number = 0
for data in details.split("\n"):
    if data.startswith("ORTHOLOGY"):
        indicator = True
    if data.startswith("COMPOUND"):
        indicator = False
    if indicator:
      line_number += 1
print(f"Pathway orthology number: {line_number}")