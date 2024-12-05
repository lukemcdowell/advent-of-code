from math import floor


class Main:
    def __init__(self, input_file):
        self.data = self.get_data(input_file)

    def get_data(self, filename):
        with open(filename, "r") as file:
            return [x.strip() for x in file.readlines()]

    def part_one(self):
        # graph of page dependencies. each key is a page number and the value is a list of dependencies
        deps = {}
        total = 0
        rule = True
        for line in self.data:
            if line == "":
                rule = False
                continue

            if rule:
                X, Y = map(int, line.split("|"))
                if Y in deps:
                    deps[Y].append(X)
                else:
                    deps[Y] = [X]
            else:
                valid = True
                updates = [int(n) for n in line.split(",")]

                # check all pages are valid
                for page in updates:
                    if not valid:
                        break

                    # check all other pages d
                    for dep in updates:
                        if page == dep:
                            continue
                        # check d does not depend on p
                        if updates.index(page) > updates.index(dep):
                            if dep in deps and page in deps[dep]:
                                valid = False
                                break

                        # check p does not depend on d
                        else:
                            if page in deps and dep in deps[page]:
                                valid = False
                                break

                if valid:
                    total += updates[floor(len(updates) / 2)]
        return total

    def part_two(self):
        # graph of page dependencies. each key is a page number and the value is a list of dependencies
        deps = {}
        total = 0
        rule = True
        for line in self.data:
            if line == "":
                rule = False
                continue

            if rule:
                X, Y = map(int, line.split("|"))
                if Y in deps:
                    deps[Y].append(X)
                else:
                    deps[Y] = [X]
            else:
                valid = True
                updates = [int(n) for n in line.split(",")]

                # check all pages are valid
                for page in updates:
                    if not valid:
                        break

                    # check all other pages d
                    for dep in updates:
                        if page == dep:
                            continue
                        # check d does not depend on p
                        if updates.index(page) > updates.index(dep):
                            if dep in deps and page in deps[dep]:
                                valid = False
                                break

                        # check p does not depend on d
                        else:
                            if page in deps and dep in deps[page]:
                                valid = False
                                break

                # find the page with same number of dependencies as pages that depend on it
                if not valid:
                    for page in updates:
                        if page not in deps:
                            continue

                        d = len([d for d in deps[page] if d in updates])
                        c = 0
                        for num in [p for p in updates if p != page]:
                            if num in deps and page in deps[num]:
                                c += 1

                        if c == d:
                            total += page
                            break

        return total


if __name__ == "__main__":
    day1 = Main("input.txt")
    print("Part One Total:", day1.part_one())
    print("Part Two Total:", day1.part_two())
