def 計算面積(高, 寬):
    return 高 * 寬

def main():
    h = float(input("請輸入矩形的高度: "))
    w = float(input("請輸入矩形的寬度: "))
    面積 = 計算面積(h, w)
    print(f"矩形的面積是: {面積}")

if __name__ == "__main__":
    main()
