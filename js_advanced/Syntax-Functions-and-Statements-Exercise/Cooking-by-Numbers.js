function cook(num, ...list) {
    let result = num;
    for (let i = 0; i < 5; i++) {
        switch (list[i]) {
            case 'chop':
                result /= 2;
                break;
            case 'dice':
                result = Math.sqrt(result);
                break;
            case 'spice':
                result += 1;
                break;
            case 'bake':
                result *= 3;
                break;
            case 'fillet':
                result -= result * 0.20;
                break
        }
        console.log(result)
    }
}

cook('9', 'dice', 'spice', 'chop', 'bake', 'fillet')