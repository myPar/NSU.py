from typing import List


def get_zero_str(zero_numb: int):
    output_str = ""

    for i in range(zero_numb):
        output_str += "0"
    return output_str


def get_rank_list(input_list: List[int]):
    rank = len(str(max(input_list)))
    output_string_list = []

    for i in range(len(input_list)):
        str_element = str(input_list[i])
        zero_str = get_zero_str(rank - len(str_element))
        output_string_list.append(zero_str + str_element)

    return output_string_list, rank


def merge_blocks(blocks: List[List[str]]):
    out_put_block = []

    for block in blocks:
        out_put_block += block
    return out_put_block


def cast_str_list(input_list: List[str]):
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    return input_list


def radix_sort(input_block: List[str], rank_idx: int, max_rank: int) -> List[str]:
    if len(input_block) <= 1 or rank_idx >= max_rank:
        return input_block                              # return sorted block

    blocks = [[], [], [], [], [], [], [], [], [], []]

    for i in range(len(input_block)):
        blocks[int(input_block[i][rank_idx])].append(input_block[i])    # split elements on blocks; block index matches
                                                                        # numerals stands in rank_idx place in numbers in the block
    for i in range(len(blocks)):
        if len(blocks[i]) != 0:
            blocks[i] = radix_sort(blocks[i], rank_idx + 1, max_rank)
    return merge_blocks(blocks)     # merge sorted blocks


def solution(input_list: List[int]):
    return cast_str_list(radix_sort(get_rank_list(input_list)[0], 0, get_rank_list(input_list)[1]))


def main():
    input_list = list(map(int, input().split()))
    print(solution(input_list))


if __name__ == "__main__":
    main()
