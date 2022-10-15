from cmath import log
import re


def main(source):
    p = r"\(([A-Za-z0-9-_ `,\r\n]+)\)"
    p2 = r"\'([A-Za-z0-9-_]+)"
    matches2 = re.findall(pattern=p, string=source)
    matches = re.findall(pattern=p2, string=source)
    res = {}
    for key in matches:
        array = []
        for value in matches2:
            values = value.split(',')
            for value2 in values:
                without_spaces = value2.strip()
                new_string = without_spaces[1:]

                # for clear_world in without_spaces:
                #     clear
                array.append(new_string)
            matches2.remove(value)
            break
        res[key] = array
    return res
if __name__ == '__main__':
    print(main('<section> <:loc array( `enonbe , `anar )-> @\'xear\'; :>; <: loc array(`teen, `arainre ,`labiso, `incece_652) -> @\'isdi\'; :>; <: loc array(`teed_577 , `laon)-> @\'arordi_632\'; :>; </section>'))