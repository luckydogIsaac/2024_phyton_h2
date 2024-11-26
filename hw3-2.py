def find_max(a, b):
    if a > b:
        return a
    else:
        return b

def main():
    
    num1 = float(input("請輸入第一個數: "))
    num2 = float(input("請輸入第二個數: "))

    max_num = find_max(num1, num2)

    print(f"兩個數中的最大值是: {max_num}")


if __name__ == "__main__":
    main()
