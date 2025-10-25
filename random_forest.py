import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import export_text


df = pd.read_csv(r"C:\Users\hp\Desktop\Os-PBL\Os-PBL\newdataset.csv")
print(" Dataset loaded. Class distribution:\n", df['replace'].value_counts())


X = df[['Reference bit', 'dirty bit', 'age', 'access count']]
y = df['replace']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

clf = RandomForestClassifier(
    n_estimators=100,      
    max_depth=10,           
    class_weight='balanced',
    random_state=42
)
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"\n Accuracy: {acc:.4f}\n")
print("Confusion Matrix:\n", cm)
print("\nClassification Report:\n", report)

tree_rules = export_text(clf.estimators_[0], feature_names=list(X.columns))
print("\n--- Rules of the first tree in the Random Forest ---\n")
print(tree_rules)
