# I'm going to solve a physics problem
# It is about electric force continuous distribution
# import math module
import math
# from fundamentals.Class_3_MoreControlFlowTools.ifStatement import printLine
# For validation I need import 'os'
import os
# print(os.name)
def Clean_THEWINDOW():
    # clean the window
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def welcome():
    Clean_THEWINDOW()
    print("-"*30)
    print("WELCOME")
    while True:
        option = int(validation_METHOD("MENU \n 1-Solve the problem \n 2-Exit\n Option: "))
        if option == 1:
            electricFCD()
            break
        elif option == 2:
            break
        else:
            print("opcion incorrecta")
            Clean_THEWINDOW()
            continue

    print("-"*30)
def validation_METHOD(valor_INPUT):
    # using validation with 'os'
    while True:
        try:
            valor = float(input(valor_INPUT))
            return valor
        except ValueError:
            # VALIDATION_FIRST = input("   ingrese un numero: \n   1-cambiar numero \n   2-reiniciar\n
            # option: ") if VALIDATION_FIRST == 1:
            print("   ingresa un número")
            Clean_THEWINDOW()

def electricFCD():
    vector = 0
    vector_ZERO = []
    vector_POSITION = []

    Q_0 = validation_METHOD("Valor de la carga \'Q\': ")
    for iterator in range(3):
        if iterator == 0:
            # using validation with 'os'
            vector = validation_METHOD("   x_0: ")
        elif iterator == 1:
            vector = validation_METHOD("   y_0: ")
        elif iterator == 2:
            vector = validation_METHOD("   z_0: ")
        vector_ZERO.append(vector)
    print("   [x_0, y_0, z_0] = ", vector_ZERO)

    number_VECTORS = int(validation_METHOD("cantidades de carga sobre \'Q\' = " + str(Q_0) + ": "))
    list_VECTOR = []
    list_RESULT_VECTOR = []
    list_RESULT_VECTOR_SUM = [0, 0, 0]
    list_RESULT_VECTOR_SUM_TOTAL = []
    list_RESULT_VECTOR_SUM_TOTAL_MODULO = 0

    for num in range(1, number_VECTORS + 1):
        q = validation_METHOD("   valor de la carga N°" + str(num) + ": ")
        print("   Posición de la carga N° ", num, ": ")
        for vector_i in range(1, 3 + 1):
            if vector_i == 1:
                vector = validation_METHOD("   x_" + str(num) + ": ")
            elif vector_i == 2:
                vector = validation_METHOD("   y_" + str(num) + ": ")
            elif vector_i == 3:
                vector = validation_METHOD("   z_" + str(num) + ": ")
            list_VECTOR.append(vector)
        print("    [x_"+str(num)+", y_"+str(num)+", z_"+str(num)+"] = ", list_VECTOR)

        # rest 'list_VECTOR' y 'vector_ZERO'
        for i in range(len(vector_ZERO)):
            vector_POSITION.append(vector_ZERO[i] - list_VECTOR[i])
        print("    [x_0, y_0, z_0] - [x_"+str(num)+", y_"+str(num)+", z_"+str(num)+"] = ",vector_POSITION)

        R_MODULE = math.pow(
            math.pow(vector_POSITION[0], 2) + math.pow(vector_POSITION[1], 2) + math.pow(vector_POSITION[2], 2),
            1.5)
        # print("module", R_MODULE)
        F_value = (Q_0 * q) / (R_MODULE)
        # print(F_value)
        for i in vector_POSITION:
            result = i * F_value
            list_RESULT_VECTOR.append(result)

        # print("    ", list_RESULT_VECTOR)

        list_RESULT_VECTOR_SUM[0] += list_RESULT_VECTOR[0]
        list_RESULT_VECTOR_SUM[1] += list_RESULT_VECTOR[1]
        list_RESULT_VECTOR_SUM[2] += list_RESULT_VECTOR[2]

        list_VECTOR.clear()
        vector_POSITION.clear()
        list_RESULT_VECTOR.clear()

    # print(list_RESULT_VECTOR_SUM)
    print("-"*30)
    for v in list_RESULT_VECTOR_SUM:
        # e = 8.8541878176 * math.pow(10, -12)
        k = 9 * math.pow(10, 9)
        # result_TOTAL = v/(4*math.pi*e)
        result_TOTAL = v * k
        list_RESULT_VECTOR_SUM_TOTAL.append(result_TOTAL)
    print(">> La fuerza resultante es: ")
    print("  ", list_RESULT_VECTOR_SUM_TOTAL)
    # calculate the module of the resulting vector
    list_RESULT_VECTOR_SUM_TOTAL_MODULO = math.pow(math.pow(list_RESULT_VECTOR_SUM_TOTAL[0], 2) +
                                                   math.pow(list_RESULT_VECTOR_SUM_TOTAL[1], 2) +
                                                   math.pow(list_RESULT_VECTOR_SUM_TOTAL[2], 2), 0.5)
    print(">> Posee un modulo de: ")
    print("  ", list_RESULT_VECTOR_SUM_TOTAL_MODULO)


# PRINT RESULT

# electricFCD()
welcome()
# result_TOTAL =0
# k=12
# e_0 = 8.8541878176 * math.pow(10, -12)
# result_TOTAL =  k*9*math.pow(10,9)
# print(result_TOTAL)
