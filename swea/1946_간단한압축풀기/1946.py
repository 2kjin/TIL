T = int(input())
for t in range(1, T+1):
    n = int(input()) 
    result = ''                                             # 결과값들을 받을 빈 공간 생성
    for i in range(n):
        n, cnt = input().split()                          # 문자와 숫자 할당
        cnt = int(cnt)                                    # str로 받은 cnt를 int로 변환
        result += n * cnt                               # 빈 공간에 n를 입력받은 cnt만큼 추가
 
    print(f'#{t}')
    for i in range(len(result)):
        if (i+1)%10 == 0:                              # 10으로 나눴을때 나머지가 0 이라면
            print(result[i])                               # 줄 바꿔서 출력
        else:
            print(result[i], end='')                    # 아니라면 붙여서 출력
    print()