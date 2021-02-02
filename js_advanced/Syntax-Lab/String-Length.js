function stringLength(a, b, c){
    let totalSum = a.length + b.length + c.length
    console.log(totalSum)
    let averageSum = (a.length + b.length + c.length) / 3
    console.log(Math.floor(averageSum))
}

let a = 'chocolate'
let b = 'ice cream'
let c = 'cake'
stringLength(a, b, c)