# Количество натуральных делителей числа X
def findNum(x):
    i = 2;
    degree = 0;
    result = 1;
    while x >= 1:
        if x % i == 0:
            degree += 1;
            x = x // i;
        else:
            result *= (degree + 1);
            degree = 0;
            i += 1;
            if x == 1: return result;

print(findNum(1000000000));