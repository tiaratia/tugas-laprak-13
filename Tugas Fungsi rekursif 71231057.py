#!/usr/bin/env python
# coding: utf-8

# In[1]:


# soal pertama 
def cek_prima(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        return cek_prima(n-1)

bilangan = int(input(" Masukka Bilangan Yang Ingin Dicek: "))
if cek_prima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")


# In[8]:


#soal ke dua 
def palidromeAsik(s,b):
    if len(s)== b :
        s = ''.join(e for e in s if e. isalnum())
    #base case 
    if len(s) < 1 :
        return True 
    # recurssion case
    else:
        if s[0] == s [-1]:
            return palidromeAsik(s[1:-1], b)
        else:
            return False 
kalimat = input("Masukkan kalimat yang ingin dicek: ")
if cek_palindrom(kalimat):
    print(f"{kalimat} adalah palindrom.")
else:
    print(f"{kalimat} bukan palindrom.")


# In[ ]:


# soal ke 3
def jumlah_deret_ganjil(n):
    if n % 0:
        return 0
    else:
        return n + jumlah_deret_ganjil(n-2)

n = int(input("Masukkan nilai n: "))
print(f"Jumlah deret ganjil dari 1 + 3 + 7 + ... + {n} adalah {jumlah_deret_ganjil(n)}")



# In[4]:


# soal ke empat 
def jumlah_digit(bilangan):
    if bilangan <= 10:
        return bilangan
    else:
        return bilangan % 10 + jumlah_digit(bilangan // 10)

bilangan = int(input("Masukkan bilangan yang ingin dicek: "))
print(f"Jumlah digit dari {bilangan} adalah {jumlah_digit(bilangan)}")


# In[8]:


# soal yang ke 5 
def kombinasi(j,u):
    if j == 0 or j == u:
        return 1
    elif j < u :
        return 0 
    else:
        return kombinasi(j-1,u-1) + kombinasi (j-1,u)
print (kombinasi(j: 4, u: 2))
print (kombinasi(j: 5, u: 3))
print (kombinasi(j: 6,u: 2))


# In[ ]:




