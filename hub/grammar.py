from flask import Flask, request
import copy

grammar = Flask(__name__)

@grammar.route("/")
def solution():
    matrix_param = request.values["mx"]
    matrix = eval(matrix_param)

    org_matrix = copy.deepcopy(matrix)

    sum_org = 0

    new_matrix = copy.deepcopy(matrix)

    new_matrix = new_matrix[1:]

    index = 0

    ghosts = []

    ghosts1 = []



    for row in new_matrix:
        for row1 in matrix:
            for num1 in row1:
                if row[index] + num1 == row[index]:
                    ghosts.append(row[index])
                index += 1

            index = 0
            break

    matrix = matrix[1:]
    new_matrix = new_matrix[1:]

    for row in new_matrix:
        for row1 in matrix:
            for num1 in row1:
                if row[index] + num1 == row[index]:
                    ghosts1.append(row[index])
                index += 1

            index = 0
            break

    for sth in org_matrix:
        for number in sth:
            sum_org += number


    allghosts = list(ghosts) + list(ghosts1)


    intersect = set(ghosts1).intersection(set(ghosts))
    intersect = list(intersect)

    allghosts = sum(allghosts) - sum(intersect)

    price = sum_org - allghosts

    return f"<h1>price is {price}</h1>"


@grammar.route("/page")
def page():
    with open("Example Domain.html", 'r') as file:
        return file.read()


@grammar.route("/palindrome")
def palindrome():
    string = request.values["palindrome"].lower().replace(" ", "")
    rev_string = string[::-1]
    if string == rev_string:
        return "True"
    else:
        return "False"

@grammar.route("/pal")
def pal():
    with open("palindrome.html", 'r') as file:
        return file.read()


if __name__ == '__main__':
    grammar.run(host="0.0.0.0", port=20000)


