function sortingNumbers(arr) {
    const newArr = [];
    const arrLen = arr.length/2;
    arr.sort(function (a, b) {
        return a - b
    })
    for (let i = 0; i < arrLen; i++) {
       let first = arr.shift();
       let last = arr.pop();
       newArr.push(first);
       newArr.push(last);
    }
    return newArr
}

console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))