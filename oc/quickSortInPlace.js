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

console.log(quicksort([7,1,3,2,5,6,4]));