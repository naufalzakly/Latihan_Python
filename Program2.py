print("\nSelamat Datang di Program 2") #print selamat datang

#user memilih angka inputan untuk memilih program mana yang dijalankan
masukan = int(input("\n1. Menentukan Nilai Ganjil atau Genap \n2. Operasi Perhitungan \n3. MAD LIBS GAME \n4. Exit \nSilahkan Pilih Pilihan Anda: "))


if masukan == 1:
    #no 1
    number = int(input("Masukan Nomor Anda: "))
    angka = number % 2
    ganjil = angka >0
    genap = angka = 0
    print(number,"\n",ganjil)
elif masukan == 2:
    #no 2
    inputan1 = int(input("Inputan 1: "))
    inputan2 = int(input("Inputan 2: "))
    num1 = inputan1 // inputan2
    num2 = inputan1 % inputan2
    total_num = num1 * num2
    print("Keluaran: ", total_num)
elif masukan ==3:
    #no 3
    inputan1 = input("Masukan Nama mu: ")
    inputan2 = input("Masukan Nama teman mu: ")
    print("Saya", inputan1,"\nIni Adik saya", inputan2,"\nKita Kembar Seirama")
elif masukan ==4:
    exit()
else:
    print("Pilihan Anda Tidak Ada")