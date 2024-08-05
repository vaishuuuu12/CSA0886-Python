n = 3
gray_codes = ['0', '1']
for i in range(1, n):
    reflected = gray_codes[::-1]
    for j in range(len(gray_codes)):
        gray_codes[j] = '0' + gray_codes[j]
    for j in range(len(reflected)):
        reflected[j] = '1' + reflected[j]
    gray_codes += reflected
for code in gray_codes:
    print(code)
