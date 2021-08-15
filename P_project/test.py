import pokepy
import requests

description = pokepy.V2Client().get_pokemon_species(1).flavor_text_entries[0].flavor_text
description = description.replace("\n", " ")

poke_desc = ''
for i in description:
    poke_desc += i
    if i == '.':
        break


# for i in description:
#     print (i)

print(poke_desc)

# strObj = "This is a sample string"
# start = 5
# stop = 10
# # Remove charactes from index 5 to 10
# if len(strObj) > stop :
#     strObj = strObj[0: start:] + strObj[stop + 1::]