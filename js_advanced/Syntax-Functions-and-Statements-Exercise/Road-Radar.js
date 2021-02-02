function speedLimit(speed, area) {
    let areasLimits = {
        'motorway': 130, 'interstate': 90,
        'city': 50, 'residential': 20
    }
    if (speed <= areasLimits[area]) {
        return `Driving ${speed} km/h in a ${areasLimits[area]} zone`
    }
    if (speed > areasLimits[area]) {
        let diff = speed - areasLimits[area]
        let status = ''
        if (0 < diff) { status = 'speeding'}
        if (20 < diff) {status = 'excessive speeding'}
        if (40 < diff) {status = 'reckless driving'}
        return `The speed is ${diff} km/h faster than the allowed speed of ${areasLimits[area]} - ${status}`
    }
}

console.log(speedLimit(21, 'residential'))