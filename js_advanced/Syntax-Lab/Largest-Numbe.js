function solve(num1, num2, num3) {
    let result;

    if (num1 > num2 && num1 > num3){
        result = num1;
    }


    if (num2 > num1 && num2 > num3){
        result = num2;
    }


    if (num3 > num1 && num3 > num2){
        result = num3;
    }
    console.log(`The largest number is ${result}.`)
}

let num1 = 1
let num2 = 10
let num3 = -1

solve(num1, num2, num3)
