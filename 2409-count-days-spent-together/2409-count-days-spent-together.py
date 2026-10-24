class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" string to day of the year
        def date_to_day(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            # Sum up days of the preceding months, then add the current day
            return sum(days_in_month[:month - 1]) + day
        
        # Convert all input dates to days of the year
        start_a = date_to_day(arriveAlice)
        end_a = date_to_day(leaveAlice)
        start_b = date_to_day(arriveBob)
        end_b = date_to_day(leaveBob)
        
        # Find the intersection of the two intervals
        latest_start = max(start_a, start_b)
        earliest_end = min(end_a, end_b)
        
        # Calculate overlapping days
        overlap = earliest_end - latest_start + 1
        
        # If overlap is negative, they don't meet at all
        return max(0, overlap)
