function heroInventory(array) {
    let dataJSON = []
    for (let str of array) {
        let [name, level, items] = str.split(" / ")
        level = Number(level);
        items = items ? items.split(', ') : [];
        dataJSON.push({name, level, items})
    }
    return JSON.stringify(dataJSON)
}

console.log(heroInventory(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara']
))