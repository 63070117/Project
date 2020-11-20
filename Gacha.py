"""Gacha"""
import random
def main():
    box = []
    rate_box = []
    while True:         #นำเข้าข้อมูลของ gacha โดยให้กรอก: ชื่อitem เรท% ถ้ากรอบครบแล้วให้พิมพ์ END
        item, rate = input("item:   "), input("rate%:   ")
        if item == "ํEND" or rate == "END":
            break
        box.append(item)
        rate_box.append(float(rate))
    print(box)

    roll = int(input("open roll???:   "))
    print(random.choices(box, weights=rate_box, k=roll))
main()
