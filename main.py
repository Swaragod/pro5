from decorator import logger
import os


@logger
def summa(a, b):
    res_ = a + b
    return res_

@logger
def multi(a, b):
    res_ = a * b
    return res_

@logger
def div(a, b):
    res_ = a / b
    return res_


if __name__ == '__main__':

    summa(100, 500)
    multi(200, 45)
    summa(500, 544400)
    summa(520, -53500)
    summa(0, 50330)
    div(563, 50)

print(os.getcwd())






