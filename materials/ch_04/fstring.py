pi = 3.1415
r = 999
area = pi * r * r
print('pi =', pi,)
print(f'pi = {pi}')
print(f'Area = pi * r * r = {pi} * {r} * {r} = {area}')
print('-' * 30)
print(f'Area = {area}')
print(f'Area = {area:.2f}')  # ทศนิยม 2 ตำแหน่ง
print(f'Area = {area:.0f}')  # ทศนิยม 0 ตำแหน่ง
print(f'Area = {area:.8f}')  # ทศนิยม 8 ตำแหน่ง
print(f'Area = {area:.8E}')  # รูปแบบเลขยกกำลัง
print(f'Radius = {r}')
print(f'Radius = {r:X}')