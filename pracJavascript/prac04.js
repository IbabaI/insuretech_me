const array = [1, "test", {name : "name"}, 123.42312];
console.log(array[2])

// in java -> java는 형태가 같아야 한다. 
// public String [] StringArray = new String [5];
// public ArrayList(String) arrayListString = new ArrayList(String);

for(let i=0; i<array.length; i++){ // i는 0부터 시작, length는 4까지,  0 < 4
    let element = array[i];
    console.log(element);
}

// 위 아래는 같은 표현법

for(element of array){
    console.log(element);
}

// 위 아래는 같은 표현법

array.map((data) =>{
    console.log(data);
});