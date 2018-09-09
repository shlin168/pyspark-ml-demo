from pyspark.sql.types import StructField, StructType, IntegerType, StringType


def get_train_schema():
    return StructType([
        StructField('Age', IntegerType(), True),
        StructField('Attrition', StringType(), True),
        StructField('BusinessTravel', StringType(), True),
        StructField('DailyRate', IntegerType(), True),
        StructField('Department', StringType(), True),
        StructField('DistanceFromHome', IntegerType(), True),
        StructField('Education', IntegerType(), True),
        StructField('EducationField', StringType(), True),
        StructField('EmployeeCount', IntegerType(), True),
        StructField('EmployeeNumber', IntegerType(), True),
        StructField('EnvironmentSatisfaction', IntegerType(), True),
        StructField('Gender', StringType(), True),
        StructField('HourlyRate', IntegerType(), True),
        StructField('JobInvolvement', IntegerType(), True),
        StructField('JobLevel', IntegerType(), True),
        StructField('JobRole', StringType(), True),
        StructField('JobSatisfaction', IntegerType(), True),
        StructField('MaritalStatus', StringType(), True),
        StructField('MonthlyIncome', IntegerType(), True),
        StructField('MonthlyRate', IntegerType(), True),
        StructField('NumCompaniesWorked', IntegerType(), True),
        StructField('Over18', StringType(), True),
        StructField('OverTime', StringType(), True),
        StructField('PercentSalaryHike', IntegerType(), True),
        StructField('PerformanceRating', IntegerType(), True),
        StructField('RelationshipSatisfaction', IntegerType(), True),
        StructField('StandardHours', IntegerType(), True),
        StructField('StockOptionLevel', IntegerType(), True),
        StructField('TotalWorkingYears', IntegerType(), True),
        StructField('TrainingTimesLastYear', IntegerType(), True),
        StructField('WorkLifeBalance', IntegerType(), True),
        StructField('YearsAtCompany', IntegerType(), True),
        StructField('YearsInCurrentRole', IntegerType(), True),
        StructField('YearsSinceLastPromotion', IntegerType(), True),
        StructField('YearsWithCurrManager', IntegerType(), True)])


def get_pred_schema():
    return StructType([
        StructField('Age', IntegerType(), True),
        StructField('BusinessTravel', StringType(), True),
        StructField('DailyRate', IntegerType(), True),
        StructField('Department', StringType(), True),
        StructField('DistanceFromHome', IntegerType(), True),
        StructField('Education', IntegerType(), True),
        StructField('EducationField', StringType(), True),
        StructField('EmployeeCount', IntegerType(), True),
        StructField('EmployeeNumber', IntegerType(), True),
        StructField('EnvironmentSatisfaction', IntegerType(), True),
        StructField('Gender', StringType(), True),
        StructField('HourlyRate', IntegerType(), True),
        StructField('JobInvolvement', IntegerType(), True),
        StructField('JobLevel', IntegerType(), True),
        StructField('JobRole', StringType(), True),
        StructField('JobSatisfaction', IntegerType(), True),
        StructField('MaritalStatus', StringType(), True),
        StructField('MonthlyIncome', IntegerType(), True),
        StructField('MonthlyRate', IntegerType(), True),
        StructField('NumCompaniesWorked', IntegerType(), True),
        StructField('Over18', StringType(), True),
        StructField('OverTime', StringType(), True),
        StructField('PercentSalaryHike', IntegerType(), True),
        StructField('PerformanceRating', IntegerType(), True),
        StructField('RelationshipSatisfaction', IntegerType(), True),
        StructField('StandardHours', IntegerType(), True),
        StructField('StockOptionLevel', IntegerType(), True),
        StructField('TotalWorkingYears', IntegerType(), True),
        StructField('TrainingTimesLastYear', IntegerType(), True),
        StructField('WorkLifeBalance', IntegerType(), True),
        StructField('YearsAtCompany', IntegerType(), True),
        StructField('YearsInCurrentRole', IntegerType(), True),
        StructField('YearsSinceLastPromotion', IntegerType(), True),
        StructField('YearsWithCurrManager', IntegerType(), True)])
