import datetime
from pathlib import Path


def logger(target_function):

    def new_function(*args, **kwargs):

        start_time = datetime.datetime.now()
        result = target_function(*args, **kwargs)
        log_info = f'{start_time} - {target_function.__name__}{args}_{kwargs} = {result}'

        with open("logging.txt", 'a') as file:
            file.write(log_info + '\n')

        return result

    return new_function

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



summa(100, 500)
multi(200, 45)
summa(500, 544400)
summa(520, -53500)
summa(0, 50330)
div(563, 50)


PA = 'home/projects/pyscripts/python/sample.md'
PAA = Path.absolute(PA)
print(PAA)






