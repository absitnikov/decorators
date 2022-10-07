from dec_log import logger
import os

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
path = os.path.abspath('logs.txt')


@logger(path)
def flat_generator(list_gen):
    for item in list_gen:
        if isinstance(item, list):
            for xs in flat_generator(item):
                yield xs
        else:
            yield item


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
