class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        



# Maps n to k_count - n_count

# max(n cooutn - k count - prev(k_count - n count))

        n_count_map = defaultdict(int)
        k_minus_n_count_map = defaultdict(int)

        largest_count = 0
        largest_count_n = -1

        total_k = 0

        for n in nums:
            if n == k:
                total_k+=1
            print(n)            
            k_minus_n_count_map[n] = max(n_count_map[k] - n_count_map[n], 
                                        k_minus_n_count_map[n])
            n_count_map[n] += 1

            n_minus_k = n_count_map[n] - n_count_map[k]
            print("n_minus_k", n_minus_k)
            print("k_minus_n", n_count_map[k] - n_count_map[n])
            k_minus_n_count_map[n] = max(n_count_map[k] - n_count_map[n], 
                                        k_minus_n_count_map[n])
            print("k_minus_n_count_map[n]", k_minus_n_count_map[n])

            cur_largest_count = n_minus_k + k_minus_n_count_map[n]

            print(cur_largest_count)
            if cur_largest_count > largest_count:
                largest_count = cur_largest_count
                largest_count_n = n

            print()


        return largest_count + total_k

        




        


