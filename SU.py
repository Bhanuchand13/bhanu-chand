def Nnumberele(list1, N):
   new_list = []
   for i in range(0, N):
      max1 = 0
   for j in range(len(list1)):
      if list1[j] > max1:
         max1 = list1[j];
         list1.remove(max1);
         new_list.append(max1)
      print("Largest numbers are ",new_list)
      my_list = [14,67,48,23,5,62]
      N = 4
