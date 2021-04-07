"""Faktorial hisoblash"""
def faktorial(x):
    try:
        x = int(x)
        result = 1
        for i in range(1, x+1):
            result = result * i
        return result
    except ValueError:
        return "Faktorial raqamlar orqali hisoblanadi so'zlar yoki maxsus belgilar bilan emas"
# print(faktorial("4r"))



"""Fibonachi sonlari"""
def fibo_son(n):
    try:
        n = int(n)
        fib_list = [0, 1]
        # sonlar = []
        while fib_list[-1] < n:
            fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list
    except ValueError:
        return "So'zlar yoki maxsus belgilar Fibonachi sonlari hisoblanmaydi"
# print(fibo_son("25q"))


"""Arab raqamidan rim raqamiga o'tish"""
def int_to_roman(input):
    try:
        input = int(input)
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = " "
        for i in range(len(ints)):
            count = int(input / ints[i])
            result += nums[i] * count
            input -= ints[i] * count
        return result
    except ValueError:
        return "Arab raqanlari kundalik ishlatadigan raqamlarimiz harf yoki belgilar emas"
# print(int_to_roman(34))


"""Rim raqamidan arab raqamiga o'tish"""
def roman_to_int(s):
    try:
        s = str(s)
        s = s.upper()
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - (2 * rom_val[s[i - 1]])
            else:
                int_val += rom_val[s[i]]
        return int_val
    except AttributeError:
        return "Siz rim raqami kiritmadingiz! AttributeError"
    except KeyError:
        return "Maxsus belgilar rim raqami hisoblanmaydi! KeyError"
    except TypeError:
        return "Boshqa turdagi belgi kiritdingiz! TypeError"
# print(roman_to_int("w"))


"""telefon, mobil operatorlarni tekshirish"""
def mobil_operator(raqami):
    try:
        baza = {
            33: "Humans",
            71: "TashTT",
            90: "Beeline",
            91: "Beeline",
            93: "Ucell",
            94: "Ucell",
            99: "Uzmobile",
            88: "Mobiuz",
            97: "Mobiuz",
            98: "Perfectum"
        }
        return baza[int(str(raqami)[3:5])]
    except KeyError:
        return "Siz mavjud bo'lmagan operator kodini jo'natdingiz"
    except ValueError:
        return "Operator kodi raqamlardan iborat, iltimos raqam kiriting"
# print(mobil_operator("fe"))


"""kiritilgan matnni teskari yozib beruvchi funksiya"""
def teskariMatn(text):
    try:
        text = str(text)
        result = ""
        for i in text:
            result = i + result
        return result
    except SyntaxError:
        return "Siz maxsus belgi kiritdingiz"

# print(teskariMatn(5553))


"""Paskal uchburchagi"""
def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]
# pascal_triangle(4)

