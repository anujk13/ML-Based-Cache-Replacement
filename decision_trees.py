import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE


df = pd.read_csv(r"C:\Users\hp\Desktop\Os-PBL\Os-PBL\newdataset.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
X = df[['reference_bit', 'dirty_bit', 'age', 'access_count']]
y = df['replace']


pipeline = Pipeline([
    ('smote', SMOTE(random_state=42)),
    ('classifier', DecisionTreeClassifier(random_state=42))
])


cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


y_pred = cross_val_predict(pipeline, X, y, cv=cv, n_jobs=-1)


overall_accuracy = accuracy_score(y, y_pred)
overall_f1 = f1_score(y, y_pred)
cm = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)


print("\n=== Final Evaluation Results ===")
print(f"Overall Accuracy: {overall_accuracy:.4f}")
print(f"Overall F1 Score: {overall_f1:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)