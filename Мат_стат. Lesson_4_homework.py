#!/usr/bin/env python
# coding: utf-8

# 1. Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
# 
# 

# In[57]:


a = 200
b = 800
M = (a + b)/2
print (f"среднее значение {M}")


# In[58]:


a = 200
b = 800
D = (b-a)**2/12
print (f" дисперсия {D}")


# 2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.
# 

# D(X)= (b-a)**2/12
# 
# D(X) = 0.2
# 
# a = 0.5
# 
# (b-0.5)**2/12 = 0.2
# 
# (b**2 - 0.5b + 0.25)/ 12 = 0.2 
# 
# (b**2 - b + 0.25) = 2.4
# 
# b1, b2 = -1.04919, 2.04919

# In[61]:


a = 0.5
b = 2.04919
print(f"Правая границя величины B равна {b}")

M = (a + b)/2
print (f"среднее значение {M}")

D = (b-a)**2/12
print (f"check дисперсия {D}")


# 3. Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# 
# f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-((x+2)***2) / 32))
# 
# Найдите:
# 
# а). M(X)
# 
# б). D(X)
# 
# в). std(X) (среднее квадратичное отклонение)
# 

# $f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e ^ {- \frac{(x - a)^2}{2 \sigma^2}}$
# 

# $а) \; a = M(X) = -2$ 
#  
# $б) \; \sigma^2 = D(X) = 16$
# 
# $в) \; std(X) = \sigma =  4 $

# 4. Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.
# 

# In[5]:


mu = 174
std = 8 


# In[40]:


a = 182
Z = (a - mu)/std

print( f"  а). больше 182 см :\n Z = {Z}, по правилу трёх сигм - (100-68)/2 = {(100-68)/2}%, по таблице -  P = 15.866% ")


# In[41]:


a = 190
Z = (a - mu)/std

print( f"   б). больше 190 см :\n Z = {Z}, по правилу трёх сигм - (100-95.4)/2 = {(100-95.4)/2}%, по таблице - P = 2.275% ")


# In[42]:


a1 = 166
Z1 = (a1 - mu)/std
print(f" a1 = {a1}\n Z = {Z1}")
a2 = 190
Z2 = (a2 - mu)/std
print(f" a2 = {a2}\n Z = {Z2}")

print( f"   в). от 166 см до 190 см:\n по правилу трёх сигм  68 +(95.4-68)/2 = {68 +(95.4-68)/2}%, по таблице - P = 97.72% - 15.87% =  {97.72 - 15.87} % ")


# In[43]:


a1 = 166
Z1 = (a1 - mu)/std
print(f" a1 = {a1}\n Z = {Z1}")
a2 = 182
Z2 = (a2 - mu)/std
print(f" a2 = {a2}\n Z = {Z2}")
print( f"   г). от 166 см до 182 см:\n по правилу трёх сигм около 68%, по таблице - P = 84.13% - 15.87% =  {84.13 - 15.87} % ")


# In[44]:


a1 = 158
Z1 = (a1 - mu)/std
print(f" a1 = {a1}\n Z = {Z1}")
a2 = 190
Z2 = (a2 - mu)/std
print(f" a2 = {a2}\n Z = {Z2}")
print( f"   д). от 158 см до 190 см:\n по правилу трёх сигм около 95.4%, по таблице - P = 97.72% - 2.28% =  {97.72 - 2.28} % ")


# In[46]:


a1 = 150
Z1 = (a1 - mu)/std
print(f" a1 = {a1}\n Z = {Z1}")
a2 = 190
Z2 = (a2 - mu)/std
print(f" a2 = {a2}\n Z = {Z2}")
print( f"   е). не выше 150 см или не ниже 190 см:\n по правилу трёх сигм (100-99.72)/2 +(100-95.4)/2 = {(100-99.72)/2 +(100-95.4)/2}%, по таблице - P = 0.13% + 2.28% =  {0.13 + 2.28} % ")


# In[38]:


a1 = 150
Z1 = (a1 - mu)/std
print(f" a1 = {a1}\n Z = {Z1}")
a2 = 198
Z2 = (a2 - mu)/std
print(f" a2 = {a2}\n Z = {Z2}")
print( f"ё). не выше 150 см или не ниже 198 см:\n по правилу трёх сигм  (100-99.72) = {100-99.72}%, по таблице - P = 0.13% + 0.13% =  {0.13 + 0.13} % ")


# In[48]:


a = 166
Z = (a - mu)/std

print( f"  ж). ниже 166 см :\n Z = {Z},  по правилу трёх сигм около (100-68)/2 = {(100-68)/2}%, по таблице - P = 15.87% ")


# 5. На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

# In[50]:


Z = (190 - 178)/5
Z

