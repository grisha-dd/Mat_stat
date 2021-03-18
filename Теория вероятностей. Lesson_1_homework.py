#!/usr/bin/env python
# coding: utf-8

# 1. Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
# 

# a) Найти вероятность того, что все карты – крести. 

# In[78]:


from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# In[79]:


clubs = 13
result = 4
r1 = combinations(clubs, result)
print (f"Число сочетаний крестей:  {r1}")


# In[80]:


totals = 52
r2 = combinations(totals, result)
print (f"Общее число исходов:  {r2}")


# In[81]:


p = r1/r2
print (f"вероятность того, что все карты – крести:  {p}")


# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# In[82]:


aces_totals = 4
aces_1 = combinations(aces_totals, 1)
aces_2 = combinations(aces_totals, 2)
aces_3 = combinations(aces_totals, 3)
aces_4 = combinations(aces_totals, 4)
print (f"Один туз - число сочетаний :  {aces_1}")
print (f"Два туза - число сочетаний :  {aces_2}")
print (f"Три туза - число сочетаний :  {aces_3}")


# In[83]:


others_totals = 48
other_1 = combinations(others_totals, 3)
other_2 = combinations(others_totals, 2)
other_3 = combinations(others_totals, 1)
print (f"Число сочетаний остальных карт при 1 тузе:  {other_1}")
print (f"Число сочетаний остальных карт при 2 тузах:  {other_2}")
print (f"Число сочетаний остальных карт при 3 тузах:  {other_3}")


# In[84]:


P1 = (aces_1 * other_1)/r2
P2 = (aces_2 * other_2)/r2
P3 = (aces_3 * other_3)/r2
P4 = 1/r2
print (f"Вероятность, что окажется 1 туз: {P1}")
print (f"Вероятность, что окажется 2 туза: {P2}")
print (f"Вероятность, что окажется 3 туза: {P3}")
print (f"Вероятность, что окажется 4 туза: {P4}")
print(f"Вероятность, что среди 4-х карт окажется хотя бы один туз: {P1+P2+P3+P4}")


# 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# In[85]:


all_buttons = 10
code = 3

variants = combinations(all_buttons, code)

print (f"Число возможных кодов:  {r1}")


# In[76]:


P_code = 1/variants
print (f"Вероятность того, что человек, не знающий код, откроет дверь с первой попытки:  {P_code}")


# 3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?
# 

# In[74]:


from numpy import prod

total_details = 15
colored_details = 9
result_details = 3

k = 0
P_final = []

while k < result_details:
    P = (colored_details - k)/(total_details - k)
    k += 1
    print (f"Вероятность того, что {k} деталь окрашена:  {P}")
    P_final.append(P)
    
print (f"Вероятность того,  что все извлеченные детали окрашены:  {prod(P_final)}")   

    


# 4. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# In[62]:


P_loto = 2/100*1/99
print(P_loto)


# In[ ]:




