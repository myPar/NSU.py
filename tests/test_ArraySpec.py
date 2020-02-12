import ArraySpec

# tests for ArraySpec (order: minimum element, maximum element, average, median, standard deviation,
# monotone elements, number)
assert (ArraySpec.solution([3, 21, 1, 2, 3, 4.5, 33.12, 13, 20]) == (1.0, 33.12, 11.18, 4.5, 11.3206271911, 1, 5))
assert (ArraySpec.solution([0]) == (0.0, 0.0, 0.0, 0.0, None, 1, 1))  # list consist with one element
assert (ArraySpec.solution([33, 2, 2, 13, 3, 3, 3, 3, 21.8, 4.12, 4.12]) == (2.0, 33.0, 8.3672727273, 3.0, 10.2032593723
                                                                             , 4, 5))
