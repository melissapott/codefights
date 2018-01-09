"""Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array."""

def almostIncreasingSequence(sequence):
    skipped = 0
    #find the smallest number in the sequence
    one_before = min(sequence) - 1
    last = one_before

    for item in sequence:

        if last < item:
            one_before = last
            last = item
        else:
            skipped += 1
            if skipped >= 2:
                return False
            if item > one_before:
                # we're going to try to skip the item from the last iteration
                last = item
            else:
                #we're going to let it pass and see if we should skip this one next time
                one_before = last

    return True

# expected result = False
sequence = [1,3,2,1]
print(almostIncreasingSequence(sequence))

# expected result = True
sequence = [1,3,2]
print(almostIncreasingSequence(sequence))