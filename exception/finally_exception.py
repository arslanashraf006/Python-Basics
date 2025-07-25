def process_file():
    f = None  
    try:
        f = open("c:\\code\\data.txt")
        x = 1 / 0
    except FileNotFoundError as e:
        print("inside except - File not found")
    finally:
        print("cleaning up file")
        if f is not None:
            f.close()

process_file()
