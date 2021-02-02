function squareOfStars(size=5){
    let star;
    let array = [];
    for (let i = 1; i <= size; i++){
        array.push('*')

    }
    for (let x = 1; x <= size; x++){
        console.log(...array)
    }

}
squareOfStars(2)