function solve(arr) {
    let output = arr.sort((a, b) => a.localeCompare(b));
    for (i = 0; i < arr.length; i++) {
        console.log(`${i+1}.${output[i]}`)
    }
}

solve(["John", "Bob", "Christina", "Ema"])