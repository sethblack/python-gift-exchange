def knn(person, others, k=3, reverse=False):
    return [n[0] for n in sorted(
        [(p, current_person.euclidean_distance(p)) for p in people],
        key=lambda f: f[1],
        reverse=reverse
    )][:k]
