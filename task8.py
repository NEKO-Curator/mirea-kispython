import re


def main(source):
    p = r"\#([A-Za-z0-9-_]+)[=\s]?"
    p2 = r"\"([A-Za-z0-9-_]+)\""
    matches2 = re.findall(pattern=p, string=source)
    matches = re.findall(pattern=p2, string=source)
    res = {}
    for key in matches:
        for value in matches2:
            res[key] = int(value)
            matches2.remove(value)
            break
    return res

if __name__ == '__main__':
    print(main('\\begin do loc #-842=>"biri_954"; done do loc #8243 =>"zaxe_913";done\ndo loc#-662=> "isonce"; done do loc#-3656 => "teve"; done \\end'))