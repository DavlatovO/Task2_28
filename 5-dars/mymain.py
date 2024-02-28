from mydecorators import check_admin


@check_admin
def get_staff(a,b,c):
    print("Func ishladi")


result = get_staff(10, 10, 10)


