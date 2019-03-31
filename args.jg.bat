@rem args.jg.bat -- batch para linha comandos MS-DOS
@rem Testa execucao de args.jg.py com vários argumentos.

@rem Opcao para mostrar a ajuda.
python args.jg.py -h
@pause

python args.jg.py -x
@pause

@rem Os dois seguintes são equivalentes.
python args.jg.py -xml --pt FilePT.txt
@pause
python args.jg.py -x --pt FilePT.txt
@pause

@rem Argumentos errados:
python args.jg.py -x Alien
@pause