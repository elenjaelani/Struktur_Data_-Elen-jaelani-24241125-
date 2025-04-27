print ("elen jaelani 242421125")
inputuser = int(input("masukkan bilangan antara 24 atau lebih dari 25"))

#+++++24------------
#memeriksa angka yang kurang dari 24
iskurangdari = (inputuser <24)

#memeriksa angka yang kurang dari 25
islebihdari = (inputuser <25)

final = iskurangdari or islebihdari
print("angka yang anda masukan", final)