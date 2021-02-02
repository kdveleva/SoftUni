function distanceToUniversity(steps, lengthOfFootprint, speed) {
    let speedInMeters = speed * 1000/3600;
    let distanceInMeters = steps * lengthOfFootprint;
    const rest = Math.floor(distanceInMeters/500);
    let time = distanceInMeters/speedInMeters + rest * 60;
    let hours = Math.floor(time/3600);
    let minutes = Math.floor(time/60);
    let seconds = Math.ceil(time - hours*3600 - minutes*60);

    return `${hours.toFixed(0).padStart(2, "0")}:${minutes.toFixed(0).padStart(2, "0")}:${seconds.toFixed(0).padStart(2, "0")}`
}

console.log(distanceToUniversity(4000, 0.60, 5))