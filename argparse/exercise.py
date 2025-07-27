import argparse

if __name__ == "__main__":
    parcer = argparse.ArgumentParser()
    parcer.add_argument("--physics", help = "physics marks")
    parcer.add_argument("--chemistry", help = "chemistry marks")
    parcer.add_argument("--math", help="math marks")

    args = parcer.parse_args()

    phy = int(args.physics)
    che = int(args.chemistry)
    math = int(args.math)

    avg = (phy + che + math)/3
    print("average:", avg)