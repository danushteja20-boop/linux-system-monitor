import os

print("===== CPU INFO =====")
os.system("top -b -n1 | head -5")

print("\n===== MEMORY INFO =====")
os.system("free -h")

print("\n===== DISK USAGE =====")
os.system("df -h")

print("\n===== CURRENT USER =====")
os.system("whoami")
