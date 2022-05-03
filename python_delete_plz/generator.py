def generator_send():
    received_value = 0

    while True:

        received_value = yield
        print("received_value = ",end=""), print(received_value)
        yield received_value * 2

gen = generator_send()
next(gen)
print(gen.send(2))

next(gen)
print(gen.send(3))

print(type(x*x for x in range(5)))