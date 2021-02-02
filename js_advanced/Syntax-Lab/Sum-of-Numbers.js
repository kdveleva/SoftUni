function solve(n, m){
    let numberOne = Number(n);
    let numberTwo = Number(m);
    let  result = 0;
    for (let i=numberOne; i<=numberTwo; i++) {
        result += i;
    }
    return result

}

console.log(solve('1', '5'))