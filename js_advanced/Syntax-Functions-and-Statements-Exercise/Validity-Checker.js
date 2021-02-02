function validity(x1, y1, x2, y2) {
    function test(x1, y1, x2, y2){
        let result
        let validate = 'invalid'
        result = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
        if (Number.isInteger(result)) {
            validate = 'valid'
        }
        return validate
    }
    console.log( `{${x1}, ${y1}} to {0, 0} is ${test(x1,y1,0,0)}
{${x2}, ${y2}} to {0, 0} is ${test(x2,y2,0,0)}
{${x1}, ${y1}} to {${x2}, ${y2}} is ${test(x1, y1, x2, y2)}`)
}

validity(2, 1, 1, 1)