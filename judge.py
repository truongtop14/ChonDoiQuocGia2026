import os
import subprocess


PROBLEMS = [

    "bai1",
    "bai2",
    "bai3",
    "bai4",
    "bai5",
    "bai6",
    "bai7",
    "bai8",
    "bai9"

]


scores=[]



for p in PROBLEMS:


    print("="*60)

    print("CHAM",p)



    path=f"{p}/checker.py"


    if not os.path.exists(path):

        print("Missing checker")

        scores.append(0)

        continue



    result=subprocess.run(

        [
            "python3",
            path
        ],

        capture_output=True,

        text=True

    )


    print(result.stdout)



    score=0


    # đọc dòng FINAL SCORE

    for line in result.stdout.split("\n"):


        if "FINAL SCORE" in line:

            try:

                score=int(
                    line.split(":")[1]
                    .split("/")[0]
                    .strip()
                )

            except:

                score=0



    scores.append(score)



print("\n")
print("="*60)

print("KET QUA")

print("="*60)



for i,s in enumerate(scores):

    print(
        f"Bai {i+1}: {s}/100"
    )



avg=sum(scores)/len(scores)



print("="*60)

print(
    f"DIEM TRUNG BINH: {avg:.2f}"
)


print("="*60)