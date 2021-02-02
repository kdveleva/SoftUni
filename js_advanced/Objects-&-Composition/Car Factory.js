function carAssembler(carObject) {
    let newParts = {model: '', engine: {power: 0, volume: 0}, carriage: {type: '', color: ''}, wheels: [] }
    newParts["model"] = carObject.model
    if (carObject.power < 91) {
        newParts["engine"]["power"] = 90
        newParts["engine"]["volume"] = 1800
    } else if (carObject.power < 120) {
        newParts["engine"]["power"] = 120
        newParts["engine"]["volume"] = 2400
    } else if (carObject.power < 300) {
        newParts["engine"]["power"] = 200
        newParts["engine"]["volume"] = 3500
    }

    newParts["carriage"]["type"] = carObject.carriage
    newParts["carriage"]["color"] = carObject.color
    if (Math.floor(carObject.wheelsize) % 2 === 0) {
        carObject.wheelsize = Math.floor(carObject.wheelsize - 1)
    }
    for (let i = 0; i < 4; i++) {
        newParts["wheels"].push(carObject.wheelsize)
    }
    return newParts
}

console.log(carAssembler({ model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 15}
))