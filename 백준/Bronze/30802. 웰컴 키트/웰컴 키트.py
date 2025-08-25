N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

T_order = 0
P_order_d = 0
P_order_s = 0

T_order += (S//T +1 if S%T != 0 else S//T)
T_order += (M//T +1 if M%T != 0 else M//T)
T_order += (L//T +1 if L%T != 0 else L//T)
T_order += (XL//T +1 if XL%T != 0 else XL//T)
T_order += (XXL//T +1 if XXL%T != 0 else XXL//T)
T_order += (XXXL//T +1 if XXXL%T != 0 else XXXL//T)


P_order_d = N // P
P_order_s = N % P

print(T_order)
print(f"{P_order_d} {P_order_s}")