class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        '''
        1 to find the common factor, we find prime numbers for each number
        2 and if its same as other number, then its a common factor (larger than 1) so connect with graph
        3 travarse the graphs and return the max length
        '''
        def setup():
            primes = []
            for num in range(2,100000+1):
                is_prime = True
                for p in primes:
                    if num%p == 0:
                        is_prime = False
                        break
                if is_prime: 
                    primes.append(num)
            return primes
        primes = setup()
        print(primes)
        # each_primes = []
        # for num in A:
        #     temp = []
        #     while num>1:
        #         if num in primes:
        #             temp.append(num)
        #         num = num//
        #     each_primes.append(temp)
                
