"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(weigth,time,total_doze_24):
  """ Calculating the dose of new person """
  while True:
    if (total_doze_24)<=(3250):
      newDose = 750
      if time>=6:
        newDose = weigth*15
        break
      else:
        newDose = 0
        break
    else:
      if time>=6:
        newDose = weigth*15
        newDose = 4000-total_doze_24
        break
      else:
        newDose = 0
        break
    break
  
  return newDose
    
def main():
  weigth = int(input("Patient's weight (kg): "))
  time = int(input("How much time has passed from the previous dose (full hours): "))
  total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))

  newDose = calculate_dose(weigth,time,total_doze_24)
  print(f"The amount of Parasetamol to give to the patient: {newDose}")
    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()




