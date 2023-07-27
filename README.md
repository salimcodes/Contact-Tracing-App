# Contact Tracing Web App

![image](https://github.com/salimcodes/Contact-Tracing-App/assets/64667212/e7ffc20f-cda2-4a8d-b8b7-bddd8884c5cd)

This is a simple Contact Tracing Web App that helps you find out if you have been in contact with someone who has tested positive for COVID-19. Please note that this app is a prototype and is currently trained on dummy data of 10 people and their locations. 

## How it Works
The app uses the DBSCAN clustering algorithm to identify potential contacts based on a safe distance of 6 feet (approximately 0.0020288 kilometers). It takes in the name of a person and outputs the names of people they may have come into contact with. The names in this demo are as follows: **`Adeola`, `Amaka`, `Ayoola`, `Bimpe`, `Dolapo`, `Femi`, `Mayokun`, `Segun`, `Seyi`, `Tolu`.**

## Usage
1. Input the name of a person in the provided text field.
2. Click the "Submit" button to find potential contacts.

Please be aware that this is a demo version, and the results are based on dummy data. For a more comprehensive and accurate contact tracing experience, the app will be further developed and trained on real-world data.

## Try it Out Locally
To run the Contact Tracing Web App, ensure you have the required dependencies, such as pandas, scikit-learn, numpy, and gradio. Simply execute the code provided in your Python environment and interact with the app in your web browser.

Feel free to contribute to the development of this app or use it as a foundation for more robust contact tracing solutions.

*Disclaimer: This app is for demonstration purposes only and does not provide real contact tracing functionality.*
