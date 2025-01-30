import json

# Gebruik een relatieve padnaam omdat het bestand in dezelfde map staat
input_file = "2000-096.json"
output_file = "factuur_2000-096.json"

# JSON inlezen
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract relevante factuurgegevens
order = data["order"]
klant = order["klant"]
producten = order["producten"]

factuur_data = {
    "order": {
        "factuurnummer": order["ordernummer"],
        "factuurdatum": order["orderdatum"],
        "betaaltermijn": order["betaaltermijn"],
        "klant": {
            "naam": klant["naam"],
            "adres": klant["adres"],
            "postcode": klant["postcode"],
            "stad": klant["stad"],
            "KVK-nummer": klant["KVK-nummer"]
        },
        "producten": []  # Dit staat nu correct **binnen** "order"
    }
}

# Productgegevens verwerken en totaalprijs berekenen
totaal_excl_btw = 0
totaal_btw = 0

for product in producten:
    prijs_excl = product["aantal"] * product["prijs_per_stuk_excl_btw"]
    btw = prijs_excl * (product["btw_percentage"] / 100)
    totaal_excl_btw += prijs_excl
    totaal_btw += btw

    factuur_data["order"]["producten"].append({  # Dit is nu correct binnen "order"
        "productnaam": product["productnaam"],
        "aantal": product["aantal"],
        "prijs_per_stuk_excl_btw": product["prijs_per_stuk_excl_btw"],
        "totaal_excl_btw": round(prijs_excl, 3),
        "btw_percentage": product["btw_percentage"],
        "btw_bedrag": round(btw, 3)
    })

# Eindtotalen toevoegen
factuur_data["order"]["totaal_excl_btw"] = round(totaal_excl_btw, 3)
factuur_data["order"]["totaal_btw"] = round(totaal_btw, 3)
factuur_data["order"]["totaal_incl_btw"] = round(totaal_excl_btw + totaal_btw, 3)

# JSON opslaan als factuur
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(factuur_data, f, indent=4)

print(f"Factuur opgeslagen als: {output_file}")
