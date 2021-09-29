class suku:
    def intro(self):
        print("indonesia mempunyai berbagai macam suku")

    def bahasa(self):
        print("suku suku tersebut mempunyai bahasa yang berbeda")

class sunda(suku):
    def bahasa(self):
        print("Suku Sunda berkomunikasi menggunakan bahasa Sunda. Uniknya bahasa Sunda yang digunakan memiliki dialek khas dari daerah-daerah di Jawa Barat. Misalnya Sunda-Banten, Cirebonan, atau Sunda-Jawa Tengah yang biasanya eksis di daerah-daerah perbatasan.")

class jawa(suku):
    def bahasa(self):
        print("Suku Jawa berkomunikasi menggunakan bahasa. Setiap daerah memiliki dialek bahasa Jawa yang berbeda. Dialek bahasa Jawa dari Jawa Tengah memiliki perbedaan dengan dialek bahasa Jawa dari Jawa Timur. ")

obj_suku = suku()
obj_sunda = sunda()
obj_jawa = jawa()

obj_suku.intro()
obj_suku.bahasa()

print("\n")

obj_sunda.intro()
obj_sunda.bahasa()

print("\n")

obj_jawa.intro()
obj_jawa.bahasa()