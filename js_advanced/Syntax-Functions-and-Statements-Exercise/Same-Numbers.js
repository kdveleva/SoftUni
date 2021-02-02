function sameNumbers(integer) {
    let first = integer % 10;
    let sumAllDigits = 0;
    let FT = true
    while (integer) {
        if (integer % 10 !== first) FT = false;
        sumAllDigits += integer % 10;
        integer = Math.floor(integer/10)
    }
    if (FT) console.log(true)
    else console.log(false)
    console.log(sumAllDigits)
}

sameNumbers(1234)