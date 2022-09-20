from datetime import datetime
import os


def new_path(log_path):
    def logger(original_function):
        def new_function(*args, **kwargs):

            if not os.path.isdir(log_path):
                os.makedirs(log_path)

            start_time = datetime.now().strftime("%Y/%m/%d -%H:%M:%S")
            result = original_function(*args, **kwargs)
            log_info = f'{start_time}   -   function:   {original_function.__name__}' \
                       f'{args}_{kwargs}   -   result:    {result}'

            full_path = os.path.join(log_path, "logs.txt")
            with open(full_path, 'a') as file:
                file.write(log_info + '\n')

            print(f'Лог функции: {original_function.__name__} сохранен в файле: {full_path}')
            return result

        return new_function

    return logger
