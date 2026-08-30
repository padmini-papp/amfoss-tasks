import time
import random


def naive_multiply(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            total = 0
            for x in range(k):
                total += A[i][x] * B[x][j]
            result[i][j] = total

    return result


def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(n)]


def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(n)]


def split(M):
    n = len(M)
    mid = n // 2
    top_left = [row[:mid] for row in M[:mid]]
    top_right = [row[mid:] for row in M[:mid]]
    bottom_left = [row[:mid] for row in M[mid:]]
    bottom_right = [row[mid:] for row in M[mid:]]
    return top_left, top_right, bottom_left, bottom_right


def combine(c11, c12, c21, c22):
    top = [c11[i] + c12[i] for i in range(len(c11))]
    bottom = [c21[i] + c22[i] for i in range(len(c21))]
    return top + bottom


def divide_conquer_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    a11, a12, a21, a22 = split(A)
    b11, b12, b21, b22 = split(B)

    c11 = add_matrix(divide_conquer_multiply(a11, b11), divide_conquer_multiply(a12, b21))
    c12 = add_matrix(divide_conquer_multiply(a11, b12), divide_conquer_multiply(a12, b22))
    c21 = add_matrix(divide_conquer_multiply(a21, b11), divide_conquer_multiply(a22, b21))
    c22 = add_matrix(divide_conquer_multiply(a21, b12), divide_conquer_multiply(a22, b22))

    return combine(c11, c12, c21, c22)


def strassen_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    a11, a12, a21, a22 = split(A)
    b11, b12, b21, b22 = split(B)

    m1 = strassen_multiply(add_matrix(a11, a22), add_matrix(b11, b22))
    m2 = strassen_multiply(add_matrix(a21, a22), b11)
    m3 = strassen_multiply(a11, sub_matrix(b12, b22))
    m4 = strassen_multiply(a22, sub_matrix(b21, b11))
    m5 = strassen_multiply(add_matrix(a11, a12), b22)
    m6 = strassen_multiply(sub_matrix(a21, a11), add_matrix(b11, b12))
    m7 = strassen_multiply(sub_matrix(a12, a22), add_matrix(b21, b22))

    c11 = add_matrix(sub_matrix(add_matrix(m1, m4), m5), m7)
    c12 = add_matrix(m3, m5)
    c21 = add_matrix(m2, m4)
    c22 = add_matrix(sub_matrix(add_matrix(m1, m3), m2), m6)

    return combine(c11, c12, c21, c22)


def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]


def print_matrix(M):
    for row in M:
        print(row)


def main():
    n = int(input("Enter matrix size (power of 2, e.g. 2, 4, 8): "))

    A = generate_matrix(n)
    B = generate_matrix(n)

    print("\nMatrix A:")
    print_matrix(A)
    print("\nMatrix B:")
    print_matrix(B)

    start = time.time()
    result_naive = naive_multiply(A, B)
    naive_time = (time.time() - start) * 1000

    start = time.time()
    result_dc = divide_conquer_multiply(A, B)
    dc_time = (time.time() - start) * 1000

    start = time.time()
    result_strassen = strassen_multiply(A, B)
    strassen_time = (time.time() - start) * 1000

    print("\nMethod                     Time Taken")
    print("-" * 45)
    print(f"Naive Matrix Multiplication   {naive_time:.2f} ms")
    print(f"Divide and Conquer            {dc_time:.2f} ms")
    print(f"Strassen's Algorithm          {strassen_time:.2f} ms")

    verified = result_naive == result_dc == result_strassen
    print(f"\nVerification Status: {'PASSED' if verified else 'FAILED'}")

    times = {"Naive": naive_time, "Divide and Conquer": dc_time, "Strassen's Algorithm": strassen_time}
    fastest = min(times, key=times.get)
    print(f"Fastest Method: {fastest}")


if __name__ == "__main__":
    main()
