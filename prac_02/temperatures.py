# """
# CP1404/CP5632 - Practical
# Pseudocode for temperature conversion
# """
#
# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print(f"Result: {fahrenheit:.2f} F")
#     elif choice == "F":
#         fahrenheit = float(input("Fahrenheit: "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print(f"Result: {celsius:.2f} C")
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()

import numpy as np
import matplotlib.pyplot as plt

# 설정
np.random.seed(42)  # 재현 가능성 확보
n_experiments = 10000  # 실험 횟수
sample_size = 30  # 한 번 평균을 낼 때 샘플의 크기

# 원래 분포: 균등분포(정규분포 아님)
original_distribution = np.random.uniform(low=0.0, high=1.0, size=(n_experiments, sample_size))

# 각 샘플의 평균 계산
sample_means = original_distribution.mean(axis=1)

# 히스토그램 그리기
plt.figure(figsize=(10,6))
plt.hist(sample_means, bins=50, density=True, color='skyblue', edgecolor='black')
plt.title(f'중심극한정리 예시 (샘플 크기={sample_size}, 반복={n_experiments}회)')
plt.xlabel('샘플 평균')
plt.ylabel('밀도')
plt.grid(True)
plt.show()

