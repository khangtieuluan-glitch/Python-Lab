# 题目（LeetCode 原题，比想象的绕）
# 给你两个已排好序的数组 nums1 和 nums2，还有一个 m 和 n：
# nums1 长度是 m + n，前 m 个是有效数据，后 n 个是 0（用来占位的空位）
# nums2 长度是 n，全是有效数据
# 要求：把 nums2 合并进 nums1，结果仍有序，直接改 nums1，不返回新数组

def merge(nums1, m, nums2, n):
    i = m - 1                    # nums1 有效数据的末尾
    j = n - 1                    # nums2 的末尾
    k = m + n - 1                # nums1 最后一个空格

    while j >= 0:                # 只要 nums2 还有数没搬，就继续
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]  # nums1 的大 → 搬它
            i -= 1
        else:
            nums1[k] = nums2[j]  # nums2 的大（或 i 走完了）→ 搬它
            j -= 1
        k -= 1                   # 无论搬谁，空格都往前挪一格


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]; merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]

    b = [1]; merge(b, 1, [], 0)
    assert b == [1]

    c = [0]; merge(c, 0, [1], 1)
    assert c == [1]

    d = [4, 5, 6, 0, 0, 0]; merge(d, 3, [1, 2, 3], 3)
    assert d == [1, 2, 3, 4, 5, 6]

    print("PASS  0088_merge_sorted_array")
