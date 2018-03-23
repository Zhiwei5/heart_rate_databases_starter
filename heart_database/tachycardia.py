def tachycardia(heart_rate, age):
    """
               Determine whether or not a patients has

               :param heart_rate: the input should be a float
               :param age: the input should be a float
               :raises ValueError: if the input includes string


               :returns: return a boolean. if the patients has Tachycardia, a variable named diagnosis would
               equal to one, if not, diagnosis would equal to 0.
               :rtype: int

               """
    try:
        import logging
    except ImportError:
        print("Necessary imports failed")
        return
    logging.basicConfig(filename='tachycardia.log', filemode='w',
                        level=logging.DEBUG)

    try:
        float(heart_rate)
    except ValueError:
        print("your input has a invalid value: {}".format(heart_rate))
        return None

    try:
        float(age)
    except ValueError:
        print("your input has a invalid value: {}".format(age))
        return None

    diagnosis = 0

    if age <= 0.005479:
        if heart_rate > 159:
            diagnosis = 1
    elif age <= 0.016438:
        if heart_rate > 166:
            diagnosis = 1
    elif age <= 0.05769:
        if heart_rate > 182:
            diagnosis = 1
    elif age <= 0.166666:
        if heart_rate > 179:
            diagnosis = 1
    elif age <= 0.41666:
        if heart_rate > 186:
            diagnosis = 1
    elif age <= 0.91666 :
        if heart_rate > 169:
            diagnosis = 1
    elif age <= 2:
        if heart_rate > 151:
            diagnosis = 1
    elif age <= 4:
        if heart_rate > 137:
            diagnosis = 1
    elif age <= 7:
        if heart_rate > 133:
            diagnosis = 1
    elif age <= 11:
        if heart_rate > 130:
            diagnosis = 1
    elif age <= 15:
        if heart_rate > 119:
            diagnosis = 1
    else:
        if heart_rate > 100:
            diagnosis = 1

    return diagnosis
