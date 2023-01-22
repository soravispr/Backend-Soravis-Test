
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

# Written by Soravis Prommas 01/20/2023

def convert_to_text(number):
    num_dict = { 0: 'ศูนย์', 1: 'หนึ่ง', 2: 'สอง', 3: 'สาม', 4: 'สี่', 5: 'ห้า', 6: 'หก', 7: 'เจ็ด', 8: 'แปด', 9: 'เก้า', 10: 'สิบ'}

    million = int(number / 1000000)
    hundred_thousand = int((number - (million*1000000)) / 100000)
    ten_thousand = int((number - (million*1000000) - (hundred_thousand*100000)) / 10000)
    thousand = int((number - (million*1000000) - (hundred_thousand*100000) - (ten_thousand*10000)) / 1000)
    hundred = int((number - (million*1000000) - (hundred_thousand*100000) - (ten_thousand*10000) - (thousand*1000)) / 100)
    ten = int((number - (million*1000000) - (hundred_thousand*100000) - (ten_thousand*10000) - (thousand*1000) - (hundred*100)) / 10)
    one = int(number - (million*1000000) - (hundred_thousand*100000) - (ten_thousand*10000) - (thousand*1000) - (hundred*100) - (ten*10))

    txt = ''

    if million > 0:
        txt += num_dict[million] + 'ล้าน'
    
    if hundred_thousand > 0:
        txt += num_dict[hundred_thousand] + 'แสน'
    
    if ten_thousand > 0:
        txt += num_dict[ten_thousand] + 'หมื่น'
    
    if thousand > 0:
        txt += num_dict[thousand] + 'พัน'
    
    if hundred > 0:
        txt += num_dict[hundred] + 'ร้อย'
    
    if ten > 0:
        if ten == 2:
            txt += 'ยี่สิบ'
        elif ten == 1:
            txt += 'สิบ'
        else:
            txt += num_dict[ten] + 'สิบ'
    
    if one > 0:
        if ten > 0 and one == 1:
            txt += 'เอ็ด'
        else:
            txt += num_dict[one]
    
    return txt

txt = convert_to_text(223425)
print(txt)