function lowestPrice(array) {
    let output = {};
    while (array.length) {
        let sale = array.shift();
        let [town, product, price] = sale.split(" | ");
        if (!output[product]) {
            output[product] = {town, price: Number(price)}
        } else {
            output[product] = output[product].price <= Number(price)
                ? output[product]
                : {
                    town, price: Number(price)
                }
        }
    }
    let result = [];
    for (const product in output) {
        result.push(`${product} -> ${output[product].price} (${output[product].town})`)
    }

    return result.join('\n');
}

    console.log(lowestPrice(['Sample Town | Sample Product | 1000',
        'Sample Town | Orange | 2',
        'Sample Town | Peach | 1',
        'Sofia | Orange | 3',
        'Sofia | Peach | 2',
        'New York | Sample Product | 1000.1',
        'New York | Burger | 10']
    ))

