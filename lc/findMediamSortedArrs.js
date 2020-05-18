
// * @param {number[]} nums1
// * @param {number[]} nums2
// * @return {number}




var findMedianSortedArrays = function (nums1, nums2) {
  //get the smaller array 
  if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1)
  let start = 0;
  let end = nums1.length

  while (start <= end) {
    // get partitions 
    let partitionX = (end + start) / 2 | 0
    let partitionY = (nums1.length + nums2.length + 1) / 2 - partitionX | 0

    let minX = partitionX == 0 ? -Infinity : nums1[partitionX - 1]
    let maxX = partitionX == nums1.length ? Infinity : nums1[partitionX]

    let minY = partitionY == 0 ? -Infinity : nums2[partitionY - 1]
    let maxY = partitionY == nums2.length ? Infinity : nums2[partitionY]

    if (minX <= maxY && minY <= maxX) {
      //found 
      // odd 
      return Math.Max(minX, minY)

      // even
      return (Math.max(minX, maxY), Math.min(minY, maxX)) / 2


    } else if (minX > minY) {
      end = partitionX - 1
    } else {
      start = partition + 1
    }

  }
};