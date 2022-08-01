# It is about electric force continuous distribution

import math
import os

def clean_window():
    """
    clean the window
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def validation_method(input_value):
    """
    Using validation with 'os'
    """
    while True:
        try:
            valor = float(input(input_value))
            return valor
        except ValueError:
            print("   ingresa un número")

def electricFCD():
    """
    All the calculations.
    """
    vector = 0
    vector_zero = []
    vector_position = []

    Q_0 = validation_method("Valor de la carga \'Q\': ")
    for iterator in range(3):
        if iterator == 0:
            vector = validation_method("   x_0: ")
        elif iterator == 1:
            vector = validation_method("   y_0: ")
        elif iterator == 2:
            vector = validation_method("   z_0: ")
        vector_zero.append(vector)
    print("   [x_0, y_0, z_0] = ", vector_zero)

    number_vectors = int(validation_method("cantidades de carga sobre \'Q\' = " + str(Q_0) + ": "))
    list_vector = []
    list_result_vector = []
    list_result_vector_sum = [0, 0, 0]
    list_result_vector_sum_total = []
    list_result_vector_sum_total_module = 0

    for num in range(1, number_vectors + 1):
        q = validation_method("   valor de la carga N°" + str(num) + ": ")
        print("   Posición de la carga N° ", num, ": ")
        for vector_i in range(1, 3 + 1):
            if vector_i == 1:
                vector = validation_method("   x_" + str(num) + ": ")
            elif vector_i == 2:
                vector = validation_method("   y_" + str(num) + ": ")
            elif vector_i == 3:
                vector = validation_method("   z_" + str(num) + ": ")
            list_vector.append(vector)
        print("    [x_"+str(num)+", y_"+str(num)+", z_"+str(num)+"] = ", list_vector)

        # Subtraction between 'list_vector' and 'vector_zero'
        for i in range(len(vector_zero)):
            vector_position.append(vector_zero[i] - list_vector[i])
        print("    [x_0, y_0, z_0] - [x_"+str(num)+", y_"+str(num)+", z_"+str(num)+"] = ",vector_position)

        R_MODULE = math.pow(
            math.pow(vector_position[0], 2) + math.pow(vector_position[1], 2) + math.pow(vector_position[2], 2),
            1.5)
        # print("module", R_MODULE)
        F_value = (Q_0 * q) / (R_MODULE)
        # print(F_value)
        for i in vector_position:
            result = i * F_value
            list_result_vector.append(result)

        # print("    ", list_RESULT_VECTOR)

        list_result_vector_sum[0] += list_result_vector[0]
        list_result_vector_sum[1] += list_result_vector[1]
        list_result_vector_sum[2] += list_result_vector[2]

        list_vector.clear()
        vector_position.clear()
        list_result_vector.clear()

    # print(list_RESULT_VECTOR_SUM)
    print("-"*30)
    for v in list_result_vector_sum:
        # e = 8.8541878176 * math.pow(10, -12)
        k = 9 * math.pow(10, 9)
        # result_TOTAL = v/(4*math.pi*e)
        result_TOTAL = v * k
        list_result_vector_sum_total.append(result_TOTAL)
    print(">> La fuerza resultante es: ")
    print("  ", list_result_vector_sum_total)
    # calculate the module of the resulting vector
    list_result_vector_sum_total_module = math.pow(
        math.pow(list_result_vector_sum_total[0], 2) +
        math.pow(list_result_vector_sum_total[1], 2) +
        math.pow(list_result_vector_sum_total[2], 2), 0.5
    )
    
    print(">> Posee un modulo de: ")
    print("  ", list_result_vector_sum_total_module)

def run():
    clean_window()
    print("-"*30)
    print("WELCOME")
    while True:
        option = int(validation_method("MENU \n 1-Solve the problem \n 2-Exit\n Option: "))
        if option == 1:
            electricFCD()
            break
        elif option == 2:
            break
        else:
            print("opcion incorrecta")
            clean_window()
            continue

    print("-"*30)

if __name__ == '__main__':
    # electricFCD()
    run()
    # result_TOTAL =0
    # k=12
    # e_0 = 8.8541878176 * math.pow(10, -12)
    # result_TOTAL =  k*9*math.pow(10,9)
    # print(result_TOTAL)
