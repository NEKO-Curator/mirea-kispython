def transpose(table):
    response = []
    for i in range(len(table[0])):
        response.append([])
        for j in range(len(table)):
            response[i].append(table[j][i])
    return response


def delete_empty_rows(table):
    return [row for row in table if row[0] is not None]


def delete_duplicate_columns(table):
    for row in table:
        del row[5]
    for row in table:
        del row[2]
    for row in table:
        del row[1]
    return table


def transformer(i, value):
    if i == 0:
        return (value + '0')
    if i == 1:
        dig = value.split('-')
        return f'{(dig[2])[2:]}-{dig[1]}-{dig[0]}'
    if i == 2:
        replaced = value\
            .replace('[at]', '@')
        return replaced
    if i == 3:
        value = value\
            .replace('(', '')\
            .replace(') ', '-')
        dig = value.split('-')
        return f'{dig[0]}-{dig[1]}-{dig[2]}{dig[3]}'


def transform(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = transformer(i, table[i][j])
    return table


def main(table):
    return transpose(
            transform(
                transpose(
                    delete_duplicate_columns(
                        delete_empty_rows(table)
                    )
                )
            )
    )

if __name__ == '__main__':
    print(main([['0.08', None, '01-08-2003', '01-08-2003', 'zuvudan45[at]yandex.ru', None, '(060) 427-44-44'], ['0.24', None, '10-05-2001', '10-05-2001', 'bukananz56[at]gmail.com', None, '(768) 237-75-70'], [None, None, None, None, None, None, None], ['0.18', None, '07-07-2001', '07-07-2001', 'vagoranz39[at]rambler.ru', None, '(211) 602-83-23'], [None, None, None, None, None, None, None], ['0.61', None, '08-10-2002', '08-10-2002', 'tifanz68[at]gmail.com', None, '(061) 217-74-70']]))