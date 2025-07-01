import socket

# Dicionário com nomes comuns de serviços por porta
nomes_portas = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

def scan_ports(host, portas=None):
    if portas is None:
        portas = list(nomes_portas.keys())

    print(f"\n\033[1;36m🔎 Escaneando {host}...\033[0m")
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("\033[1;31m❌ Host inválido ou não encontrado.\033[0m")
        return

    for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, porta))
        nome = nomes_portas.get(porta, "Desconhecido")
        if resultado == 0:
            print(f"\033[1;32m✅ Porta {porta} ABERTA ({nome})\033[0m")
        else:
            print(f"\033[1;31m⛔ Porta {porta} FECHADA ({nome})\033[0m")
        sock.close()


def main():
    host = input("\nDigite o IP ou site para escanear: ").strip()
    if not host:
        print("Informe um host válido.")
        return
    scan_ports(host)


if __name__== '__main__':
    main()
    