function gcd(num1, num2){
    let maxGCD = 0
    if (num1 > 0 && num2 > 0){
        let maxNum = Math.max(num1, num2);
        for (let i = 1; i <= num1; i++ ){
            if (num1 % i === 0 && num2 % i === 0){
                maxGCD = i
            }
        }
    }
    console.log(maxGCD)
}

gcd(2154, 458 )