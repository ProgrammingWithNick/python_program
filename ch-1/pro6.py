# 6. Histogram Function
print("="*50)
print("PROGRAM 6: HISTOGRAM")
print("="*50)

def histogram(lst):
    for num in lst:
        print('*' * num)

test_list = [4, 9, 7]
print(f"Histogram for {test_list}:")
histogram(test_list)
print()