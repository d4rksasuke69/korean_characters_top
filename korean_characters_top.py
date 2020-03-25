import random

if __name__ == "__main__":
    with open("build_result.txt", "w") as f:
        a = random.randint(0,1)
        if a:
            f.write("BUILD SUCCESS")
        else:
            f.write("BUILD FAILED")
