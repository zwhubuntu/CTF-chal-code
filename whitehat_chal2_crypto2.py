import base64

lst = [
    'p1BxpCR4sCRTomlDonYwtG0EqSRyond0cDYwqncwpnxzqnh4r1sx',
    'q1CyqDS4tDSUpnmEpoZxuH0FrTSzpoe0dEZxrodxqoyaroi4s1ty',
    'r1DzrET4uETVqonFqpAyvI0GsUTaqpf0eFAyspeyrpzbspj4t1uz',
    's1EasFU4vFUWrpoGrqBzwJ0HtVUbrqg0fGBztqfzsqactqk4u1va',
    't1FbtGV4wGVXsqpHsrCaxK0IuWVcsrh0gHCaurgatrbdurl4v1wb',
    'u1GcuHW4xHWYtrqItsDbyL0JvXWdtsi0hIDbvshbuscevsm4w1xc',
    'v1HdvIX4yIXZusrJutEczM0KwYXeutj0iJEcwticvtdfwtn4x1yd',
    'w1IewJY4zJYAvtsKvuFdaN0LxZYfvuk0jKFdxujdwuegxuo4y1ze',
    'x1JfxKZ4aKZBwutLwvGebO0MyAZgwvl0kLGeyvkexvfhyvp4z1af',
    'y1KgyLA4bLACxvuMxwHfcP0NzBAhxwm0lMHfzwlfywgizwq4a1bg',
    'z1LhzMB4cMBDywvNyxIgdQ0OaCBiyxn0mNIgaxmgzxhjaxr4b1ch',
    'a1MiaNC4dNCEzxwOzyJheR0PbDCjzyo0nOJhbynhayikbys4c1di',
    'b1NjbOD4eODFayxPazKifS0QcEDkazp0oPKiczoibzjlczt4d1ej',
    'c1OkcPE4fPEGbzyQbaLjgT0RdFElbaq0pQLjdapjcakmdau4e1fk',
    'd1PldQF4gQFHcazRcbMkhU0SeGFmcbr0qRMkebqkdblnebv4f1gl',
    'e1QmeRG4hRGIdbaSdcNliV0TfHGndcs0rSNlfcrlecmofcw4g1hm',
    'f1RnfSH4iSHJecbTedOmjW0UgIHoedt0sTOmgdsmfdnpgdx4h1in',
    'g1SogTI4jTIKfdcUfePnkX0VhJIpfeu0tUPnhetngeoqhey4i1jo',
    'h1TphUJ4kUJLgedVgfQolY0WiKJqgfv0uVQoifuohfprifz4j1kp',
    'i1UqiVK4lVKMhfeWhgRpmZ0XjLKrhgw0vWRpjgvpigqsjga4k1lq',
    'j1VrjWL4mWLNigfXihSqnA0YkMLsihx0wXSqkhwqjhrtkhb4l1mr',
    'k1WskXM4nXMOjhgYjiTroB0ZlNMtjiy0xYTrlixrkisulic4m1ns',
    'l1XtlYN4oYNPkihZkjUspC0AmONukjz0yZUsmjysljtvmjd4n1ot',
    'm1YumZO4pZOQljiAlkVtqD0BnPOvlka0zAVtnkztmkuwnke4o1pu',
    'n1ZvnAP4qAPRmkjBmlWurE0CoQPwmlb0aBWuolaunlvxolf4p1qv',
    'o1AwoBQ4rBQSnlkCnmXvsF0DpRQxnmc0bCXvpmbvomwypmg4q1rw'
]

for i in lst:
    try:
        print base64.b64decode(i)
    except:
        pass
