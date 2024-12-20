# Liste des logs (adresses IP et horodatage)
logs = [
    ('192.168.1.1', '2024-09-12 12:15:10'),
    ('192.168.1.2', '2024-09-12 12:16:15'),
    ('192.168.1.1', '2024-09-12 12:20:20'),
    ('192.168.1.3', '2024-09-12 12:30:25'),
    ('192.168.1.1', '2024-09-12 12:35:30')
]

# 1. Comptage des connexions par IP
ip_counts = {ip: logs.count(ip) for ip, _ in logs}

# Afficher les IPs avec plus de 3 connexions
for ip, count in ip_counts.items():
    if count > 3:
        print(f"IP connectée plus de 3 fois : {ip}, Nombre de connexions : {count}")

# 2. Trouver la première et la dernière connexion
first_connection, last_connection = min(logs, key=lambda x: x[1]), max(logs, key=lambda x: x[1])

print(f"Première connexion : IP: {first_connection[0]}, Heure: {first_connection[1]}")
print(f"Dernière connexion : IP: {last_connection[0]}, Heure: {last_connection[1]}")

# 3. Nombre total d'adresses IP uniques
print(f"Nombre total de connexions uniques : {len(set(ip for ip, _ in logs))}")
