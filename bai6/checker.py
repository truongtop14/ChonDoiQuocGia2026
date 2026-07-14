
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

from math import sqrt

def dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def closest(px):

    n = len(px)

    if n <= 3:

        ans = float("inf")

        for i in range(n):
            for j in range(i + 1, n):
                ans = min(ans, dist2(px[i], px[j]))

        return ans, sorted(px, key=lambda p: p[1])

    mid = n // 2

    xmid = px[mid][0]

    dl, leftY = closest(px[:mid])
    dr, rightY = closest(px[mid:])

    d = min(dl, dr)

    py = []

    i = j = 0

    while i < len(leftY) and j < len(rightY):

        if leftY[i][1] < rightY[j][1]:
            py.append(leftY[i])
            i += 1
        else:
            py.append(rightY[j])
            j += 1

    py.extend(leftY[i:])
    py.extend(rightY[j:])

    strip = []

    for p in py:

        if (p[0] - xmid) * (p[0] - xmid) < d:

            for q in strip[-7:]:

                d = min(d, dist2(p, q))

            strip.append(p)

    return d, py


def solve(points):

    px = sorted(points)

    ans2, _ = closest(px)

    return "{:.6f}".format(sqrt(ans2))
# ==================================================
# TEST GENERATOR
# ==================================================
# ==================================================
# TEST GENERATOR
# ==================================================

def gen_test(sub):

    if sub == 1:

        n = random.randint(2, 2000)

    elif sub == 2:

        n = random.randint(20001, 50000)

    else:

        n = random.randint(100000, 200000)

    points = []
    used = set()

    while len(points) < n:

        x = random.randint(-10**9, 10**9)
        y = random.randint(-10**9, 10**9)

        if (x, y) not in used:

            used.add((x, y))
            points.append((x, y))

    return n, points


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
    1: 20,
    2: 30,
    3: 50
}

score = 0

EPS = 1e-6

for sub in [1, 2, 3]:

    print("\n" + "=" * 60)
    print("Subtask", sub)

    ok = True

    for tc in range(TEST_PER_SUBTASK):

        n, points = gen_test(sub)

        inp = str(n) + "\n"

        for x, y in points:
            inp += f"{x} {y}\n"

        out_cpp, runtime, status = run_cpp(inp)

        if status == "TLE":

            print(f"Test {tc+1}: TLE")
            ok = False
            break

        if status != "OK":

            print(status)
            ok = False
            break

        out_std = solve(points)

        try:

            ans_cpp = float(out_cpp)
            ans_std = float(out_std)

            if abs(ans_cpp - ans_std) > EPS:

                print(f"Test {tc+1}: WA")

                print("\nInput:")
                print(inp[:1000])

                print("\nExpected:", out_std)
                print("Got     :", out_cpp)

                ok = False
                break

        except:

            print("Invalid Output")
            ok = False
            break

        print(f"Test {tc+1}: AC ({runtime:.4f}s)")

    if ok:

        score += SUBTASK_SCORE[sub]

        print(f"Subtask {sub}: Accepted (+{SUBTASK_SCORE[sub]} điểm)")

    else:

        print(f"Subtask {sub}: Failed")

print("\n" + "=" * 60)
print("FINAL SCORE:", score, "/100")
print("=" * 60)