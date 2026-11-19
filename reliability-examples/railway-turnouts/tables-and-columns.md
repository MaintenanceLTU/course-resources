# BIS

| Column | Type | Swedish | English |
|----------|----------|----------|----------|
| Bdl | text | Bandel | Line section |
| Pl_Forb | text | Driftplats | Location reference |
| Växelnr | text | Växelnummer | Turnout identifier |
| Växeltyp | text | Växeltyp | Turnout type |
| tunglängd | numeric | Tunglängd | Switch blade length |
| LÖ-radie | integer | Lågrälsradie | Diverging track radius |
| V/H-växel | text | Vänster- eller högerväxel | Left- or right-hand turnout |
| Hsp | text | nhsp: normal huvudspår, ahsp: avvikande huvudspår, ssp: sidospår | nhsp: main track, ahsp: alternative main track, ssp: side track |
| Inläggningsår Växel | integer | Installationsår för växel | Turnout installation year |
| Tillverkare Växel | text | Tillverkare av växel | Turnout manufacturer |
| Tillverkningsår Växel | integer | Tillverkningsår för växel | Turnout manufacturing year |
| Värmeeffekt(kW) totalt | numeric | Total installerad växelvärmeeffekt | Total switch heating power (kW) |
| Sliper typ | text | Slipertyp | Sleeper type |
| Befästningstyp | text | Befästningstyp | Fastening type |
| Ballast typ | text | Ballasttyp | Ballast type |
| Besiktningsklass | text | Besiktningsklass | Inspection class |
| Utrustad med växelvärme | text | Utrustad med växelvärme | Equipped with switch heating |
| Växeldriv modell | text | Modell på växeldriv | Point machine model |
| Antal växel driv | integer | Antal växeldriv | Number of point machines |
| KorsningModell | text | Korsningsmodell | Crossing model |


# OFELIA

| Column | Type | Swedish | English |
|----------|----------|----------|----------|
| Felrapport | text | Felrapportnummer | Failure report ID |
| Pl_Forb | text | Driftplats | Location reference |
| Bdl | text | Bandel | Line section |
| Tågstörande | text | Tågstörande fel | Train-delaying failure |
| Orsakskod | text | Orsakskod | Cause code |
| Anmält datum | timestamp | Datum då felet anmäldes | Failure report date |
| Vidareanmält | timestamp | Tidpunkt för vidareanmälan | Forwarded time |
| Påbörjat | timestamp | Tidpunkt då arbetet påbörjades | Work start time |
| Avhjälpt | timestamp | Tidpunkt då felet avhjälptes | Fault restoration time |
| Anläggningsindivid | text | Anläggningsindivid | Asset identifier |
| Anläggningstyp (BVS) | text | Anläggningstyp | Asset type |
| Växeltyp (ANL) | text | Växeltyp | Turnout type |
| Anläggningsdel (BVS) | text | Anläggningsdel | Asset part |


