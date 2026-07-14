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
# SEGMENT TREE
# ==================================================

def build(id, l, r, st, a):

    if l == r:
        st[id] = a[l]
        return

    mid = (l + r) // 2

    build(id * 2, l, mid, st, a)
    build(id * 2 + 1, mid + 1, r, st, a)

    st[id] = st[id * 2] + st[id * 2 + 1]


def update(id, l, r, pos, val, st):

    if l == r:
        st[id] = val
        return

    mid = (l + r) // 2

    if pos <= mid:
        update(id * 2, l, mid, pos, val, st)
    else:
        update(id * 2 + 1, mid + 1, r, pos, val, st)

    st[id] = st[id * 2] + st[id * 2 + 1]


def query(id, l, r, u, v, st):

    if v < l or r < u:
        return 0

    if u <= l and r <= v:
        return st[id]

    mid = (l + r) // 2

    return (
        query(id * 2, l, mid, u, v, st)
        + query(id * 2 + 1, mid + 1, r, u, v, st)
    )


def solve(a, operations):

    n = len(a) - 1

    st = [0] * (4 * (n + 5))

    build(1, 1, n, st, a)

    ans = []

    for op in operations:

        if op[0] == 1:

            _, i, x = op

            update(1, 1, n, i, x, st)

        else:

            _, l, r = op

            ans.append(str(query(1, 1, n, l, r, st)))

    return "\n".join(ans)

# ==================================================
# TEST GENERATOR
# ==================================================

def gen_test(sub):

    if sub == 1:

        n = random.randint(1, 1000)
        q = random.randint(1, 1000)

    elif sub == 2:

        n = random.randint(5000, 20000)
        q = random.randint(5000, 20000)

    else:

        n = random.randint(100000, 200000)
        q = random.randint(100000, 200000)

    a = [0]

    for _ in range(n):
        a.append(random.randint(-10**9, 10**9))

    ops = []

    for _ in range(q):

        if random.randint(0, 1):

            i = random.randint(1, n)
            x = random.randint(-10**9, 10**9)

            ops.append((1, i, x))

        else:

            l = random.randint(1, n)
            r = random.randint(l, n)

            ops.append((2, l, r))

    return n, q, a, ops

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

        n,q,a,ops = gen_test(sub)

        inp = f"{n} {q}\n"

        inp += " ".join(map(str,a[1:])) + "\n"

        for op in ops:

            if op[0] == 1:
                inp += f"1 {op[1]} {op[2]}\n"
            else:
                inp += f"2 {op[1]} {op[2]}\n"

        out_cpp, runtime, status = run_cpp(inp)

        if status == "TLE":

            print(f"Test {tc+1}: TLE")
            ok = False
            break

        if status != "OK":

            print(status)
            ok = False
            break

        out_std = solve(a,ops)

        if out_cpp != out_std:

            print(f"Test {tc+1}: WA")

            print("\nInput:")
            print(inp[:1000])

            print("\nExpected:")
            print("\n".join(out_std.split("\n")[:20]))

            print("\nGot:")
            print("\n".join(out_cpp.split("\n")[:20]))

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