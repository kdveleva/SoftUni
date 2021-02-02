function fruit(fruit, weight, pricePerKilo){
    let money = pricePerKilo * (weight/1000);
    console.log(`I need $${money.toFixed(2)} to buy ${(weight/1000).toFixed(2)} kilograms ${fruit}.`)
}


let arr = ['orange', 2500, 1.80]
fruit(...arr)
let brr = ['apple', 1563, 2.35]
fruit(...brr)