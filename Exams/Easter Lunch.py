couzinaci = int(input())
eggs = int(input())
cookies = int(input())

price_couzunaci = couzinaci * 3.2
price_eggs = eggs * 4.35
price_cookies = cookies * 5.4
price_boq = 0.15 * eggs * 12

total = price_boq + price_eggs + price_couzunaci + price_cookies

print(F'{total:.2f}')