def predictor(user_age):
    if user_age<10:
        prediction= "Survived"
    else:
        prediction = "Super survived"
    return prediction