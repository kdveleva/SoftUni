function compose(arr) {
    const calObj = {};
    for (let i = 0; i < arr.length; i+=2) {
        calObj[arr[i]] = Number(arr[i + 1]);
        }
    return calObj;
}

console.log(compose(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']))