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

class Node:

    def __init__(self):

        self.child = {}
        self.pass_cnt = 0
        self.end_cnt = 0


def solve(operations):

    root = Node()

    ans = []

    # -----------------------------
    # Insert
    # -----------------------------
    def insert(word):

        cur = root
        cur.pass_cnt += 1

        for ch in word:

            if ch not in cur.child:
                cur.child[ch] = Node()

            cur = cur.child[ch]
            cur.pass_cnt += 1

        cur.end_cnt += 1

    # -----------------------------
    # Delete
    # -----------------------------
    def erase(word):

        cur = root

        path = [root]

        for ch in word:

            if ch not in cur.child:
                return

            cur = cur.child[ch]
            path.append(cur)

        if cur.end_cnt == 0:
            return

        cur.end_cnt -= 1

        for node in path:
            node.pass_cnt -= 1

    # -----------------------------
    # Query Prefix
    # -----------------------------
    def query(prefix):

        cur = root

        for ch in prefix:

            if ch not in cur.child:
                return 0

            cur = cur.child[ch]

        return cur.pass_cnt

    # -----------------------------
    # Process
    # -----------------------------
    for op in operations:

        t = op[0]

        if t == 1:

            insert(op[1])

        elif t == 2:

            erase(op[1])

        else:

            ans.append(str(query(op[1])))

    return "\n".join(ans)

# ==================================================
# TEST GENERATOR
# ==================================================

import string

def random_word(length):

    letters = string.ascii_lowercase

    return "".join(random.choice(letters) for _ in range(length))


import random
import string

def random_word(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def gen_test(sub):

    if sub == 1:

        q = random.randint(1, 5000)
        limit = 50000

    elif sub == 2:

        q = random.randint(50000, 100000)
        limit = 200000

    else:

        q = random.randint(150000, 200000)
        limit = 2000000

    operations = []

    dictionary = []

    total = 0

    while len(operations) < q:

        typ = random.randint(1, 3)

        # -----------------------
        # Insert
        # -----------------------
        if typ == 1 or len(dictionary) == 0:

            length = random.randint(1, 10)

            if total + length > limit:
                continue

            word = random_word(length)

            operations.append((1, word))

            dictionary.append(word)

            total += length

        # -----------------------
        # Delete
        # -----------------------
        elif typ == 2:

            word = random.choice(dictionary)

            operations.append((2, word))

            dictionary.remove(word)

            total += len(word)

        # -----------------------
        # Query Prefix
        # -----------------------
        else:

            if dictionary and random.randint(0, 1):

                word = random.choice(dictionary)

                prefix = word[:random.randint(1, len(word))]

            else:

                length = random.randint(1, 5)
                prefix = random_word(length)

            operations.append((3, prefix))

            total += len(prefix)

        if total >= limit:
            break

    return operations
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

        operations=gen_test(sub)

        inp=str(len(operations))+"\n"

        for op in operations:

            inp+=f"{op[0]} {op[1]}\n"

        out_cpp,runtime,status=run_cpp(inp)

        if status=="TLE":

            print(f"Test {tc+1}: TLE")

            ok=False
            break

        if status!="OK":

            print(status)

            ok=False
            break

        out_std=solve(operations)

        if out_cpp!=out_std:

            print(f"Test {tc+1}: WA")

            print("\n========== INPUT ==========")
            print(inp[:1000])

            print("\n========== EXPECTED ==========")
            print("\n".join(out_std.split("\n")[:20]))

            print("\n========== GOT ==========")
            print("\n".join(out_cpp.split("\n")[:20]))

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