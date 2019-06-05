# test function dot


def utils_varmat_dot():
    import numpy as np
    from limetr.utils import VarMat

    ok = True
    # setup test problem
    # -------------------------------------------------------------------------
    var_mat = VarMat.testProblem()
    var_mat_rank_1 = VarMat.testProblemRank1()

    tol = 1e-10

    # test the dot product with vector
    # -------------------------------------------------------------------------
    x = np.random.randn(var_mat.num_data)

    tr_y = var_mat.varMat().dot(x)
    my_y = var_mat.dot(x)

    tr_y_rank_1 = var_mat_rank_1.varMat().dot(x)
    my_y_rank_1 = var_mat_rank_1.dot(x)

    err = np.linalg.norm(tr_y - my_y)
    err_rank_1 = np.linalg.norm(tr_y_rank_1 - my_y_rank_1)
    ok_vec = err < tol
    ok_vec_rank_1 = err_rank_1 < tol

    if not ok_vec:
        print('err', err)
        print('tr_y', tr_y)
        print('my_y', my_y)

    if not ok_vec_rank_1:
        print('err_rank_1', err_rank_1)
        print('tr_y_rank_1', tr_y_rank_1)
        print('my_y_rank_1', my_y_rank_1)

    # test the dot product with matrix
    # -------------------------------------------------------------------------
    x = np.random.randn(var_mat.num_data, 2)

    tr_y = var_mat.varMat().dot(x)
    my_y = var_mat.dot(x)

    tr_y_rank_1 = var_mat_rank_1.varMat().dot(x)
    my_y_rank_1 = var_mat_rank_1.dot(x)

    err = np.linalg.norm(tr_y - my_y)
    err_rank_1 = np.linalg.norm(tr_y_rank_1 - my_y_rank_1)
    ok_mat = err < tol
    ok_mat_rank_1 = err_rank_1 < tol

    if not ok_mat:
        print('err', err)
        print('tr_y', tr_y)
        print('my_y', my_y)

    if not ok_mat_rank_1:
        print('err_rank_1', err_rank_1)
        print('tr_y_rank_1', tr_y_rank_1)
        print('my_y_rank_1', my_y_rank_1)

    ok = ok and ok_vec and ok_vec_rank_1 and ok_mat and ok_mat_rank_1

    return ok
