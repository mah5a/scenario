import codecs
import csv
import urllib
from extend_list import ExtendList


def main():
    url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
    stream = urllib.request.urlopen(url)
    csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))
    print(type(csv_file))

    iris_lst = []
    for row in csv_file:
        IRIS = ExtendList(row)
        iris_lst.append(IRIS)
        print(iris_lst)

    iris_lst = iris_lst[1:]
    print(iris_lst)


if __name__ == '__main__':
    main()
