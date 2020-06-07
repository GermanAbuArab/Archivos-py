import math
tabla = [[0,31663,0],[31633,45190,0.1],[45190,67785,0.15],[67785,135570,0.24],[135570,225950,0.25],
         [225950,338925,0.27],[338925,519685,0.31],[519685,math.inf,0.36]]

def calculo_irpf(tabla, salario):
    irpf_calculado = 0
    for i in range(0, 8):
        if salario > tabla[i][1]:
            irpf_calculado = irpf_calculado + tabla[i][2]*( tabla[i][1] - tabla[i][0])
        else:
            irpf_calculado = irpf_calculado + (salario - tabla[i][0]) * tabla[i][2]
            break
    return irpf_calculado


def main():
    while True:
        salario = int(input('Ingrese un salario nominal mensual (0 para finalizar): '))
        if salario == 0:
          break
        print(f'El IRPF para un salario mensual de ${salario} es {calculo_irpf(tabla,salario)}.')



if __name__ == '__main__':
    main()
