# [알고리즘 분석 Hw01] 

#### 2016103236 응용수학과 김영웅



### 수행내용

> 파이썬 프로그램을 이용하여 n개의 데이타 (키 값은 1~100 사이의 자연수)를 정렬하는 문제를 파이썬 프로그램을 이용하여 다음의 내용에 대해 수행한다.
> * (1) n개의 데이타를 random으로 생성 
> * (2) O(n^2) 인 exchange sort 알고리즘(A)와 O(n log n) 알고리즘인 merge sort 알고리즘(B)를 구현
>* (3) n=2,000, 4,000, 12,000에 대해 알고리즘 A, B가 종료될 때까지의 시간을 측정한다.
>* (4) A, B 를 1분간 수행할 때 해결할 수 있는 문제의 크기 n' 를 (3)의 결과를 이용하여 추정한다. A와 B의 수행시간과 n의 관계를 고려해서 추정할 것.
>* (5) n=5,000만일 때의 A, B의 수행시간을 (3)의 결과를 이용하여 추정한다.

---
<br>

#### (1) n개의 데이타를 random으로 생성

```
import random as rand
data = [rand.randint(1, 100) for i in range(100)]
```
<br>

#### (2) O(n^2) 인 exchange sort 알고리즘(A)와 O(n log n) 알고리즘인 merge sort 알고리즘(B)를 구현

<br>

> **(2-A) 구현**

```
 #깊은 복사를 위한 copy 라이브러리 임포트
    import copy
    
    def exchange_sort(_s):
        s = copy.deepcopy(_s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] > s[j]:
                    s[i], s[j] = s[j], s[i]
        return s

```
<br>

> **(2-B) 구현**

```
    def merge_sort(_s):
        s = copy.deepcopy(_s)
        if len(s) == 1:
            return s
        else:
            mid = len(s)//2
            left = merge_sort(s[:mid])
            right = merge_sort(s[mid:])
    
            i, j = 0, 0
            result = []
            while (i<len(left)) & (j<len(right)):
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            while (i<len(left)):
                result.append(left[i])
                i+=1
    
            while (j<len(right)):
                result.append(right[j])
                j+=1
            return result
```
<br>

#### (3) n=2,000, 4,000, 12,000에 대해 알고리즘 A, B가 종료될 때까지의 시간을 측정한다.

```
from time import time

conditions = [[rand.randint(1, 100) for i in range(iteration)]
             for iteration in [2000, 4000, 12000]]


for condition in conditions:
    print(f'n={len(condition)}')
    start = time()
    exchange_sort(condition)
    end = time()
    print(f'exchange sort time  : {end-start:6.5f}s')
    start = time()
    data_sorted_by_merge = merge_sort(condition)
    end = time()
    print(f'merge sort time     : {end-start:6.5f}s')
    print()

```
#### Result

|         | Exchange |  Merge   |
| :-----: | :------: | :------: |
| n=2000  | 0.09803s | 0.02000s |
| n=4000  | 0.38798s | 0.04300s |
| n=12000 | 3.28930s | 0.13900s |

<br>

#### (4) A, B 를 1분간 수행할 때 해결할 수 있는 문제의 크기 n' 를 (3)의 결과를 이용하여 추정한다. A와 B의 수행시간과 n의 관계를 고려해서 추정할 것.

**앞선,  (3)의 결과를 보면, O(N^2)의 시간 복잡도를 가지는 exchange sort의 경우 n이 커질수록 소요시간은 t는 k*n^2에 수렴하게 된다.
n=2000 일 때 t=0.098s 임을 이용하면 k = 2.45e-08, 이를 이용해 1분동안 실행 가능한 n의 수를 구하면 약 n=49487이다.**

```
import math
k = (0.098)/(2000*2000)
print(k)
a_minute_iteration_of_exchange = math.sqrt(60/2.45e-08)
print(a_minute_iteration_of_exchange)
```

2.45e-08

49487.165930539355

<br>

**마찬가지로, O(N*logN)의 시간 복잡도를 가지는 merge sort의 경우 n이 커질수록 소요시간 t는 k*nlog(n)에 수렴하게 된다.**

**n=2000일 때, t=0.02s 임을 이용하면, k = 1.3156332492395189e-06 **

**단, 이를 이용해 1분동한 실행 가능한 n의 수를 구하려면, nlog(n) 함수의 역함수를 이용해야 하므로 엄밀한 증명은 생략한다. **

**(근사를 통해 약 n=3055000임을 확인할 수 있다.)**

```
k = (0.02)/(2000*math.log(2000))
print(k)
# a_minute_iteration_of_merge = 3055000
```

1.3156332492395189e-06

<br>

#### (5) n=5,000만일 때의 A, B의 수행시간을 (3)의 결과를 이용하여 추정한다.

**앞서 (4)에서 구한 k를 이용하면 각각 구할 수 있다.
exchange sort의 경우, t = (2.45e-08)*n^2에 수렴하므로, 계산하면 약 708일이 소요된다.**

```
t_exchange = (2.45e-08)*(50000000)*(50000000) // 3600 // 24  # 708일
print(t_exchange)
```
708.0

<br>

merge sort의 경우, t = (1.3156332492395189e-06)*nlog(n)에 수렴하므로, 계산하면 약 19분이 소요된다.

```
t_merge = (1.3156332492395189e-06)*50000000*math.log(50000000) // 60 # 19분
print(t_merge)
```

19.0