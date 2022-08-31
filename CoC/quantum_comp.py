'''You are the first to build a high-end Quantum Computer!
Quantum Computers are the next big step in the evolution of computers and they use qubits to store information.
Your task: Print out the minimum number of qubits required to store the file sizes received as input.

Hints:
- n qubits can store as much information as 2^n bits.(Why? While classical bit can be either 0 OR 1, a quantum bit, or qubit is a superposition of 0 AND 1)
- Qubits may have unused capacity (you'll need to find the minimum qubit size that fulfills this: total capacity of qubits >= the information we need to store.)
- 1 byte= 8 bits, 1 KB = 1024 byte, 1 MB = 1024 KB, 1 GB = 1024 MB, 1 TB = 1024 GB

Example:
Input : 3 byte (3 byte = 24 bits )
Output : 5 (5 qubit = 2^5bits = 32 bits. And 32bits >= 24 bits .
4 qubit would be too few since 2^4=16 and 16 is less than 24.
Input
Line 1: An integer N for the value you need to convert to qubits.
Line 2: A string S for the name of measurement unit you need to convert to qubits. byte, KB, MB, GB,TB
Output
Line 1 : An integer Q for the MINIMUM REQUIRED qubits you need to store the amount of information defined in the input.
Constraints
0 ≤ N ≤ 1024
S can only be one of the following: byte, KB, MB, GB or TB
Example
Input
1
byte
Output
3'''


# n,r=(input("enter no and type: ")).split()
n = int(input("enter no: "))
r = input("Enter type: ").lower()
e = (n*(2**3) if r == "byte" else n*(2**10) if r == "kb" else n*(2**20) if r == "mb" else n*(2**30) if r == "gb" else n*(2**40) if r == "tb" else 0)
for i in range(e):
    s = 2**i
    if s >= e:
        print(i)
        break
