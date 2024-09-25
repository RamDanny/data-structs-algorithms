class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge_sort(self, p, r):
        # one elt array
        if p == r:
            return
        else:
            # split into 2 subprobs
            q = (p + r) // 2
            self.merge_sort(p, q)
            self.merge_sort(q+1, r)
            # merge in sorted order
            a, b = [], []
            na, nb = q - p + 1, r - q
            for i in range(p, q+1):
                a.append(self.sorting_array[i])
            for i in range(q+1, r+1):
                b.append(self.sorting_array[i])
            xa, xb, xs = 0, 0, p
            while xa < na and xb < nb:
                self.comparison_count += 1
                if a[xa] <= b[xb]:
                    self.sorting_array[xs] = a[xa]
                    xs += 1
                    xa += 1
                else:
                    self.sorting_array[xs] = b[xb]
                    xs += 1
                    xb += 1
            while xa < na:
                self.sorting_array[xs] = a[xa]
                xs += 1
                xa += 1
            while xb < nb:
                self.sorting_array[xs] = b[xb]
                xs += 1
                xb += 1
            #print(self.sorting_array)
    
    def left(self, i):
        return 2*i+1
    
    def right(self, i):
        return 2*i+2
    
    def heapify(self, i, size):
        # find max child
        l, r, maxchild = self.left(i), self.right(i), i
        if 2*i+1 < size and self.sorting_array[l] > self.sorting_array[maxchild]:
            maxchild = 2*i + 1
        if 2*i+2 < size and self.sorting_array[r] > self.sorting_array[maxchild]:
            maxchild = 2*i + 2
        if maxchild != i:
            # swap max child with out-of-place parent, repeat recursively
            self.sorting_array[i], self.sorting_array[maxchild] = self.sorting_array[maxchild], self.sorting_array[i]
            self.heapify(maxchild, size)
            self.comparison_count += 1

    def build_heap(self, size):
        # call heapify on all non-leaves
        for i in range(size//2 - 1, -1, -1):
            self.heapify(i, size)
            self.comparison_count += 1
    
    def heapsort(self, size):
        k = 0
        self.build_heap(size)
        for i in range(size-1, 0, -1):
            # reduce heap size
            self.sorting_array[0], self.sorting_array[i] = self.sorting_array[i], self.sorting_array[0]
            k += 1
            self.heapify(0, size-k)
            #print(self.sorting_array, size-k)

    def heap_sort(self):
        self.heapsort(len(self.sorting_array))

    def insertion_sort(self):
        # consider the unsorted subarray
        for i in range(1, len(self.sorting_array)):
            x = self.sorting_array[i]
            j = i-1
            while j >= 0:
                # sort the next elt into place
                self.comparison_count += 1
                if x < self.sorting_array[j]:
                    self.sorting_array[j+1] = self.sorting_array[j]
                else:
                    break
                j -= 1
            self.sorting_array[j+1] = x
            #print(self.sorting_array)

if __name__ == '__main__':
    a = [3, 6, 1, 4, 2, 5]
    s = Sorting(a)
    s.heap_sort()
