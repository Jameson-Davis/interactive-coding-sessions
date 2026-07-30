my_friends_info = {
    "nick" : {
        "age" : 41, 
        "city": "Boulder", 
        "hobbies": ["skiing", "cooking"]
    }, 
    "Sam": {
        "age": 25, 
        "city": "chicago", 
        "hobbies": ["hiking", "coffee"], 
        "job": "professor"
    }
}

job = my_friends_info["Sam"].get("job")
print(job)

job = my_friends_info["Sam"]["job"]
print(job)

job = my_friends_info["Sam"]["job"]
print(job)