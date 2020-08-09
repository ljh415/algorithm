# Hashing

## Hash란?

- 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수
- 기존의 자료구조들은 탐색, 삽입에 선형시간이 소요하지만,
해쉬는 즉시 저장하거나 찾고자 하는 위치를 참조할 수 있으므로 빠르다.
- 보통 modular 연산(나머지 연산)을 사용

## Hash함수의 한계 ⇒ 충돌(Conclusion)

- 서로 다른 입력 값에 대해 같은 해시 태이블 주소를 반환할 때 충돌이 발생

### 해결방법

- 크게 개방해싱과 폐쇄해싱으로 나뉜다.
- 아래 그림 참고
- Open Addressing에는 다음과 같은 방식들이 있다.
    1. Liner Probing (선형탐색)
    2. Qudratic Probing (제곱탐색)
    3. Double Hasing (이중해싱)
    4. Rehasing (재해싱)

![1](https://user-images.githubusercontent.com/48716219/89732694-7d8e2b80-da8b-11ea-9e83-a0e9457151f9.png)

- 볼만한 자료

    [해쉬 알고리즘(Hash Algorithm) 요약 정리, 테스트 코드](https://hsp1116.tistory.com/35)

    [해싱, 해시함수, 해시테이블](https://ratsgo.github.io/data%20structure&algorithm/2017/10/25/hash/)

    [8장 해시 테이블](https://dbehdrhs.tistory.com/70)