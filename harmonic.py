def nthharmonic(N):
       harmonic = 1.00
       for i in range(2, N+1):
           harmonic += 1/i
       return harmonic

if __name__ == "__main__":
    print("Enter Number: ")
    N = int(input())
    print(round(nthharmonic(N), 5))