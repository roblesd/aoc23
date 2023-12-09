import re
data = ""
with open("./input/day5.input", 'r') as file:
    data = file.read()
with open("./day5spec.txt", 'r') as file:
    data = file.read()

class Range():
    def __init__(self, dest, source, length):
        self.dest_range_start = dest
        self.source_range_start = source
        self.range_length = length
    def __str__(self):
        return f"dest_range_start: {self.dest_range_start}, source_range_start: {self.source_range_start}, range_length: {self.range_length}"
    

def day5part1(seeds: list):
    # data structures
    # soil-to-fertilizer, fertilizer-to-water, water-to-light, light-to-temperature, temperature-to-humidit, humidity-to-location
    maps = [[] for i in range(7)]
    print("maps: ", maps)
    # seeds_loc = {}
    min_loc = float('inf')

    lines = data.split("\n")
    print(seeds)
    map_idx = -1
    #initialize maps list: list with idx for each map - populate with the ranges in it
    for line in lines[2:]:
        if "map" in line:
            # print(line)
            map_idx += 1
        elif line == "":
            continue
        else:
            dest, source, length = [int(num) for num in line.split()]
            maps[map_idx].append(Range(dest, source, length))

    for gen in seeds:
        for seed in gen:
            print(f"seed: {seed}")
            # loop over maps
            input_num = seed
            for i, map in enumerate(maps):
                print(f"in map {i}")
                #loop over the ranges within a map
                for j, r in enumerate(map):
                    print(f"checking range {j} in the map")
                    # if the input is in a range, map it to the destination range
                    if input_num >=  r.source_range_start and input_num < r.source_range_start + r.range_length:
                        print(f"input num {input_num} was found to be in this range: {r}")
                        input_num = r.dest_range_start + (input_num - r.source_range_start)
                        break
                #if the input number was not in a range within the map, it stays the same
            if input_num < min_loc:
                min_loc = input_num
                print(f"New lowest location: {min_loc}")
    print(f"THE MIN LOCATION IS: {min_loc}")

def day5part2():
    # data structures
    # soil-to-fertilizer, fertilizer-to-water, water-to-light, light-to-temperature, temperature-to-humidit, humidity-to-location
    maps = [[] for i in range(7)]
    print("maps: ", maps)
    # seeds_loc = {}
    min_loc = float('inf')

    lines = data.split("\n")
    seeds_ranges = [int(seed) for seed in lines[0].split(": ")[1].split()]
    #79 14 55 13
    seed_starts = []
    ranges = []
    for i in range(0, len(seeds_ranges), 2):
        seed_starts.append(seeds_ranges[i])
        ranges.append(seeds_ranges[i+1])
    print(seed_starts)
    print(ranges)

    #loop over the seed starts
    for k, seed_start in enumerate(seed_starts):
        # loop over the maps
        input_num = seed_start
        for i, map in enumerate(maps):
            print(f"in map {i}")
            #loop over the ranges within a map
            for j, r in enumerate(map):
                if input_num + ranges[k]

            

if __name__ == "__main__":
    # lines = data.split("\n")
    # seeds = [int(seed) for seed in lines[0].split(": ")[1].split()]
    # day5part1(seeds)

    day5part2()