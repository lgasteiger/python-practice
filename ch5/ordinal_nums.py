def test_ordinal_nums():
    """
    this function is the driver to test the ordinal numbers output logic
    """
    ordinal_nums_list = list(range(1, 36))
    teens_nums = list(range(11, 20))
    for num in ordinal_nums_list:
        if num in teens_nums:
            print(f"{num}th")
        elif num % 10 == 1:
            print(f"{num}st")
        elif num % 10 == 2:
            print(f"{num}nd")
        elif num % 10 == 3:
            print(f"{num}rd")
        else:
            print(f"{num}th")
        # end if
    # end for...in
# end test_ordinal_nums()

########################
# main app starts here #
########################
test_ordinal_nums()
