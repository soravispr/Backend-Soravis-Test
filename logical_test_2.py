
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

# Written by Soravis Prommas 01/20/2023

def convert_to_roman(arabic_num):
    M = int(arabic_num / 1000)
    CM = int((arabic_num - (M*1000)) / 900)
    D = int((arabic_num - (M*1000) - (CM*900)) / 500)
    CD = int((arabic_num - (M*1000) - (CM*900) - (D*500)) / 400)
    C = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400)) / 100)
    XC = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100)) / 90)
    L = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100) - (XC*90)) / 50)
    XL = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100) - (XC*90) - (L*50)) / 40)
    X = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100) - (XC*90) - (L*50) - (XL*40)) / 10)
    IX = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100) - (XC*90) - (L*50) - (XL*40) - (X*10)) / 9)
    V = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100) - (XC*90) - (L*50) - (XL*40) - (X*10) - (IX*9)) / 5)
    IV = int((arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100) - (XC*90) - (L*50) - (XL*40) - (X*10) - (IX*9) - (V*5)) / 4)
    I = arabic_num - (M*1000) - (CM*900) - (D*500) - (CD*400) - (C*100) - (XC*90) - (L*50) - (XL*40) - (X*10) - (IX*9) - (V*5) - (IV*4)

    roman_num = ''

    if M > 0:
        for m in range(M):
            roman_num += 'M'
    
    if CM > 0:
        for cm in range(CM):
            roman_num += 'CM'
    
    if D > 0:
        for d in range(D):
            roman_num += 'D'
    
    if CD > 0:
        for cd in range(CD):
            roman_num += 'CD'
    
    if C > 0:
        for c in range(C):
            roman_num += 'C'
    
    if XC > 0:
        for xc in range(XC):
            roman_num += 'XC'
    
    if L > 0:
        for l in range(L):
            roman_num += 'L'
    
    if XL > 0:
        for xl in range(XL):
            roman_num += 'XL'
    
    if X > 0:
        for x in range(X):
            roman_num += 'X'
    
    if IX > 0:
        for ix in range(IX):
            roman_num += 'IX'
    
    if V > 0:
        for m in range(V):
            roman_num += 'V'
    
    if IV > 0:
        for iv in range(IV):
            roman_num += 'IV'
    
    if I > 0:
        for i in range(I):
            roman_num += 'I'
    
    return roman_num


roman_num = convert_to_roman(940)
print(roman_num)
