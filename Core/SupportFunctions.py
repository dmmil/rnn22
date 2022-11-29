from typing import List, Dict


def init_route(route_type: int, ll: int, m: int) -> List[Dict]:
    route = []
    if route_type == 0:
        right_direction = False
        for il in range(ll):
            right_direction = not right_direction
            if right_direction:
                for im in range(m):
                    route.append({'Lr': 0, 'L': il, 'M': im})
                    route.append({'Lr': 1, 'L': il, 'M': im})
            else:
                for im in reversed(range(m)):
                    route.append({'Lr': 0, 'L': il, 'M': im})
                    route.append({'Lr': 1, 'L': il, 'M': im})
    else:
        raise 'selected route type not supported in this version'
    return route
