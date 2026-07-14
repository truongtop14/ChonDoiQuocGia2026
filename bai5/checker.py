
import os
import random
import subprocess
import time


# ==================================================
# CONFIG
# ==================================================
# Thư mục chứa checker.py
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CPP_FILE = os.path.join(
    BASE_DIR,
    "main.cpp"
)


EXE_FILE = os.path.join(
    BASE_DIR,
    "main.exe"
)

TIME_LIMIT = 1.0          # seconds
TEST_PER_SUBTASK = 5

# ==================================================
# COMPILE
# ==================================================

print("=" * 60)
print("Compiling...")

ret = subprocess.run(
    [
        "g++",
        CPP_FILE,
        "-O2",
        "-std=c++17",
        "-o",
        EXE_FILE
    ],
    capture_output=True,
    text=True
)

if ret.returncode != 0:
    print("Compile Error")
    print(ret.stderr)
    exit()

print("Compile Success!")

# ==================================================
# PRECOMPUTE PRIME SIEVE
# ==================================================

MAXN = 10**7

print("Building Sieve...")

is_prime = [True] * (MAXN + 1)

is_prime[0] = False
is_prime[1] = False

i = 2
while i * i <= MAXN:

    if is_prime[i]:

        j = i * i

        while j <= MAXN:
            is_prime[j] = False
            j += i

    i += 1

prefix = [0] * (MAXN + 1)

for i in range(1, MAXN + 1):
    prefix[i] = prefix[i - 1] + (1 if is_prime[i] else 0)

print("Sieve Done!")

# ==================================================
# OFFICIAL SOLUTION
# ==================================================

def solve(n):
    return prefix[n]

# ==================================================
# TEST GENERATOR
# ==================================================

def gen_test(sub):

    if sub == 1:
        n = random.randint(1, 100000)

    elif sub == 2:
        n = random.randint(1, 1000000)

    else:
        n = random.randint(1, 10000000)

    return n

# ==================================================
# RUN CPP
# ==================================================

def run_cpp(inp):

    with open("input.txt", "w") as f:
        f.write(inp)

    start = time.perf_counter()

    try:

        with open("input.txt") as fin, \
             open("output.txt", "w") as fout:

            subprocess.run(
                [EXE_FILE],
                stdin=fin,
                stdout=fout,
                stderr=subprocess.PIPE,
                timeout=TIME_LIMIT
            )

        elapsed = time.perf_counter() - start

        with open("output.txt") as f:
            out = f.read().strip()

        return out, elapsed, "OK"

    except subprocess.TimeoutExpired:

        return "", TIME_LIMIT, "TLE"

    except Exception as e:

        return "", 0, str(e)

# ==================================================
# JUDGE
# ==================================================

SUBTASK_SCORE = {
    1:20,
    2:30,
    3:50
}

score = 0

for sub in [1,2,3]:

    print("\n" + "=" * 60)
    print("Subtask",sub)

    ok = True

    for tc in range(TEST_PER_SUBTASK):

        n = gen_test(sub)

        inp = str(n) + "\n"

        out_cpp, runtime, status = run_cpp(inp)

        if status == "TLE":

            print(f"Test {tc+1}: TLE")
            ok = False
            break

        if status != "OK":

            print(status)
            ok = False
            break

        out_std = str(solve(n))

        if out_cpp != out_std:

            print(f"Test {tc+1}: WA")

            print("\nInput:")
            print(inp)

            print("Expected:",out_std)
            print("Got     :",out_cpp)

            ok = False
            break

        print(f"Test {tc+1}: AC ({runtime:.4f}s)")

    if ok:

        score += SUBTASK_SCORE[sub]

        print(f"Subtask {sub}: Accepted (+{SUBTASK_SCORE[sub]} điểm)")

    else:

        print(f"Subtask {sub}: Failed")

print("\n" + "=" * 60)
print("FINAL SCORE:",score,"/100")
print("=" * 60)