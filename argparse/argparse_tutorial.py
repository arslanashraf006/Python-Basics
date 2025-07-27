#command to run in terminal
#python filename.py -h for help
#python filename.py arg arg op
#for optional arg python filename.py --argname val --argname val --opname val
import argparse

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    #positional arg
    parse.add_argument("number1", help = "first number")
    parse.add_argument("number2", help = "second number")
    #if you want to restrict choices then use choice otherwise skip it
    parse.add_argument("operation", help = "operation", choices=['add', 'subtract','multiply'])
    #optional arg
    # parse.add_argument("--number1", help = "first number")
    # parse.add_argument("--number2", help = "second number")
    # parse.add_argument("--operation", help = "operation")
    args = parse.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    op = args.operation
    result = None
    if op == "add":
        result = n1 + n2
    elif op == "subtract":
        result = n1 - n2
    elif op == "multiply":
        result = n1 * n2
    else:
        print("unsupported data")
    print(result)