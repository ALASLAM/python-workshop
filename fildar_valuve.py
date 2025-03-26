def fileter_value(cost):
    if(cost>350):
        return True
    else:
        return False
price=[2541,5461,4548,5184,542]
filter_value=filter(fileter_value,price)
