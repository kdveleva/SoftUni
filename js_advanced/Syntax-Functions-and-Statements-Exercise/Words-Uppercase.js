function changeToUppercase(string) {
    let re = /\w+/g;
    let myArray = string.match(re);
    console.log(myArray.join(", ").toUpperCase())
}

changeToUppercase('Hi, how are you?')