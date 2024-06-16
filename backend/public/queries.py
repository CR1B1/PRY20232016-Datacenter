def sql_graph_priority(_id:int=None):
    if _id is not None:
        return f"""
        SELECT ps.priority,count(ps.priority) as count_priority
        FROM public_incidence as pui 
        INNER JOIN public_subject AS ps ON pui.incidence_subject_id = ps.id 
        INNER JOIN authentication_user AS au on pui.user_id = au.id
        WHERE au.user_area_id = {_id}
        GROUP BY ps.priority
    """
    else:
        return f"""
        SELECT ps.priority,count(ps.priority) as count_priority
        FROM public_incidence as pui 
        INNER JOIN public_subject AS ps ON pui.incidence_subject_id = ps.id 
        INNER JOIN authentication_user AS au on pui.user_id = au.id
        GROUP BY ps.priority
    """
        


def sql_graph_solved(_id:int):
    if _id is not None:
        return f"""
        SELECT CASE pui.solved WHEN false THEN 'NO SOLUCIONADO' WHEN true THEN 'SOLUCIONADO' END "solution", count(pui.solved) as count_solution
        FROM public_incidence as pui
        INNER JOIN authentication_user as au ON pui.user_id = au.id
        WHERE au.user_area_id = {_id} GROUP BY pui.solved
    """
    else:
        return f"""
        SELECT CASE pui.solved WHEN false THEN 'NO SOLUCIONADO' WHEN true THEN 'SOLUCIONADO' END "solution", count(pui.solved) as count_solution
        FROM public_incidence as pui 
        GROUP BY pui.solved
    """ 


def sql_incidences_per_user(id:int=None):
    if id is not None:
        return f"""
        SELECT pui.user_id, au.username, count(pui.user_id) as count_incidences 
        FROM public_incidence as pui INNER JOIN authentication_user as au ON pui.user_id = au.id 
        WHERE au.user_area_id = {id} GROUP BY pui.user_id, au.username
    """
    else:
        pass
    return f"""
        SELECT pui.user_id, au.username, count(pui.user_id) as count_incidences 
        FROM public_incidence as pui 
        INNER JOIN authentication_user as au ON pui.user_id = au.id 
        GROUP BY pui.user_id, au.username
    """
    