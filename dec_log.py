from datetime import datetime


def logger(path):
    def _logger(function):
        def new_function(*args, **kwargs):
            result = f'function call time: {datetime.now().strftime("%b %d %Y %H:%M:%S")}\n'\
                     f'name function: {function.__name__}\n'\
                     f'arguments: {args}, {kwargs}\n'\
                     f'return value: {function(*args, **kwargs)}'
            with open(path, 'w', encoding='utf-8') as file:
                file.write(result)
            return result
        return new_function
    return _logger
