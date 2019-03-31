'''
args.jg.py -- Testes e experiências por JG, recolha de argumentos de entrada duma script.
              Para correr, ver args.jg.bat.
30/03/2019
'''
#----------
#--- Testes com o módulo argparse -- muito mais satisfatório que getopt.
#    Argumento automático -h, sendo passado mostra ajuda.
#    Se os argumentos não estiverem conformes, avisa e gera uma exceção.

import argparse

parser = argparse.ArgumentParser( description='Normalizador de parágrafos.' ) # Criar objeto.

parser.add_argument('-x','-xml', help='Resultado em XML.', action="store_true") # Irá aceitar -x ou -xml; sendo passado, será True.
parser.add_argument('--pt', help='Ficheiro em Português.') # Ex.: passar --pt FicheiroPT.txt
parser.add_argument('--en', help='Ficheiro em Inglês.') # Ex.: passar --en FicheiroEN.txt

args = parser.parse_args()

print(args)
if args.x:
    print("Então quer xml, hem?")

if args.pt == None:
    print("PT = None, sem PT.")
else:    
    print("PT =", args.pt)

if args.en == None:
    print("EN = None, not nun.")
else:    
    print("EN =", args.en)


