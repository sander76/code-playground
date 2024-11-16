from copy import copy


def product(*iterables):
    # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy

    pools = [tuple(pool) for pool in iterables]

    def iter_over_new(new_collection: list[list], pool: tuple):
        if not new_collection:
            return [[val] for val in pool]

        new_coll = []
        for coll in new_collection:
            for val in pool:
                new_coll.append(coll + [val])

        return new_coll

    new_col = []
    for pool in pools:
        new_col = iter_over_new(new_col, pool)
        # for existing in other:
        #     new_existing = []
        #     for y in pool:
        #         new_existing.append(compose(y, existing))
        #     other = [new_existing]

    #     for item in other:
    #         for val in pool:
    #             # for item in other:
    #             other.append(item + [val])
    #     # for x in other:
    #     #     for res in pool:
    #     #         x.extend([res])

    return new_col


items = list(product("XY", "ABCD"))

print(items)
