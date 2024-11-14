import time

def is_car_exists(curr_cars, car_name):
    """
    this function tests if the current car is in the recently updated list of
    cars
    """
    if car_name in curr_cars:
        output_mess = (
            f"good news, the '{car_name.title()}' is available in the "
            f"current list of cars"
        ) # end output_mess
    else:
        output_mess = (
            f"i'm sorry, but the '{car_name.title()}' is not presently found in " +
            f"the list of cars"
        ) # end output_mess
    # end if
    print(output_mess)
# end is_car_exists(curr_cars, car_name)
    
def test_is_car_exists(available_cars, car_label):
    """
    this function tests is_car_exists() against the various test cases
    """
    try:
        start_time = time.time()
        is_car_exists(available_cars, car_label)
        end_time = time.time()
        elapsed_time = end_time - start_time
        output_mess = (
            f"the time in seconds it took to complete all processes was " +
            f"{elapsed_time} seconds\n"
        ) # end output_mess
        print(output_mess)
    except Exception as e:
        output_mess = (
            f"!!!!!an unexpected, unhandled exception occurred, {e}!!!!!\n"
        )
        print(output_mess)
    # end try...catch
# end test_is_car_exists(available_cars, car_label)

##################
# app start here #
##################

###############
# test case 1 #
###############
print("*****test case 1*****")
cars_available = ['audi', 'subaru', 'tesla S30', 'cybertruck']
car = "subaru"
test_is_car_exists(cars_available, car)

###############
# test case 2 #
###############
print("*****test case 2*****")
car = 'ford'
test_is_car_exists(cars_available, car)

###############
# test case 3 #
###############
print("*****test case 3*****")
car = 'cybertruck'
test_is_car_exists(cars_available, car)

###############
# test case 4 #
###############
print("*****test case 4*****")
car = 'tesla m30'
test_is_car_exists(cars_available, car)
