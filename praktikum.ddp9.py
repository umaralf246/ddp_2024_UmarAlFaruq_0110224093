#tugas 1 
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

print(celcius_ke_fahrenheit(0))    
print(celcius_ke_fahrenheit(100))  

#tugas 2
def ganjil_genap(bilangan):
    return bilangan % 2 == 0

print(ganjil_genap(4))  
print(ganjil_genap(7))  

#tugas 3
def nilai(kemampuan):
    return print("gagal" if kemampuan <= 60 else "lulus")

(nilai(80))  
(nilai(60))  

#tugas 4
def bilangan(n):
    return print([i for i in range(1, n, 2)])

(bilangan(20))  
