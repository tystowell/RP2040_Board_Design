dt = 0.000001
time = .1
samples = int(time//dt)
period = 0.0005
result = np.zeros(samples)
samplesPerPeriod = int(period//dt)

v = 0
r = 2200
c = .000002
c1 = 0
c2 = 0

n = 0
while n < len(result):
    if n % samplesPerPeriod == 0:
        if v == 0:
            v = 3.3
        else:
            v = 0

    temp = c2
    c2 += dt * (c1 - c2)/(r * c)
    c1 += dt * ((temp - c1)/(r * c) + (v - c1)/(r * c))
    
    result[n] = c2

    n += 1
    
fig = plt.subplots(figsize=(12,6))
    
custom_x = np.arange(0, time, 0.01)

plt.plot(result)

#plt.xticks(custom_x)
plt.ylim([1.63, 1.68])
plt.show()
