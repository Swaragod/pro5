from datetime import datetime
import os


def new_path(log_path):
    def logger(original_function):
        rr = input()

        def new_function(*args, **kwargs):
            print(log_path)
            start_time = datetime.now().strftime("%Y/%m/%d -%H:%M:%S")
            result = original_function(*args, **kwargs)
            log_info = f'{start_time}   -   function:   {original_function.__name__}{args}_{kwargs}   -   result:    {result}'

            with open("logging.txt", 'a') as file:
                file.write(log_info + '\n')
            print(rr)
            return result


        return new_function

    return logger 
