def solution(numbers):
    answer = []
    
    for i in numbers:
        if i == 0:
            answer.append(1)
            continue
        n = bin(i)[2:]
        # if n.count('1') == len(n):
        #     n = '10'+n[1:]
        # else:
        while True:
            i += 1
            m = bin(i)[2:]
            n = n.zfill(len(m))
            count = 0
            for j in range(1,len(m)+1):
                if m[-j] != n[-j]:
                    count+=1
                if count > 2:
                    break
            if count <=2:
                break
        print('n=',n)
        print('m=',m)
        print('----------------------------------')
        answer.append(i)
        
    return answer


numbers = [2, 7, 3, 4, 63, 64, 0, 1, 91, 703]
# [3, 11, 5, 5, 95, 65, 1, 2, 93]
numbers2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(solution(numbers2))