Dưới đây là file `README.md` cho hệ thống chấm tự động 9 bài C++.

```md
# 🚀 Auto Judge System - Competitive Programming

Hệ thống chấm tự động dành cho các bài lập trình C++.

Hệ thống hỗ trợ:

- Biên dịch code C++ tự động.
- Sinh test ngẫu nhiên.
- Chấm theo từng Subtask.
- Kiểm tra:
  - Compile Error
  - Runtime Error
  - Time Limit Exceeded
  - Wrong Answer
- Tính điểm từng bài.
- Tính điểm trung bình toàn bộ kỳ thi.


# ⚙️ Yêu cầu môi trường

## C++

Cần có:

```

g++

````

Kiểm tra:

```bash
g++ --version
````

Yêu cầu:

```
C++17
```

---

## Python

Phiên bản:

```
Python >= 3.8
```

Không cần thư viện ngoài.

---

# ▶️ Cách chạy

## Chấm toàn bộ 9 bài

Tại thư mục gốc:

```bash
python judge.py
```

Ví dụ:

```
============================================================

CHAM bai1

Subtask 1 Accepted +20
Subtask 2 Accepted +30
Subtask 3 Failed

FINAL SCORE: 50 /100


============================================================

KET QUA

Bai 1: 50/100
Bai 2: 100/100
Bai 3: 80/100
Bai 4: 100/100
Bai 5: 70/100
Bai 6: 100/100
Bai 7: 90/100
Bai 8: 60/100
Bai 9: 100/100


============================================================

DIEM TRUNG BINH: 85.56

```

---

# 📝 Cấu trúc một bài

Ví dụ:

```
bai1/

├── main.cpp
└── checker.py
```

---

## main.cpp

Code của thí sinh.

Ví dụ:

```cpp
#include <bits/stdc++.h>
using namespace std;


int main(){

    // solution

    return 0;
}
```

---

## checker.py

Bao gồm:

### 1. Compile

```python
g++ main.cpp -O2 -std=c++17
```

### 2. Generator

Sinh dữ liệu:

```python
def gen_test(sub):

    # tạo test

    return input
```

### 3. Official Solution

Ví dụ:

```python
def solve():

    # đáp án chuẩn

    return answer
```

### 4. Judge

Kiểm tra:

```python
if output_student == output_answer:

    AC

else:

    WA
```

---

# 📚 Danh sách bài thi

## Bài 1 - Segment Tree Sum

Chủ đề:

* Segment Tree
* Point Update
* Range Sum Query

---

## Bài 2 - RMQ Min

Chủ đề:

* Segment Tree
* Range Minimum Query

---

## Bài 3 - Chia đoạn tối ưu

Chủ đề:

* Binary Search Answer
* Greedy Check

---

## Bài 4 - Thống kê số nguyên tố

Chủ đề:

* Sieve of Eratosthenes

---

## Bài 5 - Closest Pair

Chủ đề:

* Computational Geometry
* Divide and Conquer

---

## Bài 6 - Quản lý bảng điểm

Chủ đề:

* Segment Tree Max

---

## Bài 7 - Maximum Subarray

Chủ đề:

* Segment Tree
* Kadane Algorithm

Node lưu:

```
sum
prefix
suffix
best
```

---

## Bài 8 - Dictionary

Chủ đề:

* Trie
* String Processing

Operations:

```
Insert
Delete
Prefix Query
```

---

## Bài 9 - Graph / DP / Advanced

Chủ đề:

* Graph Algorithm
* Dynamic Programming
* Data Structure

---

# 🎯 Cơ chế chấm điểm

Mỗi bài:

```
100 điểm
```

Tổng:

```
9 bài × 100 điểm
```

Điểm cuối:

[
Score =
\frac{Score_1+Score_2+...+Score_9}{9}
]

Ví dụ:

```
Bai1 = 80
Bai2 = 100
Bai3 = 70

Average = 83.33
```

---

# ⏱️ Time Limit

Mỗi test:

```python
TIME_LIMIT = 1.0
```

Nếu chạy quá:

```
TLE
```

---

# ❌ Các lỗi được phát hiện

| Lỗi                | Kết quả       |
| ------------------ | ------------- |
| Code không compile | Compile Error |
| Chương trình crash | Runtime Error |
| Chạy quá thời gian | TLE           |
| Sai output         | Wrong Answer  |
| Đúng               | Accepted      |

---

# 🧪 Sinh test

Generator hỗ trợ:

* Test nhỏ kiểm tra logic.
* Test trung bình kiểm tra tối ưu.
* Test lớn kiểm tra độ phức tạp.

Ví dụ:

```
Subtask 1:
N <= 1000


Subtask 2:
N <= 20000


Subtask 3:
N <= 200000
```

---

# 🔥 Mục tiêu

Framework phục vụ:

* Luyện thi học sinh giỏi Tin học.
* Thi Olympic Tin học.
* Chấm bài tự động lớp chuyên.
* Tạo Online Judge mini.

---

# 👨‍💻 Author

Competitive Programming Auto Judge Framework

Language:

* C++17
* Python 3

```

README này phù hợp để đưa lên GitHub cho bộ **9 đề thi thuật toán + hệ thống chấm tự động**.
```
