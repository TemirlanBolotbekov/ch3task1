#Попросить пользователя ввести текст. В результате вывести процент букв в верхнем
#регистре (заглавные) и в нижнем регистре (прописные).

# text = (input("Type your text :"))

s = input("Type to text :")
let_s = 0
let_b = 0
for i in s:
    if 'a' <= i <= 'z':
        let_s += 1
    else:
        if 'A' <= i <= 'Z':
            let_b += 1
print(let_s)
print(let_b)
