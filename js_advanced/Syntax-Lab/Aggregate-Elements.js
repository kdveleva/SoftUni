function aggregatedElements(array) {
    aggregate(array, 0, (a, b) => a + b);
    aggregate(array, 0, (a, b) => a + 1/b);
    aggregate(array, '', (a, b) => a + b);
    function aggregate(arr, initVal, func){
        let val = initVal;
        for (let i = 0; i < arr.length; i++)
            val = func(val, arr[i]);
        console.log(val);
    }
}

let nums = [1, 2, 3]
aggregatedElements(nums)