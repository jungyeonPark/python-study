# 리스트 컴프리헨션
## 리스트 생성 방법
* 리스트를 생성하는 기본 방법
(너무 쉬워서 패스)

* list함수를 호출해서 리스트를 생성하는 방법
    ```python3
    r4 = list('Hello')       # 문자열을 전달해서 리스트를 생성
    r5 = list((5, 6, 7))     # 튜플을 전달해서 리스트를 생성
    r6 = list(range(0, 5))   # 레인지를 전달해서 리스트 생성
    ```
* 리스트 컴프리헨션으로 생성
    ```python3
    r1 = [1, 2, 3, 4, 5]        
    r2 = [x * 2 for x in r1]    # 리스트 컴프리헨션의 기본 구조
    r2                          # [2, 4, 6, 8, 10]
    ```
    리스트 컴프리헨션을 분석할 때는 먼저 for문 앞을 본 후 for문 이하를 본다.

    r2 = [x * 2 for x in r1] 에서 r2리스트는 x * 2의 결과들로 이뤄진다는 뜻

    그 다음 for x in r1 에서 x는 r1에 있는 값이라는 것을 알 수 있다.

## 조건 필터 추가하기
리스트에 담을 값을 걸러내고 싶다면
리스트 컴프리헨션을 기반으로 간단하게 작성할 수 있다.
```python3
r1 = [1, 2, 3, 4, 5]
r2 = [x * 2 for x in r1 if x % 2]     # if절이 추가된 리스트 컴프리헨션
r2                                    # [2, 6, 10]
```
if x % 2 가 참이면 x * 2의 값을 리스트에 추가한다.

## 리스트 컴프리헨션에 이중 for문 사용하기
옷의 상의와 하의의 색상 정보를 갖는 리스트가 각각 존재하는 상황에서 만들 수 있는 모든 조합의 색을 값으로 담는 리스트를 만들고자 한다.

```python3
r1 = ['Black', 'White']     
r2 = ['Red', 'Blue', 'Green']
r3 = [t + p for t in r1 for p in r2]    # 중첩된 for문 형태의 리스트 컴프리헨션
r3
# ['BlackRed', 'BlackBlue', 'BlackGreen', 'WhiteRed', 'WhiteBlue', 'WhiteGreen'] 
```
## 이중 for루프에 조건 필터 추가
그냥 뒤에 if문 추가하면됨
