import os
import stat
import datetime
import sys
# import pwd
# import grp
import argparse

description = ''


def ordenar_abc(directorios):
    for i in range(0, len(directorios) - 1):
        for j in range(0, len(directorios) - 1):
            if ( directorios[j] > directorios[j + 1]):
                aux = directorios[j]
                directorios[j] = directorios[j + 1]
                directorios[j+1] = aux
    return directorios


def ordenar_fecha(directorios):
    for i in range(0,len(directorios)-1):
        for j in range(0,len(directorios)-1):
            if (os.stat('./' + directorios[j]).st_ctime> os.stat('./' + directorios[j+1]).st_ctime):
                aux=directorios[j]
                directorios[j]= directorios[j+1]
                directorios[j+1]=aux
    return directorios


def main():
    parse = argparse.ArgumentParser(description)
    groupA = parse.add_mutually_exclusive_group()
    groupA.add_argument("-a", '--all', help="Incluye los archivos cuyo nombre comienza con punto", action="store_true")
    groupI = parse.add_mutually_exclusive_group()
    groupI.add_argument("-i", '--inode', help="muestra en la primera columna el número de nodo-i", action="store_true")
    groupD = parse.add_mutually_exclusive_group()
    groupD.add_argument('-d', help="Lista el propio directorio, no los archivos contenidos en él", action="store_true")
    groupD.add_argument('--directory', help="Lista el propio directorio, no los archivos contenidos en él", action="store_true")
    parse.add_argument('-l', help="Genera un listado largo", action="store_true")
    parse.add_argument('-t', help=" Ordena según fecha de modificación en lugar de alfabético", action="store_true")
    #parse.add_argument("nombre")
    args = parse.parse_args()

    directorios = os.listdir(path='.')  # The list is in arbitrary order,
    if not args.all:
        i=0
        while i < len(directorios):
            if directorios[i][0] == '.':
                directorios.pop(i)
                i=i-1
            i+=1
    if args.d:
        directorios=['.']

    #if args.nombre todo

    directorios=ordenar_abc(directorios)
    if args.t:
        directorios=ordenar_fecha(directorios)
    if args.l:
        for i in range(len(directorios)):
            directorio=os.stat('./' + directorios[i])
            directorios[i] = ( directorio.st_mode,directorio.st_nlink,directorio.st_uid,directorio.st_gid, directorio.st_size, datetime.datetime.fromtimestamp(float(directorio.st_ctime)),directorios[i] )
    if args.inode:
        if args.l:
            for i in range(len(directorios)):
                print(f" {os.stat('./' + directorios[i][-1]).st_ino} {directorios[i][0]} {directorios[i][1]} {directorios[i][2]} {directorios[i][3]} {directorios[i][4]} {directorios[i][5]} {directorios[i][6]}")
        else:
            for i in range(len(directorios)):
                print(f"{os.stat('./' + directorios[i]).st_ino} {directorios[i]}")
        return 0
    for i in range(0,len(directorios)):
        print(f"{directorios[i]}")
    return 0


if __name__ == '__main__':
    main()
