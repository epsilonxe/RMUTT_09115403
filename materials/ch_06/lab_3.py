# เงินต้น 100000 บาท
# ผ่อนชำระ 12 เดือน
# อัตราดอกเบี้ยร้อยละ 3 ต่อเดือน

# ดอกเบี้ย = เงินต้น * อัตราดอกเบี้ย * จำนวนเดือน
# ดอกเบี้ย = 100000 * (3/100) * 12 = 36000
# ยอดหนี้รวม = เงินต้น + ดอกเบี้ย = 100000 + 36000 = 136000
# ยอดผ่อนชำระต่อเดือน = ยอดหนี้รวม / จำนวนเดือน
# ยอดผ่อนชำระต่อเดือน = 136000 / 12 = 11333.34

deposit = float(input('Enter the deposit: '))
month = int(input('Enter the duration (month): '))

choice = [12, 24, 36]

if month in choice:
    if month == 12:
        int_rate = 0.01
    elif month == 24:
        int_rate = 0.015
    elif month == 36:
        int_rate = 0.025
        
    total_int = deposit * int_rate * month
    debt = deposit + total_int
    pay_per_month = debt / month
    print(f'Pay {pay_per_month:.2f} Baht/month')
else:
    print('ERROR: MONTH MUST BE 12, 24 OR 36')
