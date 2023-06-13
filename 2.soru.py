import pandas as pd

veriler = {
    'age': ['genc', 'genc', 'orta_yasli', 'yasli', 'yasli', 'yasli', 'orta_yasli', 'genc', 'genc', 'yasli', 'genc', 'orta_yasli', 'orta_yasli', 'yasli'],
    'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'],
    'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no'],
    'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent'],
    'buy_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df = pd.DataFrame(veriler)
print(df.to_string(index=False))


# P(C): P(buys_computer = "yes") ve P(buys_computer = "no") hesapla
P_yes = df[df['buy_computer'] == 'yes'].shape[0] / df.shape[0]
P_no = df[df['buy_computer'] == 'no'].shape[0] / df.shape[0]

# P(X|C) değerlerini hesapla
P_age_X_yes = df[(df['age'] == 'genc') & (df['buy_computer'] == 'yes')].shape[0] / df[df['buy_computer'] == 'yes'].shape[0]
P_age_X_no = df[(df['age'] == 'genc') & (df['buy_computer'] == 'no')].shape[0] / df[df['buy_computer'] == 'no'].shape[0]

P_income_X_yes = df[(df['income'] == 'medium') & (df['buy_computer'] == 'yes')].shape[0] / df[df['buy_computer'] == 'yes'].shape[0]
P_income_X_no = df[(df['income'] == 'medium') & (df['buy_computer'] == 'no')].shape[0] / df[df['buy_computer'] == 'no'].shape[0]

P_student_X_yes = df[(df['student'] == 'yes') & (df['buy_computer'] == 'yes')].shape[0] / df[df['buy_computer'] == 'yes'].shape[0]
P_student_X_no = df[(df['student'] == 'yes') & (df['buy_computer'] == 'no')].shape[0] / df[df['buy_computer'] == 'no'].shape[0]

P_credit_rating_X_yes = df[(df['credit_rating'] == 'fair') & (df['buy_computer'] == 'yes')].shape[0] / df[df['buy_computer'] == 'yes'].shape[0]
P_credit_rating_X_no = df[(df['credit_rating'] == 'fair') & (df['buy_computer'] == 'no')].shape[0] / df[df['buy_computer'] == 'no'].shape[0]

# P(X|buys_computer = "yes") ve P(X|buys_computer = "no") hesapla
P_X_yes = P_age_X_yes * P_income_X_yes * P_student_X_yes * P_credit_rating_X_yes
P_X_no = P_age_X_no * P_income_X_no * P_student_X_no * P_credit_rating_X_no

# P(X|buys_computer = "yes") * P(buys_computer = "yes") ve P(X|buys_computer = "no") * P(buys_computer = "no") hesapla
P_X_C_yes = P_X_yes * P_yes
P_X_C_no = P_X_no * P_no


if P_X_C_yes > P_X_C_no:
    print("X örneği buys_computer = yes sınıfına aittir.")
else:
    print("X örneği buys_computer = no sınıfına aittir.")
