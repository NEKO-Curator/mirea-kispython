def transpose(table):
    response = []
    for i in range(len(table[2])):
        response.append([])
        for j in range(len(table)):
            response[i].append(table[j][i])
    return response


def delete_empty_rows(table):
    return [row for row in table if row[2] is not None]


def delete_duplicate_columns(table):
    for column in table:
        del column[0]
    return table


def transformer(i, j, value, table):
    if i == 0:
        forione = table[1][j].split('|')
        ionedate = forione[0].split('-')
        return f'{(ionedate[2])[2:]}/{ionedate[1]}/{ionedate[0]}'
    if i == 1:
        foritwo = table[1][j].split('|')
        proc = foritwo[1].replace('%', '')
        x = int(proc)/100
        return format(x, '.3f')
    if i == 2:
        return ("Да", "Нет")[value != "Выполнено"]


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(i, j, table[i][j], table)
    return table


def main(table):
    return transform(
                    transpose(
                        delete_duplicate_columns(
                            delete_empty_rows(table)
                        )
                    )
                )

if __name__ == '__main__':
    print(main([[None, None, None, None], [None, None, '19-08-2002|14%', 'Не выполнено'], [None, None, '02-06-2001|33%', 'Выполнено'], [None, None, '09-07-2004|58%', 'Выполнено'], [None, None, None, None], [None, None, '25-07-2000|3%', 'Выполнено']]))