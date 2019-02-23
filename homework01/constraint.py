from csp import parse_neighbors, min_conflicts, CSP, UniversalDict, different_values_constraint


def Zebra():
    """Return an instance of the Zebra Puzzle."""
    Faculty = 'Adams Schuurman VanderLinden Bailey'.split()
    Times = 'mwf900 mwf1030 tth900 tth1030'.split()
    Classroom = 'nh253 sb382'.split()
    variables = Faculty + Times + Classroom
    domains = {}
    for var in variables:
        domains[var] = list(range(1, 7))

    domains['Adams'] = [1, 5]
    domains['Schuurman'] = [2, 6]
    domains['Bailey'] = [3]
    domains['VanderLinden'] = [4]

    neighbors = parse_neighbors("""Bailey: mwf900; Adams: tth900""", variables)
    for type in [Faculty, Times, Classroom]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    def zebra_constraint(A, a, B, b, recurse=0):
        same = (a == b)
        next_to = abs(a - b) == 1
        if A == 'Adams' and B == 'tth900':
            return same
        if A == 'Bailey' and B == 'mwf900':
            return same
        if recurse == 0:
            return zebra_constraint(B, b, A, a, 1)
        if ((A in Faculty and B in Faculty) or
                (A in Times and B in Times) or
                (A in Classroom and B in Classroom)):
            return not same
        raise Exception('error')
    return CSP(variables, domains, neighbors, zebra_constraint)


def solve_zebra(algorithm=min_conflicts, **args):
    z = Zebra()
    ans = algorithm(z, **args)
    for h in range(1, 7):
        print('CS', h, end=' ')
        for (var, val) in ans.items():
            if val == h:
                print(var, end=' ')
        print()
    return ans['Bailey'], ans['tth1030'], z.nassigns, ans

print(solve_zebra())