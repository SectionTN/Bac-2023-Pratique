from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from numpy import array


def verif_occur(ch):
    i = 0
    while i < len(ch) - 2 and int(ch[i]) + 1 == int(ch[i + 1]):
        i += 1
    return int(ch[i]) + 1 == int(ch[i + 1])


def tri(T, N):
    for i in range(N):
        for j in range(N - i - 1):
            if T[j] > T[j + 1]:
                aux = T[j]
                T[j] = T[j + 1]
                T[j + 1] = aux


def verifier(M, N):
    ch = M + N
    T = array([str] * len(ch))
    for i in range(len(ch)):
        T[i] = ch[i]
    tri(T, len(ch))
    nv_ch = ""
    for i in range(len(ch)):
        nv_ch = nv_ch + T[i]
    ch = nv_ch
    return verif_occur(ch)


def play():
    M = window.m.text()
    N = window.n.text()
    if not (int(M) > 0) or not (int(N) > 0):
        window.msg.setText("v introduire deux entier positifs")
    else:
        window.msg.setText("")
        resultat = verifier(M, N)
        if resultat == True:
            window.msg.setText(M + " et " + N + " forme une succession parfaite")
        else:
            window.msg.setText(M + " et " + N + " ne forme pas une succession parfaite")


application = QApplication([])
window = loadUi("parfait.ui")
window.show()
window.b_verif.clicked.connect(play)
application.exec_()
