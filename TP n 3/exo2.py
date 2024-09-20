import random

# Seuil critique pour déclencher une alerte
seuil_critique = 35.0

# Générer 10 valeurs de température envoyées par un capteur IoT
temperatures = [random.uniform(20, 40) for _ in range(10)]

# Parcourir les valeurs collectées et vérifier les alertes
for i, temperature in enumerate(temperatures, 1):
    if temperature > seuil_critique:
        # Si la température dépasse le seuil, déclencher une alerte
        print(f"ALERTE ! Température {i} : {temperature:.2f}°C (dépasse le seuil critique de {seuil_critique}°C)")
    else:
        # Sinon, afficher la température normale
        print(f"Température {i} : {temperature:.2f}°C (normale)")

# Afficher la liste complète des températures pour référence
print("\nListe complète des températures :")
print(temperatures)
