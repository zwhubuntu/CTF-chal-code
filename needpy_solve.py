import base64
import marshal
import py_compile
import time
import zlib

with open('needpy.pyc', 'wb') as fc:
    fc.write('\0\0\0\0')
    codeobject = marshal.loads(zlib.decompress(base64.b64decode(
        'eJxtVP9r21YQvyd/ieWm66Cd03QM1B8C3pggUuzYCSWstHSFQijyoJBhhGq9OXJl2ZFeqAMOK6Q/94f9Ofvn1s+d7Lgtk/3O997du/vc584a0eqpYP2GVfwDEeOrKCU6g2LRRyiK4oooFsVVUSqkqxTX6J1F+SfSNYrrdKPorC76luhbpOEGCZNFZw2KG3Rmk26QtuXi3xTb7ND6/aVu0g2RuvhEcZNut5lAGbTvAFbyH57TkYLKy8J6xpDvQxiiiaIlcdqJxVcHbXY6bXNlZgviPCrO0+StqfKd88gzNh/qRZyMdWHE29TZZvIkG7eZFRGGRcBmsXJaUoKCQ9fWKHwSqNeKFnsM5PnwJ7q2aKk4AFhcWtQCh+ChB5+Lu/RmyYUxmtOEYxas7i/2iuR7Ti14OEOSmU0RADd4+dQzbM1FJhukAUeQ+kZROuLyioagrau76kc1slY1NNaY/y3LAxDQBrAICJisV2hMdF2lxQcyFuMoqcX3+TCl6xotqzSpkqmxYVmjXVjAXiwBsEfBrd1VvTvLCj2EXRnhoryAKdpxcIgJcowUB68yAx/tlCAuPHqDuZo0CN3CUGHwkPhGMA7aXMfphjbmQLhLhJcHa0a+mpgB191c1U1lnHJQbgkHx+WGxeJbejnpkzSavo2jkxZ7i725npGAaTc8FXmUjbUETHUmkxXN5zqL5WiWxwE7Bc11yyYzNJpN02jerq+DzNNodfxOX8kE4FcmYKscDdYD1oPGGucXYNmgs1F+NTf3GOt3Mg7b+NTVruqoQyX1hOEUacKw+AGbP38ZOq9THRXaSbL5pXGQ8bho/Z/lrzQaHxdoCrlev+t6nZ7re57r+57rHXag93Deh37k+vuw9zorO/Qj/B50cAf2oyOsvut3D+ADWxdxfN/1Drqu39mHzvcRswv/Hvz7sHeg9w8Qzy99DzuFwxhPhs6zWTbOI3OZRiaZZcVj5wVwOklx7OwVxR47PR46r/SVM8ulBJic9zku/eqY/MqJxiDj+Gd55wS3f35pbLCzHoEwzKKpDkN5i+TR+1AYCWTo5IV0Z0P9H3phDDd6lMzPdS5bbo9eJGbTsW9nbDqLL1N9Iq+rRxDbll2x67a9Lf27hw5uK1s1rZr6DOPF+FI=')))
    py_compile.wr_long(fc, long(time.time()))
    marshal.dump(codeobject, fc)
    fc.flush()
    fc.seek(0, 0)
    fc.write(py_compile.MAGIC)
