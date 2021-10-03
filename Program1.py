print("\nSelamat Datang di Tugas Pratikum Algoritma 1") #print selamat datang

#user memilih angka inputan untuk memilih program mana yang dijalankan
masukan = int(input("\n1. Mengubah Suhu ke Farenheit/ Reamur/ Kelvin \n2. Menghitung Body Mass Index \n3. Permainan Batu Kertas Gunting \n4. Exit \nSilahkan Pilih Pilihan Anda: "))

#percabangan dilaksanakan jika user memasukan angka 1
if masukan ==1:

    #user memasukan angka inputan untuk memilih program mana yang dijalankan
    Masukan1 = int(input("\n1.Mengubah Suhu ke Farenheit \n2.Mengubah Suhu ke Kelvin \n3.Mengubah Suhu ke Reamur \n4.Keluar \nSilahkan Memilih Pilihan Anda: "))
    
    #percabangan 1 dilaksanakan jika user memasukan angka 1
    if Masukan1 ==1:

        #user memasukan inputan suhu celcius tipe float
        C = float(input("Masukan Suhu Celcius: "))
        F = (C * (9/5)) + 32 #rumus faranhite
        print("Suhu Fahranhite ",F ," °F") #print hasil rumus faranhite
    #percabangan dilaksanakan jika user memasukan angka 2
    elif Masukan1 ==2:

        #user memasukan inputan suhu celcius tipe float
        C = float(input("Masukan Suhu Celcius: "))
        K = C + 273.15 #rumus kelvin
        print("Suhu Kelvin ", K ," °K") #print hasil rumus kelvin
    
    #percabangan dilaksanakan jika user memasukan angka 3
    elif Masukan1 ==3:

        #user memasukan inputan suhu celcius tipe float
        C = float(input("Masukan Suhu Celcius: ")) 
        Re = C * (4/5) #rumus reamur
        print("Suhu Reamur ", Re ," °Re") #print hasil rumus reamus
    
    #percabangan dilaksanakan jika user memasukan angka 4
    elif Masukan1 ==4:
        exit() #keluar dari program
    
    #percabangan  akan false dan memasuki else jika memasukan angka selain 1,2,3
    else: 
        print("Maaf Pilihan Tidak Ada") #print pilihan tidak ada

#percabangan dilaksanakan jika user memasukan angka 2
elif masukan ==2:
    berat_badan = float(input("Masukan Berat Anda: ")) #user memasukan angka berat badan
    tinggi_badan = float(input("Masukan Tinggi Anda: ")) #user memasukan tinggi badan
    BMI = berat_badan /(tinggi_badan*tinggi_badan) #rumus bmi
    if BMI < 17.0 : #jika hasil bmi kurang 17.0 akan memulai percabangan ini
        print("Kurus, Kekurangan berat badan berat") #print kurus
    elif BMI >= 17.0 and BMI <= 18.4 : #jika hasil bmi antara 17.0 - 18.4 akan memulai percabangan ini
        print("Kurus, Kekurangan berat badan ringan") #print kurus
    elif BMI >= 18.5 and BMI <= 25.0: #jika hasil bmi antara 18.5 - 25.0 akan memulai percabangan ini
        print("Normal") #print normal
    elif BMI >= 25.1 and BMI <= 27.0: #jika hasil bmi antara 25.1 - 27.0 akan memulai percabangan ini
        print("Gemuk, Kelebihan berat badan tingkat ringan") #print gemuk
    elif BMI > 27.0 : #jika hasil bmi lebih 27.0 akan memulai percabangan ini
        print("Gemuk, Kelebihan berat badan tingkat berat") #print gemuk
#percabangan dilaksanakan jika user memasukan angka 3
elif masukan ==3:
    from random import randint #import modul random dari randint

    game_list =["Batu", "Kertas", "Gunting"] #variabel yg value nya list
    computer = game_list[randint(0,2)] #variabel yg diisi list dan akan digabungkan dengan modul random

    players = 0 #variabel value nya 0

    while players < 3: # perulangan dilaksanakan jika variabel bernilai false
        player = input("Gunting, Batu, Kertas ? : ") #user memasukan inputan string
        if player == computer: #jika value variabel sama dengan computer akan memasuki percabangan ini
            print("Seri!") #print seri
        elif player == "Batu": #jika value variabel player batu akan memasuki percabangan ini
            if computer == "Kertas":  #jika value variabel computer kertas akan memasuki percabangan ini
                print("Kamu Kalah!", computer, "membungkus", player) #print kalah
            else: #jika value variabel computer selain kertas akan memasuki percabangan ini
                print("Kamu Menang!", player, "menghancurkan", computer) #print menang
        elif player == "Kertas" : #jika value variabel player kertas akan memasuki percabangan ini
            if computer == "Gunting": #jika value variabel computer gunting akan memasuki percabangan ini
                print("Kamu Kalah!", computer, "memotong", player) #print kalah
            else:  #jika value variabel computer selain gunting akan memasuki percabangan ini
                print("Kamu Menang!", player, "membungkus", computer) #print menang
        elif player == "Gunting" : #jika value variabel player gunting akan memasuki percabangan ini
            if computer == "Batu" : #jika value variabel computer batu akan memasuki percabangan ini
                print("Kamu Kalah!", computer, "menghancurkan", player) #print kalah
            else: #jika value variabel computer selain batu akan memasuki percabangan ini
                print("Kamu Menang!", player, "momotong", computer) #print menang
        else:  #jika value variabel player selain batu,kertas,gunting akan memasuki percabangan ini
            print("Pilihan yang kamu masukan salah...")  #print inputan salah
            
        players +=1 #variabel plyaer ditambah1
elif masukan==4: #percabangan dilaksanakan jika user memasukan angka 4
    exit() #keluar dari program
else: #percabangan dilaksanakan jika user memasukan selain angka 1 sampai 4
    print("Inputan Anda Salah")  #print inputan salah


