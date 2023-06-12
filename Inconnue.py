def Inconnue(N):
    #la fonction retourne la somme des elements de N:
    if N<=9:
        return N
    else:
        s=N%10
        N=N//10
        return s+Inconnue(N)
    
def main():
    n=int(input("Donnez N:"))
    x=Inconnue(n)
    print("resultat:{}".format(x))

if __name__=="__main__":
    main()
