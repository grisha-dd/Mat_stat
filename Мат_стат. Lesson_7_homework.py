#!/usr/bin/env python
# coding: utf-8

# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks): zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. Используя математические операции, посчитать коэффициенты линейной регрессии, приняв за X заработную плату (то есть, zp - признак), а за y - значения скорингового балла (то есть, ks - целевая переменная). Произвести расчет как с использованием intercept, так и без.
# 

# Расчет с использованием intercept

# In[22]:


import numpy as np
X_zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
Y_ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(Y_ks)
n


# In[7]:


b = (np.mean(X_zp * Y_ks)- np.mean(X_zp)*np.mean(Y_ks))/(np.mean(X_zp**2) - np.mean(X_zp)**2)
b


# In[9]:


b_2 = (n * (np.sum(X_zp * Y_ks)) - (np.sum(Y_ks) * np.sum(X_zp))) /( n * (np.sum(X_zp**2)) - ((np.sum(X_zp)**2)))
b_2


# In[10]:


a = np.mean(Y_ks) - b * np.mean(X_zp)
a


# In[14]:


y_hat = a + b*X_zp
y_hat


# In[20]:


import matplotlib.pyplot as plt

plt.scatter(X_zp, Y_ks)
plt.plot (X_zp, y_hat)
plt.show()


# In[97]:


print(f"y = {a} + {b}*x")


# Расчет без использования intercept. Матричный метод

# In[23]:


import seaborn as sns


# In[24]:


X = X_zp.reshape((n,1))
X


# In[25]:


Y = Y_ks.reshape((n,1))
Y


# In[27]:


B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T@Y)
B


# In[91]:


Y_hat = B*X
Y_hat


# In[57]:


plt.scatter(X_zp, Y_ks)
plt.plot (X_zp, Y_hat)
plt.show()


# In[99]:


print(f"y = 5.88982042 * x")


# 2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
# 

# In[42]:


def mse_(B1, y=Y_ks, X=X_zp, n=10):
    return np.sum((B1*X-y)**2)/n


# In[106]:


alpha = 1e-6
alpha


# In[107]:


B1 = 0.1


# In[108]:


for i in range (2000):
    B1 -= alpha * (2/n) * np.sum((B1*X_zp-Y_ks)*X_zp)
    if i%200==0:
        print(f"Iteration: {i}, B1 = {B1}, mse= {mse_(B1)}")


# In[62]:


B1 = 5.889820420132673
B1


# 3. (необязательная)Произвести вычисления как в пункте 2, но с вычислением intercept. Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

# In[117]:


def mse_(B0, B1, y=Y_ks, X=X_zp, n=10):
    return np.sum((B0 + B1*X-y)**2)/n


# In[142]:


alpha = 1e-5
alpha


# In[143]:


B0 = 0.1
B1 = 0.1


# In[150]:


for i in range (700000):
    B0 -= alpha * (2/n) * np.sum(B0 + B1*X_zp-Y_ks)
    B1 -= alpha * (2/n) * np.sum((B0 + B1*X_zp-Y_ks)*X_zp)
    if i%100000==0:
        print(f"Iteration: {i},B0 = {B0}, B1 = {B1}, mse= {mse_(B0, B1)}")


# In[154]:


print(f"B0 = 444.1774 \nB1 = 2.62054")

