#Source code encryption decryption Engelbert Jubile
class deskripsi:
    def Deskripsi:
        print("Program Deskripsi")
        mode = 1
        print("Masukkan penggeseran yang dipilih (0 hingga 25):")
        X = int(input())
        kalimat = "AMSJHDK"
        abjad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        terdeskripsi = ''
        kalimat = kalimat.upper()
        for A in message:
            if A in letters:
                B = letters.find(A)
                if mode <= 1:
                    B += X
                elif mode >= 2:
                    B -= X
                if B >= len(abjad):
                    B -= len(abjad)
                elif B < 0:
                    B += len(abjad )
                    terdeskripsi += abjad[B]
            else:
                terdeskripsi += A
        return terdeskripsi


def Enkripsi:
    print("Program Enkripsi")
    mode = 1
    print("Masukkan penggeseran yang dipilih (0 hingga 25):")
    X = int(input())
    kalimat = "AKSGSJ"
    abjad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    terenkripsi = ''
    kalimat = kalimat.upper()
    for A in message:
        if A in letters:
            B = letters.find(A)
            if mode <= 1:
                B += X
            elif mode >= 2:
                B -= X
            if B >= len(abjad):
                B -= len(abjad)
            elif B < 0:
                B += len(abjad )
                terenkripsi += abjad[B]
        else:
            terenkripsi += A
    return terenkripsi

objek=deskripsi

print(objek.Deskripsi())
print(Enkripsi())


