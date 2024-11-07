def mentes(art, filename="rajzok.txt"):
    try:
        with open(filename, "a") as file:
            file.write(art + "\n")
        print("A rajz mentve lett a fájlba.")
    except IOError:
        print("Hiba történt a fájl mentése közben.")