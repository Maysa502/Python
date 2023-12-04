import modulo

ez = "quero jogar joguin"
print(ez)
enc = modulo.caesar(ez, 18)
print(enc)
print(modulo.caesar(enc, 18, decode = True))