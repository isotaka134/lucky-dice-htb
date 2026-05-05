#!/usr/bin/env python3
import socket
import re

HOST = "TARGET_IP"
PORT = TARGET_PORT


def solve():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.settimeout(2)

    def recv_until_prompt():
        data = b""
        while b"> " not in data:
            chunk = s.recv(8192)
            if not chunk:
                break
            data += chunk
        return data.decode(errors="replace")

    # Intro
    recv_until_prompt()

    # Start game
    s.sendall(b"1\n")

    for _ in range(100):
        output = recv_until_prompt()

        players_ordered = []

        for line in output.splitlines():
            m = re.match(r"Player\s+(\d+):\s+([\d\s]+)", line.strip())
            if m:
                player_num = int(m.group(1))
                dice = list(map(int, m.group(2).split()))
                players_ordered.append((player_num, sum(dice)))

        if not players_ordered:
            print("Parse failed")
            print(output)
            return

        max_score = max(score for _, score in players_ordered)

        winner = None
        for player_num, score in players_ordered:
            if score == max_score:
                winner = player_num

        s.sendall(f"{winner}\n".encode())

    # Final flag
    final = b""
    while True:
        try:
            chunk = s.recv(8192)
            if not chunk:
                break
            final += chunk
        except:
            break

    print(final.decode(errors="replace"))
    s.close()


if __name__ == "__main__":
    solve()
