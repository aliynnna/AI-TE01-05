from collections import deque

antrean = deque(["Alyn", "Nabila", "Shafa"])

yang_dicari = input("Mau cari siapa? ")

nomor = 1
ketemu = False

while antrean:
    orang = antrean.popleft()
    print("Memeriksa:", orang)

    if orang.lower() == yang_dicari.lower():
        print("Ketemu!", orang, "ada di urutan ke-", nomor)
        ketemu = True
        break

    nomor += 1

if not ketemu:
    print("Nama tidak ada di antrean.")
