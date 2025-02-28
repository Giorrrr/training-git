from rumus_matematika import RumusMatematika

def main():
    print("Hello from main-app!")
    print("Hasil dari 4 + 5 :", RumusMatematika.tambah(4,5))
    print("Hasil dari 4 - 5 :", RumusMatematika.kurang(4,5))
    print("Hasil dari 4 * 5 :", RumusMatematika.kali(4,5))
    print("Hasil dari 4 / 5 :", RumusMatematika.bagi(4,5))


if __name__ == "__main__":
    main()
