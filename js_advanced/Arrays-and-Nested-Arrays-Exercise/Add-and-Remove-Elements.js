function solve(arr) {
    let result = 0;
    let newArr = [];
    for (let action of arr) {
        if (action === 'add') {
            newArr.push(result += 1);
        }
        if (action === 'remove') {
            newArr.pop();
            result += 1;
        }
    }
    if (newArr.length === 0) { return 'Empty'}
    else { return newArr.join('\n')}
}

console.log(solve(['add',
    'add',
    'remove',
    'add',
    'add']
))