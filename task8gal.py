import re


def main(source):
    p = r"\#([A-Za-z0-9-_]+)[=\s]?"
    p2 = r"\>\s([A-Za-z0-9-_]+)"
    matches2 = re.findall(pattern=p, string=source)
    matches = re.findall(pattern=p2, string=source)
    res = {}
    for key in matches:
        array = []
        for value in matches2:
            array.append(int(value))
            matches2.remove(value)
            break
        res[key] = array
    return res
if __name__ == '__main__':
    print(main('\\begin{{ let(#-3101 . #-493 . #5818 } => edisen_915. }}. {{ let {#-7455 . #-8261} => oresar_543.}}. {{ let {#4463 . #9022} => anrile_503. }} \\end'))