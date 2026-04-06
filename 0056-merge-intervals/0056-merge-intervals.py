class Solution(object):
    def merge(self, intervals):
        
        # Step 1: Sort by start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        # Step 2: Merge intervals
        for start, end in intervals[1:]:
            last_end = result[-1][1]

            # Overlapping case
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result