function twoCriteria(arr) {
    return arr.sort(function (a, b) {
        if (a.length === b.length) {
            return a.localeCompare(b);
        }
        return a.length - b.length
    }).join('\n')
}

console.log(twoCriteria(['test',
    'Deny',
    'omen',
    'Default']
))