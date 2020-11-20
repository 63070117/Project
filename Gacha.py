"""Gacha"""
import random
def main():
    box = []
    rate_box = []
    grade = []
    Get = []
    SR_box = []
    SR_rate = []
    SSR_box = []
    SSR_rate = []
    counter = 0
    garuntee = 0
    while True:         #นำเข้าข้อมูลของ gacha โดยให้กรอก: ชื่อitem เรท% ถ้ากรอบครบแล้วให้พิมพ์ END
        item, rate, tier = input("item:   "), input("rate%:   "), input("Tier:   ")#โดยที่ถ้าไม่สนใจของชิ้นไหนใน tier ให้รวม %ไปใน tier ได้เลย เช่น ตัวละครNo.1-->R แต่เราไม่สนใจให้รวมไปในเรท Rได้เลย
        if item == "ํEND" or rate == "END": #ถ้ากรอกจนครบแล้วให้ใส่คำว่า END
            break
        else: 
            if tier == "SR" or tier == "SSR":#ประกัน 10
                SR_box.append(item)
                SR_rate.append(float(rate))
                if tier == "SSR": #ประกันใหญ่
                    SSR_box.append(item)
                    SSR_rate.append(float(rate))                    
        box.append(item)
        rate_box.append(float(rate))
        grade.append(tier)
        
    print(box)
    #rate_option = input("การคำนวณเรท:")#ในกรณีที่มีประกัน ถ้าเปิด10ครั้งรวด = No หรือ สะสมครบ10ครั้ง = YES
    garuntee_option = int(input("มีประกันrollที่:"))#ไม่มีให้ใส่-1
    #pickup_option = input("ประกันหน้าตู้ไหม:")#ออกหน้าตู้แน่นอน = YES
    roll = int(input("open roll???:   "))
    for i in range(roll):
        counter += 1
        garuntee += 1
        if counter % 10 != 0:
            Get.append((random.choices(box, weights=rate_box, k=1)))
            if (random.choices(box, weights=rate_box, k=1)) in SSR_box:
                garuntee = 0 #ได้ SSR
        else:
            if garuntee == garuntee_option:
                Get.append((random.choices(SSR_box, weights=SSR_rate, k=1))) # สุ่ม SSR
                garuntee = 0 #ได้ SSR
            else:
                Get.append((random.choices(SR_box, weights=SR_rate, k=1))) # สุ่ม SR
                if (random.choices(SR_box, weights=SR_rate, k=1)) in SSR_box:
                    garuntee = 0 #ได้ SSR
    print(Get)
                    

    #print(random.choices(box, weights=rate_box, k=roll))
main()
