function mostFrequentNumber(arr) {
    // Object to store frequency counts
    const frequency = {};

    // Variables to keep track of the most frequent number and its count
    let mostFrequent = arr[0];
    let highestCount = 0;

    // First pass: Calculate frequencies
    for (let i = 0; i < arr.length; i++) {
        const num = arr[i];
        frequency[num] = (frequency[num] || 0) + 1;

        // Check if this is the new most frequent number
        if (frequency[num] > highestCount || (frequency[num] === highestCount && num > mostFrequent)) {
            highestCount = frequency[num];
            mostFrequent = num;
        }
    }

    // Return the result as [number, count]
    return [mostFrequent, highestCount, frequency];
}

// Example usage
console.log(mostFrequentNumber([1, 1, 1, 2, 2])); // [1, 3]
console.log(mostFrequentNumber([2, 2, 2, 3, 3, 3])); // [3, 3]






function mostFreq(arr) {
    const freq = {}

    let mostFreq = arr[0]
    let count = 0

    for (let i = 0; i < arr.length; i++) {
        const num = arr[i]
        if (freq[num]) {
            freq[num] +=  1
        } else {
            freq[num] = 1
        }

        if (freq[num] > count || (freq[num] === count && num > mostFreq)) {
            count = freq[num]
            mostFreq = num
        }
    }


    return [mostFreq, count]
}

console.log(mostFreq([1,2])) // [2,2]

