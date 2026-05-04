from organizador import organizar, simular_organizar

simular_organizar(r"C:\Users\lopes\Downloads")

if input("\nDeseja organizar os arquivos? (s/n) ").lower() == "s":
    organizar(r"C:\Users\lopes\Downloads")
else:   
    print("Organização cancelada.")

