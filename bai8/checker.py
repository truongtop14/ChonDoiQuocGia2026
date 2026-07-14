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

print("="*60)
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

    print(ret.stderr)

    exit()


print("Compile Success!")



# ==================================================
# SOLUTION BRUTE FORCE
# ==================================================
# ==================================================
# SEGMENT TREE SOLUTION
# ==================================================

NEG_INF = -10**18


class Node:

    def __init__(self):

        self.sum = 0
        self.pref = NEG_INF
        self.suff = NEG_INF
        self.best = NEG_INF



def merge(left, right):

    res = Node()


    # tổng đoạn

    res.sum = left.sum + right.sum


    # prefix lớn nhất

    res.pref = max(
        left.pref,
        left.sum + right.pref
    )


    # suffix lớn nhất

    res.suff = max(
        right.suff,
        right.sum + left.suff
    )


    # đáp án lớn nhất

    res.best = max(
        left.best,
        right.best,
        left.suff + right.pref
    )


    return res



def make_node(x):

    node = Node()

    node.sum = x

    node.pref = x

    node.suff = x

    node.best = x

    return node



def build(id,l,r,st,a):


    if l==r:

        st[id]=make_node(a[l])

        return



    mid=(l+r)//2


    build(
        id*2,
        l,
        mid,
        st,
        a
    )


    build(
        id*2+1,
        mid+1,
        r,
        st,
        a
    )


    st[id]=merge(
        st[id*2],
        st[id*2+1]
    )




def update(id,l,r,pos,val,st):


    if l==r:

        st[id]=make_node(val)

        return



    mid=(l+r)//2


    if pos<=mid:

        update(
            id*2,
            l,
            mid,
            pos,
            val,
            st
        )

    else:

        update(
            id*2+1,
            mid+1,
            r,
            pos,
            val,
            st
        )


    st[id]=merge(
        st[id*2],
        st[id*2+1]
    )




def query(id,l,r,u,v,st):


    if r<u or v<l:

        return None



    if u<=l and r<=v:

        return st[id]



    mid=(l+r)//2


    left=query(
        id*2,
        l,
        mid,
        u,
        v,
        st
    )


    right=query(
        id*2+1,
        mid+1,
        r,
        u,
        v,
        st
    )



    if left is None:

        return right


    if right is None:

        return left



    return merge(
        left,
        right
    )




def solve(a, operations):


    n=len(a)-1


    st=[None]*(4*n+5)



    build(
        1,
        1,
        n,
        st,
        a
    )


    ans=[]



    for op in operations:


        if op[0]==1:


            _,i,x=op


            update(
                1,
                1,
                n,
                i,
                x,
                st
            )



        else:


            _,l,r=op


            res=query(
                1,
                1,
                n,
                l,
                r,
                st
            )


            ans.append(
                str(res.best)
            )



    return "\n".join(ans)
# ==================================================
# TEST GENERATOR
# ==================================================

def gen_test(sub):


    # --------------------------
    # Subtask 1
    # --------------------------

    if sub == 1:

        n = random.randint(1,1000)

        q = random.randint(1,1000)


    # --------------------------
    # Subtask 2
    # --------------------------

    elif sub == 2:

        n = random.randint(5000,20000)

        q = random.randint(5000,20000)



    # --------------------------
    # Subtask 3
    # --------------------------

    else:

        n = random.randint(100000,200000)

        q = random.randint(100000,200000)



    # sinh mảng

    a = [0]


    for i in range(n):

        a.append(
            random.randint(
                -10**9,
                10**9
            )
        )



    operations=[]


    for _ in range(q):


        # 50% update
        # 50% query


        if random.randint(0,1)==0:


            i=random.randint(1,n)

            x=random.randint(
                -10**9,
                10**9
            )


            operations.append(
                (1,i,x)
            )



        else:


            l=random.randint(
                1,n
            )

            r=random.randint(
                l,n
            )


            operations.append(
                (2,l,r)
            )



    return n,q,a,operations



# ==================================================
# RUN CPP
# ==================================================

def run_cpp(inp):


    with open("input.txt","w") as f:

        f.write(inp)



    start=time.perf_counter()


    try:


        with open("input.txt") as fin, \
             open("output.txt","w") as fout:


            subprocess.run(

                [EXE_FILE],

                stdin=fin,

                stdout=fout,

                stderr=subprocess.PIPE,

                timeout=TIME_LIMIT

            )



        runtime=time.perf_counter()-start



        with open("output.txt") as f:

            out=f.read().strip()



        return out,runtime,"OK"



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


        n,q,a,operations = gen_test(sub)



        # tạo input

        inp=f"{n} {q}\n"


        inp+=" ".join(
            map(str,a[1:])
        )

        inp+="\n"



        for op in operations:


            if op[0]==1:


                inp+=f"1 {op[1]} {op[2]}\n"


            else:


                inp+=f"2 {op[1]} {op[2]}\n"




        out_cpp,runtime,status = run_cpp(inp)



        if status=="TLE":


            print(
                f"Test {tc+1}: TLE"
            )

            ok=False

            break




        out_std=solve(
            a,
            operations
        )



        if out_cpp != out_std:



            print(
                f"Test {tc+1}: WA"
            )


            print("\nInput:")
            print(inp[:2000])


            print("\nExpected:")
            print(out_std[:1000])


            print("\nGot:")
            print(out_cpp[:1000])


            ok=False

            break



        print(
            f"Test {tc+1}: AC ({runtime:.4f}s)"
        )




    if ok:


        score += SUBTASK_SCORE[sub]


        print(
            f"Subtask {sub}: Accepted +{SUBTASK_SCORE[sub]}"
        )


    else:


        print(
            f"Subtask {sub}: Failed"
        )



print("\n"+"="*60)

print(
    "FINAL SCORE:",
    score,
    "/100"
)

print("="*60)