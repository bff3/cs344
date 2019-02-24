from csp import parse_neighbors, CSP, min_conflicts
import itertools

def Scheduling():
    """Return an instance of the Zebra Puzzle."""
    Faculty = 'Adams Schuurman VanderLinden Bailey'.split()
    Times = 'mwf900 mwf1030 tth900 tth1030'.split()
    Classrooms = 'nh253 sb382'.split()
    Courses = 'cs104 cs108 cs112 cs212 cs214 cs336 cs344'.split()
    variables = Courses
    domains = {}
    combo = list(itertools.product(Times, Faculty, Classrooms))
    for var in variables:
        domains[var] = combo

    # domains['Adams1'] = [1, 5]

    # neighbor parsing -- not implemented
    neighbors = parse_neighbors("""cs104: cs108; cs344: cs336""", variables)
    for type in [Courses, Faculty, Times, Classrooms]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    def constraint(A, a, B, b, recurse=0):
        # a room can only have one class at each time
        same_timespace = (a[0] == b[0] and a[2] == b[2])
        # faculty member can only teach one thing at a time
        same_profslot = (a[0] == b[0] and a[1] == b[1])
        if recurse == 0:
            return constraint(B, b, A, a, 1)
        return not (same_timespace or same_profslot)

    return CSP(variables, domains, neighbors, constraint)

def solve_Scheduling(algorithm=min_conflicts, **args):
    z = Scheduling()
    ans = algorithm(z, **args)
    Courses = 'cs104 cs108 cs112 cs212 cs214 cs336 cs344'.split()
    for h in Courses:
        print(h, end=' ')
        for (var, val) in ans.items():
            if var == h:
                print(val, end=' ')
        print()
    return ans

print(solve_Scheduling())