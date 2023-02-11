def truthy_falsy(chck_arg):
    mn_dt = bool(chck_arg)
    if mn_dt == True:
        return 'The value of {d} is Truthy'.format(d=chck_arg)
    else:
        return 'The value of {d} is Falsy'.format(d=chck_arg)
print(truthy_falsy(9))
