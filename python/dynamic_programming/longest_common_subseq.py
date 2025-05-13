def lcsRec(s1,s2,m,n):
    if m==0 or n==0:
        return 0
    if s1[m-1] == s2[n-1]:
        return 1 + lcsRec(s1,s2,m-1,n-1)
    else:
        return max(lcsRec(s1,s2,m-1,n),lcsRec(s1,s2,m,n-1))


def lcs(s1,s2):
    m = len(s1)
    n = len(s2)
    return lcsRec(s1,s2,m,n)

if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(lcs(s1, s2))
