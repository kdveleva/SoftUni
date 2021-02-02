function sortedCatalogue(array) {
    array.sort()
    let sorted = {};
    while (array.length) {
        let [item, price] = array.shift().split(" : ");
        const firstLetter = item[0];

        if (!sorted[firstLetter]) {
            sorted[firstLetter] = [];
        }

        sorted[firstLetter].push(`${item}: ${Number(price)}`)
    }
    let result = [];
    for (const letter in sorted) {
        let value = sorted[letter]
        result.push(`${letter}
  ${value.join('\n')}`)
    }
    return result.join('\n');
}
console.log(sortedCatalogue(['Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10']
))