navi_num = int(input())
sx , sy , ex , ey = map(int, input().split())

route_arr = []
for n in range(navi_num):
    route_num = int(input())
    route = []
    for rn in range(route_num):
        route.append(list(map(int, input().split())))
    route_arr.append(route)
    
end = [ex, ey]
values_lst = []
for mid_routes in route_arr: #한 네비 경로만 가져오기
    value = 0
    routes = [[sx, sy]]
    routes.extend(mid_routes)
    routes.append(end)
    
    for r in range(1,len(routes)):
        value += abs(routes[r-1][0]-routes[r][0]) + abs(routes[r-1][1]-routes[r][1])
    values_lst.append(value)

print(values_lst.index(min(values_lst))+1)