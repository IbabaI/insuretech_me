function myFunction(p1, p2){
    // 여러가지 프로그래밍
    return p1 + p2;
};

//   위 아래 코드는 하는일이 같다. 차이점은 거의 없고, 아래는 Arrow function 이다.

const plus = (p1, p2) => {
    return p1 + p2;
}

const minus = (p1, p2) => {
    return p1 - p2;
}

const multi = (p1, p2) => {
    return p1 * p2;
}

const div = (p1, p2) => {
    return p1 / p2;
}



//실습 3 minus, multi, div => 빼기, 곱하기, 나누기 기능 추가 바랍니다.

console.log(myFunction(5,5));
console.log(myFunction(5,9));

console.log(plus(5,9));
console.log(minus(5,9));
console.log(multi(5,9));
console.log(div(5,9));