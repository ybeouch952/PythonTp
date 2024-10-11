def verifier_coordonnees_gps(coordonnees):
    appareils_a_verifier = []

    for appareil in coordonnees:
        latitude, longitude = coordonnees[appareil]
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            appareils_a_verifier.append(appareil)

    return appareils_a_verifier

coordonnees = {
    "appareil_1": (45.0, 120.0),
    "appareil_2": (95.0, -75.0),  # Latitude invalide
    "appareil_3": (-10.0, 200.0),  # Longitude invalide
    "appareil_4": (30.0, 60.0)
}

print("Appareil à verifier ",verifier_coordonnees_gps(coordonnees))