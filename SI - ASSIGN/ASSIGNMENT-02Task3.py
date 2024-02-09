import numpy as np
df = pd.read_csv(r"C:\Users\perur\OneDrive\Desktop\SI GUIDED data set.csv")
num_samples = 10
random_input_data = np.random.rand(num_samples, input_dim)
predictions = model.predict(random_input_data)
print("Predictions:")
print(predictions)
