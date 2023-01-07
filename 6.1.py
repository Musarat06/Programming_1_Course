# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 21:53:12 2022

@author: Musarat
"""


def  main () : 

    print( "Enter seawater levels in centimeters one per line." ) 

    print( "End by entering an empty line." ) 

    lisEntries, LisEntries2 = ListElement() 
    if len(lisEntries)>1:
      minimum = Minimum(lisEntries)

      print(f"Minimum:   {minimum:.2f} cm") 

      maximum = Maximum(lisEntries)

      print(f"Maximum:   {maximum:.2f} cm") 

      Median(lisEntries) 

      Mean(LisEntries2) 

      Deviation(LisEntries2) 

def  ListElement () : 

    ''' This fuction will take input from the user and return two Lists which will be used later''' 

    lisEntries = [] 

    LisEntries2 = [] 

    while  True : 

      try : 

        Sealevel = float(input()) 

        if  Sealevel !=  ''  : 

          lisEntries.append(Sealevel) 

          LisEntries2.append(Sealevel) 
      except : 

        if  (len(lisEntries)< 2 ): 

          print( "Error: At least two measurements must be entered!" )
          break 

        else : 

          break 

    return  lisEntries, LisEntries2 

def  Minimum (List) : 

  ''' This fuction take List as input and it will return min value of that list''' 

  min =  None 

  for  i  in  List: 

    if  min  is  None  or  i<min: 

      min = i 

  return  min 

def  Maximum (List) : 
    ''' This fuction take List as input and it will return max value of that list''' 

    max =  None 

    for  i  in  List: 

      if  max  is  None  or  i>max: 

        max = i 

    return  max 

def  Median (List) : 

    ''' This fuction take List as input and it will return Median value of the list''' 

    N = len(List) 

    SortedList=[] 

    for  i  in  range(len(List)): 

        min = Minimum(List)  

        SortedList.append(min) 

        List.remove(min) 
    if  len(SortedList)% 2 != 0 : 
       
        Median = SortedList[int((len(SortedList)/ 2 ))] 

    else : 
      
        Median = (SortedList[int((len(SortedList)/ 2 ))] + SortedList[int((len(SortedList)/ 2 ))- 1 ])/ 2 

    print(f"Median:    {Median:.2f} cm" ) 

    return  Median 

def  Mean (List) : 

    ''' This fuction take List as input and it will return the Mean (Mea) value of the list''' 

    N = len(List) 

    Sum =  0 

    for  i  in  range(len(List)): 

        Sum = Sum+(List[i]) 
    Mea=round(((Sum)/(N)), 2 ) 

    print(f"Mean:      {Mea:.2f} cm") 

    return  Mea 

def  Deviation (List) : 

    ''' This fuction take List as input and it will return the StdDeviation value of the list''' 
    N = len(List) 

    Sum =  0 

    for  i  in  List: 
        Sum = Sum+i 

    Mean = Sum/N 
    sigma =  0 

    for  i  in  List: 
        sigma = sigma+((i-Mean)** 2 ) 

    sigmaSquare = ( 1 /(N- 1 ))*(sigma) 
    StdDeviation= round(((sigmaSquare)**( 1 / 2 )), 2) 
    print(f"Deviation: {StdDeviation:.2f} cm" ) 
    return  StdDeviation 
if  __name__ ==  "__main__" : 
    main() 