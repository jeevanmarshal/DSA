# class car:
#     def __init__(self, engine, model):
#         self.color = engine
#         self.model = model

#     def engine_start(self):
#         print(self.model,"Started")
    
#     def engine_stopped(self):
#         print(self.model, 'Stopped')

# benz=car('red','Innovo')
# print(benz.color)
# benz.engine_start()
# benz.engine_stopped()

numbers = [3,7,2,9,5]

max = numbers[0]

for num in numbers:
    if max < num:
        max = num

print (max)




