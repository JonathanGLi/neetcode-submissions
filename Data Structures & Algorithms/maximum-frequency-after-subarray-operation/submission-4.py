class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        



# Maps n to k_count - n_count

# max(n cooutn - k count - prev(k_count - n count))

        n_count_map = defaultdict(int)
        k_minus_n_count_map = defaultdict(int)

        largest_count = 0
        total_k = 0

        for n in nums:
            if n == k:
                total_k+=1
            k_minus_n_count_map[n] = max(n_count_map[k] - n_count_map[n], 
                                        k_minus_n_count_map[n])
            n_count_map[n] += 1

            n_minus_k = n_count_map[n] - n_count_map[k]

            largest_count = max(largest_count, n_minus_k + k_minus_n_count_map[n])


        return largest_count + total_k

        




        


