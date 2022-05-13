from sys import stdin

f_input = lambda : stdin.readline().rstrip()
N, M = map(int, f_input().split())

url_to_pwd = dict()
for _ in range(N):
    url, pwd = f_input().split()
    url_to_pwd[url] = pwd

for _ in range(M):
    find_url = f_input()
    pwd_res = url_to_pwd[find_url]
    print(pwd_res)
