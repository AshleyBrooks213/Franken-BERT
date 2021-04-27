You can add any Notebook links and descriptions here.

# These two notebooks contains data searching from ACAB.csv and Brooklyn_Center.csv files. (Located in the Files folder)

- The purpose of this was to search for tweets that were posted by News sources to find True instances of Police brutality. (This was our starting point for this task.)
- While there are True cases that have been reported from new sources in these data sets, there is still some cleaning that needs done to really parse out those cases.
- We would also like to find True cases that were posted by actual people. 
- I think the difference between them (that makes this such an interesting problem) is that a person that tweets about an occurence is likely to have some kind of emotional component to the tweet in response to the event. The idea is to keep the model from predicting emotional opinions and Hate Speech as True, even though some instances may contain aspects such as these and still be considered a True occurence.
- As you parse out the True instances, you are likely to find that you have more False tweets than True. You should be able to create **Synthetic Data** either using the SMOTE library or other similar methods to balance out the data in order to prevent bias. 
- Please, keep this in mind as you continue to work on this project with Labs. 
- Data sourcing appears to be the biggest obstacle.

ACAB: https://colab.research.google.com/drive/1KHmpvp0ka5fu407X4OQyYiNRkF2L29LW?usp=sharing

Brooklyn Center: https://colab.research.google.com/drive/1fYpFiJm-HBJ5d38qdauj6veCmTUCevGh?usp=sharing
