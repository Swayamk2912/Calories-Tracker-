from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt


CALORIE_LIMIT=int(input("Enter Calorie Goal Limit:"))
PROTEIN_LIMIT=int(input("Enter Protein Goal:"))
FAT_LIMIT=int(input("Enter Fat Limit:"))
CARBS_LIMIT=int(input("Enter Carbs Limit:"))


today=[]
@dataclass
class Food:
    name:str
    calories:int
    protein:int
    carbs:int
    fat:int
done=False


while not done:
  print("""
          (1) ADD A NEW FOOD ITEM
          (2) VISUALIZE PROGRESS
          (3) EXIT
          """)

  choice=int(input("Enter Your Choice:"))
 
  if choice==1:
    print("Adding items")
    name=input("Enter name of the food item:")
    calories=int(input("Enter calories:"))
    protein=int(input("Protein:"))
    carbs=int(input("Enter carbs:"))
    fat=int(input("Enter Fats:"))
    food=Food(name,calories,protein,fat,carbs)
    today.append(food)

  elif choice==2:
    calorie_sum=sum(food.calories for food in today)
    protein_sum=sum(food.protein for food in today)
    carbs_sum=sum(food.carbs for food in today)
    fat_sum=sum(food.fat for food in today)

    fig,axs = plt.subplots(2,2)
    axs[0,0].pie([protein_sum,carbs_sum,fat_sum],labels=["Proteins","Carbs","Fats",],autopct="1.1f%%")#autopct is used for simple Formatting
    axs[0,0].set_title("Macros Distribution.")
    axs[0,1].bar([0,1,2],[protein_sum,carbs_sum,fat_sum], width=0.4)
    axs[0,1].bar([0.5, 1.5 , 2.5],[PROTEIN_LIMIT,CARBS_LIMIT,FAT_LIMIT], width=0.4)
    axs[0,1].set_title("Macros Progress")
    axs[1,0].pie([calorie_sum,CALORIE_LIMIT-calorie_sum],labels=["Calories", "Remaining"],autopct="%1.1f%%")
    axs[1,0].set_title("Calories Goal Progress")
    axs[1,1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]) ,label="Calories Eaten")
    axs[1,1].plot(list(range(len(today))), [CALORIE_LIMIT] * len(today),label="Calorie Goal")
    axs[1,1].legend()
    axs[1,1].set_title("Calorie Goal Over Time")
    fig.tight_layout()
    plt.show()
  elif choice==3:
     done=True
     print("Thanks Visit Again")

  else:
     print("Invalid Choice Entered.")

    