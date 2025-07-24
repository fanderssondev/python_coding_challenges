def check_result[T](func: T, expected_result: T) -> None:
    """
    Compares a the return value of the tested function (func) against an
    expected result and prints the outcome.

    Args:
        func (T): The return value of the function being checked.
        expected_result (T): The expected output of the function (func).

    Returns:
        None: This function prints the result and does not return anything.
    """
    print(f"{'✅' if func == expected_result else '❌'}\t {func}\t {expected_result}")


# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python
#
# Write a class called User that is used to calculate the amount that a user will progress through a ranking system
# similar to the one Codewars uses.
#
# Business Rules:
# A user starts at rank -8 and can progress all the way to 8.
# There is no 0 (zero) rank. The next rank after -1 is 1.
# Users will complete activities. These activities also have ranks.
# Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
# The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of
# the activity
# A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next
# level
# Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't
# throw any progress away). The exception is if there is no other rank left to progress towards (Once you reach rank 8
# there is no more progression).
# A user cannot progress beyond rank 8.
# The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an
# error.
# The progress is scored like so:
#
# Completing an activity that is ranked the same as that of the user's will be worth 3 points
# Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
# Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
# Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater
# the difference between rankings the more the progression will be increased. The formula is 10 * d * d where d equals
# the difference in ranking between the activity and the user.
# Logic Examples:
# If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
# If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
# If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
# If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being
# upgraded to rank -7 and having earned 60 progress towards their next rank
# If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)
# Code Usage Examples:
# user = User()
# user.rank # => -8
# user.progress # => 0
# user.inc_progress(-7)
# user.progress # => 10
# user.inc_progress(-5) # will add 90 progress
# user.progress # => 0 # progress is now zero
# user.rank # => -7 # rank was upgraded to -7


# class User:
#     rank = -8
#     progress = 0

#     def inc_progress(self, rank_progress: int) -> None:
#         if self.rank == rank_progress:
#             self.progress += 3
#         elif self.rank - 1 == rank_progress:
#             self.progress += 1
#         elif self.rank < rank_progress:
#             d = 0
#             if self.rank < 0 and rank_progress > 0:
#                 d = self.rank + rank_progress - 1
#             elif self.rank < 0 and rank_progress < 0:
#                 d = abs(self.rank) - abs(rank_progress)
#             self.progress += 10 * d * d
#         else:
#             pass

#         if self.progress >= 100:
#             self.rank += self.progress // 100
#             self.progress %= 100

#         if self.rank == 0:
#             self.rank = 1


# class User:
#     def __init__(self):
#         self._ranks = [n for n in range(-8, 9) if n != 0]
#         self.rank_index = 0  # starts at rank -8
#         self.progress = 0

#     @property
#     def rank(self):
#         return self._ranks[self.rank_index]

#     def inc_progress(self, activity_rank):
#         if activity_rank not in self._ranks:
#             raise ValueError("Invalid rank")

#         if self.rank == 8:
#             return  # No more progress allowed

#         activity_index = self._ranks.index(activity_rank)
#         d = activity_index - self.rank_index

#         if d == 0:
#             points = 3
#         elif d == -1:
#             points = 1
#         elif d <= -2:
#             points = 0
#         else:
#             points = 10 * d**2

#         self._add_progress(points)

#     def _add_progress(self, points):
#         self.progress += points

#         while self.progress >= 100 and self.rank < 8:
#             self.progress -= 100
#             self.rank_index += 1

#         if self.rank == 8:
#             self.progress = 0


class User:
    def __init__(self) -> None:
        self.__ranks = [n for n in range(-8, 9) if n != 0]
        self.__total = 0

    @property
    def rank(self) -> int:
        return self.__ranks[min(self.__total // 100, int(len(self.__ranks) - 1))]

    @property
    def progress(self) -> int:
        return self.__total % 100 if self.rank != 8 else 0

    def inc_progress(self, value: int) -> None:
        if value not in self.__ranks:
            raise ValueError("Invalid rank")

        if self.rank == 8:
            return  # No more progress allowed

        d = self.__ranks.index(value) - self.__ranks.index(self.rank)
        self.__total += {-1: 1, 0: 3}.get(d, 10 * d**2)


# Tests ==================================
print("user")
user = User()
user.inc_progress(-8)
check_result(user.rank, -8)
check_result(user.progress, 3)

print("user2")
user2 = User()
user2.inc_progress(-7)
check_result(user2.rank, -8)
check_result(user2.progress, 10)

print("user3")
user3 = User()
user3.inc_progress(-6)
check_result(user3.rank, -8)
check_result(user3.progress, 40)

print("user4")
user4 = User()
user4.inc_progress(-5)
check_result(user4.rank, -8)
check_result(user4.progress, 90)

print("user5")
user5 = User()
user5.inc_progress(-4)
check_result(user5.rank, -7)
check_result(user5.progress, 60)

print("user6")
user6 = User()
user6.inc_progress(1)
check_result(user6.rank, -2)
check_result(user6.progress, 40)
user6.inc_progress(1)
check_result(user6.rank, -2)
check_result(user6.progress, 80)
