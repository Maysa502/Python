# Usar o comando d importação para a biblioteca criada 
import ctypes
# O uso do módulo ctypes em Python é uma forma de criar uma ponte entre Python e C

lib = ctypes.CDLL("./mensagem.so")
lib.mensagem()
