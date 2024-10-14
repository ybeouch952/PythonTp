packets = [
    (500, 'TCP'),
    (1000, 'UDP'),
    (2000, 'TCP'),
    (50, 'ICMP'),
    (1600, 'TCP'),
    (800, 'UDP')
]

# Q1

print("Tous les paquets réseau :")
for packet in packets:
    print(packet)

#Q2

print("Paquets qui depassent 1500 octets :")
for packet in packets:
    if packet[0] > 1500:
        print(packet)

#Q3

tcp_compteur = 0
udp_compteur = 0
total_packets = 0

for packet in packets:
    total_packets = total_packets+ 1
    if packet[1] == 'TCP':
        tcp_compteur = tcp_compteur+1 
    elif packet[1] == 'UDP':
        udp_compteur = udp_compteur + 1

tcp_pourcentage = (tcp_compteur * 100) / total_packets 
udp_pourcentage = (udp_compteur * 100) / total_packets 

print("Pourcentage de paquets TCP :",tcp_pourcentage)
print("Pourcentage de paquets UDP :",udp_pourcentage)