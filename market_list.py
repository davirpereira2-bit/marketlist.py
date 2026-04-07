shopping_list = ["Milk","Bread","Eggs"]

start = input('Do you want to add items?(Y/N):').upper()

if start == 'Y':

     while True :
         item = (input('What else do you need to buy?(or type "STOP" to finish):')).upper()

         if item.upper() == 'STOP':
             break

         shopping_list.append(item)
         print(f'ADDED {item},to shopping list')


else:
    print('Finish list')


print('---YOUR FINAL SHOPPING LIST---')
print(shopping_list)
