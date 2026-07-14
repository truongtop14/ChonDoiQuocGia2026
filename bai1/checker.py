import os
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

print("=" * 50)
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
print("=" * 50)

# ==================================================
# SOLUTION
# ==================================================

def check(a, k, length):

    cnt = 0

    for x in a:

        cnt += x // length

        if cnt >= k:
            return True

    return False


def solve(a, k):

    if sum(a) < k:
        return 0

    l = 1
    r = max(a)

    ans = 0

    while l <= r:

        mid = (l + r) // 2

        if check(a, k, mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


# ==================================================
# TEST GENERATOR
# ==================================================

def gen_test(subtask):

    if subtask == 1:

        n = random.randint(1, 20)
        k = random.randint(1, 100)

        a = [random.randint(1, 100) for _ in range(n)]

    elif subtask == 2:

        n = random.randint(1, 1000)
        k = random.randint(1, 5000)

        a = [random.randint(1, 1000) for _ in range(n)]

    elif subtask == 3:

        n = random.randint(50000, 100000)
        k = random.randint(1, 100000)

        a = [random.randint(1, 100000) for _ in range(n)]

    else:

        n = random.randint(100000, 200000)
        k = random.randint(1, 10**12)

        a = [random.randint(1, 10**9) for _ in range(n)]

    return n, k, a


# ==================================================
# RUN CPP
# ==================================================

def run_cpp(inp):

    with open("input.txt", "w") as f:
        f.write(inp)

    start = time.perf_counter()

    try:

        with open("input.txt", "r") as fin, \
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

        return "", 0, f"RE: {e}"


# ==================================================
# JUDGE
# ==================================================

SUBTASK_SCORE = {
    1: 20,
    2: 20,
    3: 30,
    4: 30
}

score = 0

for sub in [1, 2, 3, 4]:

    print("\n" + "=" * 50)
    print("Subtask", sub)

    ok = True

    for tc in range(TEST_PER_SUBTASK):

        n, k, a = gen_test(sub)

        inp = f"{n} {k}\n"
        inp += " ".join(map(str, a))
        inp += "\n"

        out_cpp, runtime, status = run_cpp(inp)

        if status == "TLE":

            print(f"Test {tc+1}: TLE (> {TIME_LIMIT}s)")
            ok = False
            break

        if status != "OK":

            print(status)
            ok = False
            break

        out_std = str(solve(a, k))

        if out_cpp != out_std:

            print(f"Test {tc+1}: WA")

            print("\nInput:")
            print(inp[:500])

            print("Expected:", out_std)
            print("Got     :", out_cpp)

            ok = False
            break

        print(f"Test {tc+1}: AC ({runtime:.4f}s)")

    if ok:

        score += SUBTASK_SCORE[sub]

        print(f"Subtask {sub}: Accepted (+{SUBTASK_SCORE[sub]} điểm)")
    else:

        print(f"Subtask {sub}: Failed")

print("\n" + "=" * 50)
print("FINAL SCORE:", score, "/100")
print("=" * 50)