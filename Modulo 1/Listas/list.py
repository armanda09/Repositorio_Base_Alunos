nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial:", nomes)

nomes.append("Carlos")
print("Após append:", nomes)

nomes.insert(1, "Fernanda")
print("Após insert:", nomes)

nomes[2] = "Paulo"
print("Após modificação:", nomes)
"\n"
del nomes[3]
print("Após del:", nomes)

nomes.remove("Maria")
print("Após remove:", nomes)

removido = nomes.pop(2)
print(f"Após pop (removido '{removido}'):", nomes)

nomes.clear()
print("Após clear:",nomes)