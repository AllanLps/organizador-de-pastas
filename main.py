from organizador import organizar, simular_organizar

simular_organizar(r"C:\seu\caminho\aqui")

if input("\nDeseja organizar os arquivos? (s/n) ").lower() == "s":
    organizar(r"C:\seu\caminho\aqui")
else:   
    print("Organização cancelada.")

