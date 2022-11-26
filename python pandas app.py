from sqlalchemy import create_engine
import pandas
import psycopg2

#loading txt file

dtxt = pandas.read_csv("E:\\my_employees.txt")

dcsv = pandas.read_csv("E:\\my_employees.csv")
djson = pandas.read_json("E:\\my_employees.json")
dxlsx = pandas.read_excel("E:\\my_employees.xlsx", sheet_name = 0)

engine = create_engine('postgresql+psycopg2:/mihirk:python3@127.0.0.1:5432/staff')
dsql = pandas.read_sql_table('employees', engine, schema = 'mystaff')
dsql.rename({"id": "ID", "first_name": "FirstName", "last_name": "LastName", "department": "Department", "phone": "Phone", "address": "Address", "salary": "Salary"}, axis = 'columns', inplace = True)

#writing scattered data
dtxt.to_sql('allstaff', engine, schema = 'mystaff',index = False)
dcsv.to_sql('allstaff', engine, schema = 'mystaff',index = False, if_exists = 'append')
djson.to_sql('allstaff', engine, schema = 'mystaff',index = False, if_exists = 'append')
dxlsx.to_sql('allstaff', engine, schema = 'mystaff',index = False, if_exists = 'append')
dsql.to_sql('allstaff', engine, schema = 'mystaff',index = False, if_exists = 'append')

query_all = pandas.read_sql_query('SELECT * FROM mystaff', engine)
query_count = pandas.read_sql_query('SELECT COUNT (*) FROM mystaff.allstaff', engine)
total_employees = query_count.iloc[0][0]

# total
query_count = pandas.read_sql_query('SELECT(*)FROM mystaff.allstaff',engine)

query_dept = pandas.read_sql_query('SELECT COUNT(DISTINCT "Department") FROM mystaff.allstaff', engine)
total_depts = query_dept.iloc[0][0]
query_epd = pandas.read_sql_query('SELECT "Department", COUNT("LastName") FROM mystaff.allstaff GROUP BY "Department"', engine)
query_epd.set_index("Department", inplace = True)
log_emp = query_epd.loc["Logistics", "count"]
mk_emp = query_epd.loc["Marketing", "count"]
sls_emp = query_epd.loc["Sales", "count"]
it_emp = query_epd.loc["IT", "count"]
hr_emp = query_epd.loc["HR", "count"]


sal_high =  query_all['Salary'].max()
sal_high =  query_all['Salary'].min()
sal_high =  query_all['Salary'].mean()



summary = [["Total number of employees", int(total_employees)],
           ["Employees in Logistics", int(log_emp)],
           ["Employees in Marketing", int(mk_emp)],
           ["Employees in Sales", int(sls_emp)],
           ["Employees in IT", int(it_emp)],
           ["Employees in HR", int(hr_emp)],
           ["Highest salary", int(sal_high)],
           ["Lowest salary", int(sal_low)],
           ["Salary average", int(sal_avg)]]

summary_html = pandas.DataFrame(summary, columns = ["Stats", "Value"])

with open("D:\\employees\\summary.html", "w") as f:
    summary_html.to_html(f, index = False, justify = 'center')
    
