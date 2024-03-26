!#/usr/bin/python3
"""
 Other functions
"""
c
def create_instance(data):
    class_name = data["__class__"]
    kwargs = {k: v for k, v in data.items() if k != "__class__"}

    if class_name in globals():
        cls = globals()[class_name]
        instance = cls(**kwargs)
        return instance
