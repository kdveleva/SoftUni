function solve(arr) {
    let maxNum = Number.MIN_SAFE_INTEGER;

    let output = arr.reduce((acc,curr) => {
        if (curr >= maxNum) {
            maxNum = curr;
            acc.push(maxNum);
        }
        return acc;
    }, []);
    return output;
}

console.log(solve([]))