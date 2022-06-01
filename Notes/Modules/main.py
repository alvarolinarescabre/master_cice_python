import matplotlib.pyplot as plt
from modules.a import greetings
from modules.utils.b import counter

greetings()
counter(5)


nums = [1,2,3,4,5,6]

plt.plot(nums)
plt.show()