
import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np
#Salim
import gradio as gr
def Predict(inputName):
    dataFrame = pd.read_json(r"MOCK_DATA.json")
    safe_distance = 0.0020288 # a radial distance of 6 feet in kilometers
    model = DBSCAN(eps=safe_distance, min_samples=2, metric='haversine').fit(dataFrame[['Latitude', 'Longitude']])
    core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
    core_samples_mask[model.core_sample_indices_] = True
    labels = model.labels_
    dataFrame['Cluster'] = model.labels_.tolist()
    inputNameClusters = set()
    for i in range(len(dataFrame)):
        if dataFrame['User'][i] == inputName:
            inputNameClusters.add(dataFrame['Cluster'][i])
    infected = set()
    for cluster in inputNameClusters:
        if cluster != -1:
            namesInCluster = dataFrame.loc[dataFrame['Cluster'] == cluster, 'User']
            for i in range(len(namesInCluster)):
                name = namesInCluster.iloc[i]
                if name != inputName:
                    infected.add(name) 
    return infected

app = gr.Interface(fn=Predict, 
                   inputs="text", 
                   outputs="text",
                   description = "This app helps you to find out if you have been in contact with someone who has tested positive for COVID-19. As a prototype, it was trained on a dataset of 10 people and their locations. The app takes in their names and outputs the names of people they have been in contact with. The names in this demo are as follows: Adeola, Amaka, Ayoola, Bimpe, Dolapo, Femi, Mayokun, Segun, Seyi, Tolu",
                   theme="grass",
                   title="Contact Tracing Web App") 
app.launch()


