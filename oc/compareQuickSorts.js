/*
 * Complete the 'quicksort' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function quicksort(arr) {

    function subsort(left, right) {
        if (left >= right) {
            return;
        }

        let pivot = arr[right];
        let pivotIndex = right;

        let wall = left;

        for (let i = left; i < pivotIndex; i++) {
            if (arr[i] < pivot) {
                swap(i, wall, arr);
                wall++;
            }
        }

        swap(wall, pivotIndex, arr);

        subsort(left, wall - 1);
        subsort(wall + 1, right);
    }

    subsort(0, arr.length - 1);
    return arr;
}

function swap(i, j, arr) {
    [arr[i], arr[j]] = [arr[j], arr[i]];
}



function quicksortv2(arr) {
    if (arr.length < 2) {
        return arr;
    }
    let pivot = arr[arr.length - 1];

    let left = [];
    let right = [];

    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    return quicksortv2(left).concat(pivot).concat(quicksortv2(right));
}



let test = [];

for (let i = 0; i < 10000; i++) {
    test.push(Math.floor(Math.random() * 1000));
}


console.time("IN-PLACE: ");
quicksort(test);
console.timeEnd("IN-PLACE: ");


console.time("NOT-IN-PLACE");
quicksortv2(test);
console.timeEnd("NOT-IN-PLACE");
