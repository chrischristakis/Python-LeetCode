
def minStickers(self, stickers, target):
    # bitmask of all 1's, equal to the length of our target ('hello' -> 11111)
    target_bitmask = (1 << len(target)) - 1
    cache = {}
    self.min_depth = float('inf')

    def search_cache(mask, sticker_list, depth):
        if mask in cache:
            return cache[mask]

        res = search(mask, sticker_list, depth)
        cache[mask] = res
        return res

    def search(mask, sticker_list, depth=1):
        if depth > self.min_depth:
            return -1

        useful_stickers = []
        masks = []

        # Calculate bitmask with all stickers, and check if sticker is still relevant (has changed
        # mask this iteration)
        for sticker in sticker_list:
            letters = {}  # letters we can use and their quantities
            for c in sticker:
                if c not in letters:
                    letters[c] = 0
                letters[c] += 1

            # for each letter in target, check if we can satisfy it using our inventory of letters
            new_mask = mask
            for i in range(len(target)):

                # skip char if bit is already set, no need to set it again.
                current_bit = (new_mask & (1 << (len(target) - 1) - i)) >> ((len(target) - 1) - i)
                if current_bit == 1:
                    continue

                c = target[i]
                if c in letters and letters[c] > 0:
                    letters[c] -= 1  # remove from inventory

                    # Since we parse string from left to right, but bits read from right to left,
                    # we have to shift it backwards here.
                    new_mask |= 1 << (len(target) - 1) - i

            # cull this branch once we find a solution!
            if new_mask == target_bitmask:
                if depth < self.min_depth:
                    self.min_depth = depth
                return 0

            if new_mask != mask:
                masks.append(new_mask)
                useful_stickers.append(sticker)

        # now that we have useful stickers and have assembled masks, check return values.
        if len(masks) > 0:
            answers = []
            for new_mask in masks:
                steps = search_cache(new_mask, useful_stickers, depth + 1)

                if steps == -1:
                    continue
                answers.append(1 + steps)

            if len(answers) == 0:
                return -1

            return min(answers)
        else:
            return -1  # nothing was found!

    result = search(0, stickers)
    if result == -1:
        return -1
    else:
        return result + 1


ress = minStickers(["with","example","science"], "thehat")
print(ress)