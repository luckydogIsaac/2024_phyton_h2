
def time_to_minutes(hours, minutes):
    return hours * 60 + minutes


if __name__ == "__main__":
    
    a = int(input("輸入小時: "))
    b = int(input("輸入分鐘: "))
    
    
    x = time_to_minutes(a, b)
    print(f"總共是 {x} 分鐘")
