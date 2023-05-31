
a = 2.709; #начальные а и б
b = 2.811; #начальные а и б
i = 0;  #просто чтоб считать шаги


def matic2():
    global a
    global b
    global i
    y_a = round(a ** 3 - 3 * (a ** 2) + 1.5, 4) #тут мое уровнение f(x) (а на месте х) напиши свое
    y_b = round(b ** 3 - 3 * (b ** 2) + 1.5, 4) #тут уровнение f(x) (b на месте х)
    y_b2 = round(3 * (b ** 2) - 6 * b, 3) # f'(x)
    print(i);
    print("a = ", a);
    print("b = ", b);
    print("y(a) = ", y_a);
    print("y(b) = ", y_b);
    print("y'(b) = ", y_b2);

    a = round(a - ((y_a) * ((b - a) / (y_b - y_a))), 4)
    b = round(b - (y_b / y_b2), 4)
    i = i + 1
    while i != 6:
        return matic2()


matic2()
