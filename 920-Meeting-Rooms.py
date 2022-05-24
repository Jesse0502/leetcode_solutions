from typing import List, Optional


class Solution:
    def can_attend_meetings(self, intervals: List) -> bool:
        sortedList = sorted(intervals)
        possible_meeting = []
        for idx, i in enumerate(sortedList):
            if idx == len(sortedList) - 1:
                pass
            elif i[0] <= sortedList[idx + 1][0]:
                possible_meeting.append(i)
        return True if len(possible_meeting) else False


Solution.can_attend_meetings(Solution, [(0, 30), (5, 10), (15, 20)])
