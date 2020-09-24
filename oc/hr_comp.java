// Balancing Development Teams:
// https://leetcode.com/discuss/interview-question/856945/balancing-development-teams-hackerrank-oa-how-to-solve
'''
You have an array of integers. Each index represents a team and the value represents the number of developers on the team.
e.g = [5, 4, 1, 3, 4]
In the above the first team has 5 developers , second 4 developers and so on.
You are also given an integer numHires representing the number of new hires which can be hired as per the budget.
e.g. numHires = 2
The output is the maximum number of teams having equal number of developers once the new employees are hired. Note you do not need to use all your budget when hiring.
For the above output there are two solutions:
(1) Hire one employee and assign the new hire to the forth team which currently has 3 developers. Do not hire the second employee. The array now becomes :
[5, 4, 1, 4, 4]
The second, forth and fifth team have equal number of developers. They all have 4 developers. So 3 teams have equal number of developers.
(2) Hire one employee and assign to the second team and one to the fifth team. The array then becomes :
[5, 5, 1, 3, 5]
The first, second and fifth team now have equal number of developers. All 3 teams have 5 developers.
Therefore the maximum number of team having equal developers is equal to 3.
The output of the program is therefore 3
The first
'''
// APPROACH1
// first,sort the array and then use binary search to pick a possible value for the longest balanced team. 
// Check whether you can balance such length team in O(1) time using prefix_sum, you have to check n times for 
// one specific length and logn times for all the possible value. So the total time would be O(nlogn)

//  Time Complexity (NlogN)

public static int maxBalancedTeams(List<Integer> developers, int maxNewHires) { Collections.sort(developers); // sort the array in ascending order int[] prefixSum = new int[developers.size() + 1]; // make prefix sum array prefixSum[1] = developers.get(0);

	        for (int i = 1; i < prefixSum.length - 1; ++i) {
		       prefixSum[i + 1] = prefixSum[i] + developers.get(i);
	        }

	// Run binary search for the number denoting MAXIMUM NUMBER OF TEAMS HAVING SAME
	// NUMBER OF MEMBERS

	// initialize variables
	int max = developers.size(); // Possible that all teams may have same number of members
	int min = 1; // Worst case scenario, distinct number of members in all teams
	int ans = 1;
	while (min <= max) {
		int mid = (max + min) / 2; // find mid as we do in binary search denoting NUMBER OF TEAMS HAVING SAME
									// NUMBER OF DEVELOPERS

		// check if there exist some groups in which members can be added to make "mid"
		// number of groups have equal members
		if (check(prefixSum, mid, maxNewHires, developers)) {
			ans = mid;
			min = mid+1; // if there exist such case, look for a better case. Increase min to mid.
		} else {
			max = mid - 1; // if not, look for a worse case. decrease max to mid.
		}
	}
	return ans;
}

public static boolean check(int[] pSum, int len, int maxHire, List<Integer> dev) {

	// Run sliding window of length you got using binary search
	int i = 0;
	int j = len;
	while (j <= dev.size()) {
		int maxSize = dev.get(j - 1); // the last element of the sliding window will be having the max size in the
										// current window as we sorted the list at the start
		int totalMembers = maxSize * len; // for all teams to have same number of members, the total number of
											// members should be equal to (length of window)*(max team size of
											// current window)
		int currMembers = pSum[j] - pSum[i]; // the current number of members in all the teams of the current
												// sliding window
		if (currMembers + maxHire >= totalMembers) {
			return true; // Now if the current members of the window, plus the members we are allowed to
							// add, is greater or equal to the total members we wanted, return true
		} else {
			i++;
			j++;
		}
	}
	return false;
}





// APPROACH2

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class balancingDevelopmentTeams {

public static void main(String[] args) {
	// TODO Auto-generated method stub
	List<Integer> list = new ArrayList<>();
	list.add(3);
	list.add(0);
	list.add(2);
	list.add(2);
	list.add(1);
	System.out.println(maxBalancedTeams(list, 3));
}

public static int maxBalancedTeams(List<Integer> developers, int maxNewHires) {
	Collections.sort(developers); // sort the array in ascending order
	int[] prefixSum = new int[developers.size() + 1]; // make prefix sum array

	prefixSum[1] = developers.get(0);

	for (int i = 1; i < prefixSum.length - 1; ++i) {
		prefixSum[i + 1] = prefixSum[i] + developers.get(i);
	}

	// Run binary search for the number denoting MAXIMUM NUMBER OF TEAMS HAVING SAME
	// NUMBER OF MEMBERS

	// initialize variables
	int max = developers.size(); // Possible that all teams may have same number of members
	int min = 1; // Worst case scenario, distinct number of members in all teams
	int ans = 1;
	while (min <= max) {
		int mid = (max + min) / 2; // find mid as we do in binary search denoting NUMBER OF TEAMS HAVING SAME
									// NUMBER OF DEVELOPERS

		// check if there exist some groups in which members can be added to make "mid"
		// number of groups have equal members
		if (check(prefixSum, mid, maxNewHires, developers)) {
			ans = mid;
			min = mid+1; // if there exist such case, look for a better case. Increase min to mid.
		} else {
			max = mid - 1; // if not, look for a worse case. decrease max to mid.
		}
	}
	return ans;
}

public static boolean check(int[] pSum, int len, int maxHire, List<Integer> dev) {

	// Run sliding window of length you got using binary search
	int i = 0;
	int j = len;
	while (j <= dev.size()) {
		int maxSize = dev.get(j - 1); // the last element of the sliding window will be having the max size in the
										// current window as we sorted the list at the start
		int totalMembers = maxSize * len; // for all teams to have same number of members, the total number of
											// members should be equal to (length of window)*(max team size of
											// current window)
		int currMembers = pSum[j] - pSum[i]; // the current number of members in all the teams of the current
												// sliding window
		if (currMembers + maxHire >= totalMembers) {
			return true; // Now if the current members of the window, plus the members we are allowed to
							// add, is greater or equal to the total members we wanted, return true
		} else {
			i++;
			j++;
		}
	}
	return false;
}