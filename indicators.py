import math

# Global parameters
rho = None
dim = None
max_bound = None
max_value = 1000000.0


def calc_add_eps_indicator(p_ind_a, p_ind_b):
    """
    Calcule l'indicateur epsilon additionnel pour déterminer le maximum epsilon
    par lequel l'individu `a` doit être réduit pour que l'individu `b` soit faiblement dominé.
    """
    global max_bound, dim
    eps = (p_ind_a.v[0] / max_bound) - (p_ind_b.v[0] / max_bound)
    for i in range(1, dim):
        temp_eps = (p_ind_a.v[i] / max_bound) - (p_ind_b.v[i] / max_bound)
        if temp_eps > eps:
            eps = temp_eps
    return eps


def calc_bentley_indicator(a, b):
    """
    Calcul de l'indicateur de Bentley :
    Retourne une valeur négative si `a` domine `b`, sinon 0.
    """
    global dim
    res = 0.0
    for i in range(dim):
        if a.f[i] < b.f[i]:
            res -= 1.0
        elif a.f[i] == b.f[i]:
            res -= 0.5
    return res


def calc_fonseca_indicator(a, b, dominates_fn):
    """
    Calcul de l'indicateur de Fonseca :
    Retourne -1 si `a` domine `b`, sinon 0.
    """
    return -1 if dominates_fn(a, b) else 0


def calc_deb_indicator(a, b, dominates_fn):
    """
    Calcul de l'indicateur de Deb :
    Retourne a.fitness - 1 si `a` domine `b`, sinon max_value.
    """
    return a.fitness - 1 if dominates_fn(a, b) else max_value


def calc_zitzler_indicator(a, b, dominates_fn):
    """
    Calcul de l'indicateur de Zitzler :
    Retourne 0 si `b` domine `a`, sinon -1.
    """
    return 0 if dominates_fn(b, a) else -1


def calc_lex1_indicator(a, b):
    """
    Calcul de l'indicateur lexicographique (critère 1 en priorité).
    """
    if (a.f[0] < b.f[0]) or ((a.f[0] == b.f[0]) and (a.f[1] < b.f[1])):
        return -1
    return 0


def calc_lex2_indicator(a, b):
    """
    Calcul de l'indicateur lexicographique (critère 2 en priorité).
    """
    if (a.f[1] < b.f[1]) or ((a.f[1] == b.f[1]) and (a.f[0] < b.f[0])):
        return -1
    return 0


def calc_indicator_value(p_ind_a, p_ind_b, indicator, r, d, b, dominates_fn):
    """
    Calcul de l'indicateur global basé sur le choix de l'indicateur.
    """
    global rho, dim, max_bound
    rho = r
    dim = d
    max_bound = b

    if indicator == 0:
        return calc_add_eps_indicator(p_ind_a, p_ind_b)
    elif indicator == 2:
        return calc_bentley_indicator(p_ind_a, p_ind_b)
    elif indicator == 3:
        return calc_fonseca_indicator(p_ind_a, p_ind_b, dominates_fn)
    elif indicator == 4:
        return calc_deb_indicator(p_ind_a, p_ind_b, dominates_fn)
    elif indicator == 5:
        return calc_zitzler_indicator(p_ind_a, p_ind_b, dominates_fn)
    elif indicator == 6:
        return calc_lex1_indicator(p_ind_a, p_ind_b)
    elif indicator == 7:
        return calc_lex2_indicator(p_ind_a, p_ind_b)
    else:
        return 0