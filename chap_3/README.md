# 깊은 복사와 얕은 복사

## 두 객체의 비교와 복사

### 두 객체를 비교할 때 사용하는 연산자
```python3
r1 = [1, 2, 3]
r2 = [1, 2, 3]
r3 = r1         

r1 is r2        # r1과 r2가 참조하는 객체는 같은 객체인가?
                # => False
r1 is r3        # r1과 r3이 참조하는 객체는 같은 객체인가?              
                # => True
r1 == r2        # r1과 r2가 참조하는 객체에 담긴 값은 같은가?
                # => True
```
## 얕은 복사
list원소 내부의 immutable한 객체를 변경할 때는 문제가 되지 않는다
```python3
a = [1, (2, 3), [4]]
b = list(a)     # 얕은 복사
a is b          # False
b[0] += 1       # int(immutable 객체) 값을 1 증가
a == b          # False
```
그러나 mutable한 객체를 변경하면 원본 리스트도 같이 바뀐다.
```python3
a = [1, (2, 3), [4]]
b = list(a)     # 얕은 복사
a is b          # False
b[2][0] += 1    # 리스트(mutable 객체)의 값을 1 증가
a == b          # True
```
immutable한 객체에 얕은 복사를 하는 것은 상관없다. (값이 바뀌지 않으므로)

하지만 mutable한 객체에 얕은 복사를 하고 복사한 객체를 바꾸면 원본 객체도 바뀐다.

=> 깊은 복사가 필요 !!

## 깊은 복사

immutable한 객체에는 얕은 복사, mutable한 객체에는 깊은 복사를 진행하는 것이 안전성과 성능을 모두 만족시키는 방법이 된다.

깊은 복사를 사용하려면 다음과 같이 **copy모듈의 deepcopy함수** 를 사용하면 된다.

```python3
J2021 = ['John', ('man', 'USA'), [175, 23]]
import copy         # deepcopy 함수 호출 위해서 copy 모듈 import
J2022 = copy.deepcopy(J2021)    #깊은 복사
J2022[2][1] += 1    # John나이 한살 먹음
J2021               # ['John', ('man', 'USA'), [175, 23]]
J2022               # ['John', ('man', 'USA'), [175, 24]]
```

