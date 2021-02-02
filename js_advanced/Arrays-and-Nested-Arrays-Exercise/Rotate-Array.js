function rotation(arr,  num) {
    for (let i = 1; i <= num; i++) {
        let first = arr.pop()
        arr.unshift(first)
    }
    return arr.join(' ')
}

console.log(rotation(['Banana',
        'Orange',
        'Coconut',
        'Apple'],
    15
))