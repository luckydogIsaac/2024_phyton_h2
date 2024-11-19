import math 
r = float(input("請輸入圓的半徑: "))
if r >= 0: 
    area = r * r * 3.14 
    circumference = r * 2 * 3.14 
    print(f"圓的面積是: {area}") 
    print(f"圓的周長是: {circumference}") 
else:
    print("半徑不能是負數，請輸入一個非負的半徑。")
