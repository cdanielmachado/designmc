from random import sample
from reframed import Community, SteadierCom, FBA
import pandas as pd

def design(species, target, environment, size=1, iters=100, growth=0.1, modelcache=None):

    abun_tol = 1e-5
    prod_tol = 1e-5

    entries = []
    tested = set()

    for i in range(iters):
        selected = tuple(sorted(sample(species, size)))

        if selected in tested:
            #print("already tested")
            continue

        tested.add(selected)

        models = [modelcache.get_model(x, reset_id=True) for x in selected]
        community = Community(f"community_{i}", models)

        if target not in community.merged_model.reactions:
            #print("missing target")
            continue

        environment.apply(community.merged_model, exclusive=True, inplace=True, warning=False)

        sol = SteadierCom(community, growth=0.1, objective1={target: 1}, proteome=True)

        if sol is None:
            #print("infeasible")
            continue

        fobj = sol.solution.values[target]

        if fobj < prod_tol:
            #print("no production")
            continue

#        print(f"hit {fobj:.3g}")

        stable = [x for x, val in sol.abundance.items() if val > abun_tol]
        entries.append((i, ",".join(selected), ",".join(stable), len(stable), fobj))

    df = pd.DataFrame(entries, columns=["iter", "initial", "stable", "species", "value"])

    return df.sort_values("value", ascending=False)


