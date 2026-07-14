import os
import shutil
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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


class JudgeGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Automatic C++ Judge")
        self.root.geometry("900x650")

        top = tk.Frame(self.root)
        top.pack(fill="x", pady=10)

        tk.Label(
            top,
            text="Bài:"
        ).pack(side="left", padx=5)

        self.problem = ttk.Combobox(
            top,
            values=["All"] + PROBLEMS,
            state="readonly",
            width=15
        )

        self.problem.current(0)
        self.problem.pack(side="left")

        tk.Button(
            top,
            text="Chọn file C++",
            command=self.choose_file
        ).pack(side="left", padx=10)

        tk.Button(
            top,
            text="Chấm",
            command=self.judge
        ).pack(side="left")

        self.file_label = tk.Label(
            self.root,
            text="Chưa chọn file"
        )

        self.file_label.pack()

        self.output = scrolledtext.ScrolledText(
            self.root,
            font=("Consolas",10)
        )

        self.output.pack(fill="both", expand=True, padx=10, pady=10)

        self.cpp_file = None

        self.root.mainloop()

    def log(self, text):

        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)
        self.root.update()

    def choose_file(self):

        path = filedialog.askopenfilename(
            filetypes=[("C++","*.cpp")]
        )

        if path:

            self.cpp_file = path
            self.file_label.config(text=path)

    def run_checker(self, problem):

        folder = os.path.join(BASE_DIR, problem)

        checker = os.path.join(folder, "checker.py")

        if not os.path.exists(checker):

            self.log(f"{problem}: Missing checker")
            return 0

        shutil.copy(
            self.cpp_file,
            os.path.join(folder, "main.cpp")
        )

        result = subprocess.run(
            ["python3", checker],
            cwd=folder,
            capture_output=True,
            text=True
        )

        self.log("=" * 60)
        self.log(problem.upper())
        self.log(result.stdout)

        score = 0

        for line in result.stdout.split("\n"):

            if "FINAL SCORE" in line:

                try:
                    score = int(
                        line.split(":")[1]
                        .split("/")[0]
                        .strip()
                    )
                except:
                    pass

        return score

    def judge(self):

        if self.cpp_file is None:

            messagebox.showerror(
                "Lỗi",
                "Hãy chọn file C++."
            )
            return

        self.output.delete("1.0", tk.END)

        scores = []

        if self.problem.get() == "All":

            for p in PROBLEMS:

                score = self.run_checker(p)
                scores.append(score)

            self.log("=" * 60)

            self.log("KẾT QUẢ")

            for i, s in enumerate(scores):

                self.log(f"{PROBLEMS[i]} : {s}/100")

            avg = sum(scores) / len(scores)

            self.log("=" * 60)
            self.log(f"ĐIỂM TRUNG BÌNH : {avg:.2f}")

        else:

            score = self.run_checker(self.problem.get())

            self.log("=" * 60)
            self.log(f"Điểm: {score}/100")


JudgeGUI()