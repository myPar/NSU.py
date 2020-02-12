import SimpleSort

# tests for simpleSort solution
assert (SimpleSort.solution([2, 3, 1, 44, 5, 2, 6, 64, 34, 11]) == [1, 2, 2, 3, 5, 6, 11, 34, 44, 64])
assert (SimpleSort.solution([0]) == [0])
assert (SimpleSort.solution([2, 1, 3, 78, 30, 4, 0]) == [0, 1, 2, 3, 4, 30, 78])
assert (SimpleSort.solution([34.1, 43.5, 12, 31.234, 5, 4, 3.25, 1, 1]) == [1.0, 1.0, 3.25, 4.0, 5.0, 12, 31.234, 34.1,
                                                                            43.5])
