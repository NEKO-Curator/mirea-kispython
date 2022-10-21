def main(y):
    if y == 0:
        return -0.03
    if y>=1:
        return main(y-1)-27*main(y-1)**3

if __name__ == '__main__':
    print(main(8))