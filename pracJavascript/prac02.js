let car = {
    carname : "bmw",
    ph :  140,
    start : function() {
        console.log("engine start");
    },
    stop : function() {
        console.log("engine stop");
    },
};

console.log(car.carname);
car.start();  //메소드로 선언된 것을 실행하려면 () 해줘야 가능
console.log(car.start);
