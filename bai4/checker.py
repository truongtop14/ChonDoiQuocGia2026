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
# OFFICIAL SOLUTION
# Binary Search + Greedy
# ==================================================

def check(a, k, limit):

    cnt = 1
    cur = 0

    for x in a:

        if cur + x <= limit:

            cur += x

        else:

            cnt += 1
            cur = x

            if cnt > k:
                return False

    return True


def solve(a, k):

    left = max(a)
    right = sum(a)

    ans = right

    while left <= right:

        mid = (left + right) // 2

        if check(a, k, mid):

            ans = mid
            right = mid - 1

        else:

            left = mid + 1

    return ans

# ==================================================
# TEST GENERATOR
# ==================================================

def gen_test(sub):

    if sub == 1:

        n = random.randint(1,20)

    elif sub == 2:

        n = random.randint(1000,2000)

    else:

        n = random.randint(100000,200000)

    k = random.randint(1,n)

    a = []

    for _ in range(n):

        if sub == 3:
            a.append(random.randint(1,10**9))
        else:
            a.append(random.randint(1,1000))

    return n,k,a

# ==================================================
# RUN CPP
# ==================================================

def run_cpp(inp):

    with open("input.txt","w") as f:
        f.write(inp)

    start = time.perf_counter()

    try:

        with open("input.txt") as fin,\
             open("output.txt","w") as fout:

            subprocess.run(
                [EXE_FILE],
                stdin=fin,
                stdout=fout,
                stderr=subprocess.PIPE,
                timeout=TIME_LIMIT
            )

        elapsed = time.perf_counter()-start

        with open("output.txt") as f:
            out=f.read().strip()

        return out,elapsed,"OK"

    except subprocess.TimeoutExpired:

        return "",TIME_LIMIT,"TLE"

    except Exception as e:

        return "",0,str(e)

# ==================================================
# JUDGE
# ==================================================

SUBTASK_SCORE={
    1:20,
    2:30,
    3:50
}

score=0

for sub in [1,2,3]:

    print("\n"+"="*60)
    print("Subtask",sub)

    ok=True

    for tc in range(TEST_PER_SUBTASK):

        n,k,a=gen_test(sub)

        inp=f"{n} {k}\n"
        inp+=" ".join(map(str,a))+"\n"

        out_cpp,runtime,status=run_cpp(inp)

        if status=="TLE":

            print(f"Test {tc+1}: TLE")
            ok=False
            break

        if status!="OK":

            print(status)
            ok=False
            break

        out_std=str(solve(a,k))

        if out_cpp!=out_std:

            print(f"Test {tc+1}: WA")

            print("\nInput:")
            print(inp[:1000])

            print("\nExpected:",out_std)
            print("Got     :",out_cpp)

            ok=False
            break

        print(f"Test {tc+1}: AC ({runtime:.4f}s)")

    if ok:

        score+=SUBTASK_SCORE[sub]

        print(f"Subtask {sub}: Accepted (+{SUBTASK_SCORE[sub]} điểm)")

    else:

        print(f"Subtask {sub}: Failed")

print("\n"+"="*60)
print("FINAL SCORE:",score,"/100")
print("="*60)