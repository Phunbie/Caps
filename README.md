**Cassava Leaf Disease Classification**

The purpose of this project is to identify the type of disease present on a Cassava Leaf image.

Cassava is the second largest provider of carbohydrate in Africa, Obviously its importance in food security in Africa cannot be over emphasized. At least 80% of household farms in Sub-Saharan Africa grow this starchy root, but viral diseases are major sources of poor yields. With the help of data science, it may be possible to identify common diseases so they can be treated.

Existing methods of disease detection in cassava require farmers to solicit the help of government-funded agricultural experts to visually inspect and diagnose the plants. This method is labor-intensive, has few reach and expensive, which made it out of the reach for majority of local farmers. To really tackle this problem, an effective solution is needed. This solution must perform well under significant constraints, since African farmers may only have access to mobile-quality cameras with low-bandwidth.

The purpose for this project task is to classify each cassava image into four disease categories or a fifth category indicating a healthy leaf. With this, farmers may be able to quickly identify diseased plants, potentially saving their crops before they inflict irreparable damage and also creating a simple web app where farmers can upload the picture of their plant and the app will tell if the plant has a particular disease and also give farmers advice on what to do based on the diagnose.


**Uploading data**
The data was gotten from kaggle, I used colab in creating my notebooks,in order to be able to run Zoomcampcapstone notebook you need to download an API from kaggle and place it beside this notebook. 
My second notebook(TFlite) was used to create a tflite model from the best model from my first notebook

**Testing the code locally**

In order to be able to use the lambda_function.py you need to download the cassava.tflite model [from here](https://drive.google.com/file/d/1-6r_gZzszIS1OMWcZcaNNXsxqFn0m8nT/view?usp=drivesdk).if you want to run the tflite.ipynb notebook you will need the [.h5 model ](https://drive.google.com/file/d/1vZXYte_tkP3iD8_iMKeE0ZUzRaBNZMKT/view?usp=drivesdk).The docker file and every other file needed to test the code locally is already in this repository. To test my code you need to run the command for building  and runing the dockerfile on your terminal.

run commands below

docker build -t cassava-model .





docker run -it --rm -p 8080:8080 cassava-model:latest




you can now run the test.py to get prediction from the containerised lambda-function.py. 
